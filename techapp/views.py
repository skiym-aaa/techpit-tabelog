from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView

class IndexView(TemplateView):
  template_name = 'techapp/index.html'
