from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def message(request, message):
  return HttpResponse(f"<h1>{message}</h1>")