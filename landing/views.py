from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import TemplateView
from django.views import View

from core.models import User
from customer.forms import CustomerForm


class HomeView(TemplateView):
    template_name = "landing/public/Home.html"


class registerView(View):
    form_class = CustomerForm
    template_name = 'landing/register'

    def get(self, request):
        return render(request, 'landing/public/register.html', {'form': self.form_class})

    def post(self, request):
        ...


class LoginView(View):

    def get(self, request):
        if request.session.get('uid', None) is None:
            return render(request, 'landing/public/Login.html')
        user = User.objects.get(id=request.session.get('uid', None))
        user = {
            'user': user

        }
        return render(request, 'landing/public/profile.html', context=user)

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
        return render(request, 'landing/public/Home.html', context=user)


class LogoutView(View):

    def get(self, request):
        if request.session.get('uid', None) is None:
            return render(request, 'landing/public/Home.html')
        del request.session['uid']
        return render(request, 'landing/public/Home.html')
