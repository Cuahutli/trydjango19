from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.db.models import Q

from django.utils import timezone


from .models import Post
from .forms import PostForm

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	if not request.user.is_authenticated():
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if request.POST:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			messages.success(request, "Creado correctamente")
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			messages.error(request, "Error al crear")
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all()
	print(queryset_list)
	query = request.GET.get("q")
	print("query", query)
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) | 
			Q(content__icontains=query) | 
			Q(user__first_name__icontains=query) | 
			Q(user__last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list,2)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
	}
	return render(request, "post_list.html", context)

def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Actualizado", extra_tags="some-tag")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form
	}
	return render(request, "post_form.html", context)

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Eliminado Correctamente")
	return redirect("posts:list")
