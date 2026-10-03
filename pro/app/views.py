from django.shortcuts import render

# Create your views here.

# function based
from django.http import HttpResponse


# def Home(request):
#     if request.method == 'GET':
#         return HttpResponse("Welcome To Django")


# Define index view return message index page
# def Index(request):
#     if request.method == 'GET':
#         return HttpResponse("Index Page")

    # class based
from django.views import View
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome")

class Index(View):
    def get(self, request):
        return HttpResponse("Index page")