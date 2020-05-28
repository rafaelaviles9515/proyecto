from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.biblioteca.forms import LibroForm
from apps.biblioteca.models import Libro
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request):
	return render(request,'libro/index.html')

#@permission_required('biblioteca.libro_view')
def libro_view(request):
	if request.method == 'POST':
		form = LibroForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('libro_listar')
	else: 
			form = LibroForm()
			return render(request, 'libro/libro_form.html', {'form':form})

def libro_list(request):
	listlibro = Libro.objects.all().order_by('codigo')
	contexto = {'listlibro':listlibro} 
	return render(request, 'libro/libro_list.html', contexto)

#@permission_required('biblioteca.libro_edit')
def libro_edit(request, id_libro):
	libro = Libro.objects.get(codigo=id_libro)
	if request.method == 'GET':
		form = LibroForm(instance=libro)
	else:
		form = LibroForm(request.POST, instance=libro)
		if form.is_valid():
			form.save()
			return redirect('libro_listar')
	return render(request, 'libro/libro_form.html', {'form':form})


def libro_delete(request, id_libro):
	libro = Libro.objects.get(codigo=id_libro)
	if request.method == 'POST':
		libro.delete()
		return redirect('libro_listar')
	return render(request, 'libro/libro_delete.html', {'libro':libro})