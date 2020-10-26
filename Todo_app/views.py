from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . forms import todo_form
from . models import todo

# Create your views here.
class todo_list(ListView):
    model = todo
    context_object_name = 'todo_list'

class todo_detail(DetailView):
    model = todo
    context_object_name = 'todo_detail'
    
class todo_create(CreateView):
    form_class = todo_form
    template_name = 'Todo_app/todo_create.html'
    success_url = '/'
    
class todo_update(UpdateView):
    form_class = todo_form
    queryset = todo.objects.all()
    template_name = 'Todo_app/todo_update.html'
    success_url = '/'

class todo_delete(DeleteView):
    model = todo
    success_url = '/'