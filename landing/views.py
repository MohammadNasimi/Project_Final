from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views import View


class HomeView(TemplateView):
    template_name = "landing/base/_base.html"


class LoginView(View):

    def get(self, request):
        return render(request, 'landing/public/Login.html')
