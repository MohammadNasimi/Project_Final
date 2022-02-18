from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import TemplateView
from django.views import View

from core.models import User


class HomeView(TemplateView):
    template_name = "landing/base/_base.html"


class LoginView(View):

    def get(self, request):
        return render(request, 'landing/public/Login.html')

    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
        user = User.objects.get(phone=phone)
        if not user.check_password(password):
            return HttpResponse('pass not correct', status=400)
        request.session['uid'] = user.id
        user = {
            'user': user,
        }
        return render(request, 'landing/base/_base.html', context=user)
