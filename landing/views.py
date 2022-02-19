from django.contrib.auth.models import Permission, ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import TemplateView
from django.views import View

from core.models import User
from customer.forms import CustomerForm
from customer.models import Customer


class HomeView(TemplateView):
    template_name = "landing/public/Home.html"


class registerView(View):
    form_class = CustomerForm
    template_name = 'landing/register'

    def get(self, request):
        return render(request, 'landing/public/register.html', {'form': self.form_class})

    def post(self, request):
        phone = request.POST['phone']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        new_user = User.objects.create_user(username=phone, email=email,
                                            first_name=first_name, last_name=last_name, password=password, phone=phone)
        Customer.objects.create(user=new_user)
        # code add permission see-profile in terminal
        # content_type = ContentType.objects.get_for_model(User)
        # permission = Permission.objects.create(
        #     name='can see profile',
        #     codename='see_profile',
        #     content_type=content_type
        # )
        # add permission when register
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(content_type=content_type, codename='see_profile')
        new_user.user_permissions.add(permission)
        return render(request, 'landing/public/Login.html')


class LoginView(PermissionRequiredMixin, View):
    permission_required = "auth.see_profile"

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
