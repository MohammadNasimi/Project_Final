from django.contrib.auth.models import Permission, ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.views.generic import TemplateView
from django.views import View

from core.models import User
from customer.forms import CustomerForm
from customer.models import Customer


class HomeView(TemplateView):
    template_name = "landing/public/Home.html"


class registerView(View):
    # form_class = CustomerForm
    # template_name = 'public/register'

    def get(self, request):
        form = CustomerForm()
        return render(request, 'landing/public/register.html', {'form': form})

    def post(self, request):
        phone = request.POST['phone']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        for i in User.objects.all():
            if i.phone == phone:
                messages.add_message(request, messages.ERROR, "phone is exist")
                return render(request, 'landing/public/register.html', {'form': self.form_class})
        if password2 != password1:
            messages.add_message(request, messages.ERROR, "your password not equal")
            return render(request, 'landing/public/register.html', {'form': self.form_class})
        if len(password1) < 8:
            messages.add_message(request, messages.ERROR, "your password should more than 8")
            return render(request, 'landing/public/register.html', {'form': self.form_class})
        new_user = User.objects.create_user(username=phone, email=email,
                                            first_name=first_name, last_name=last_name, password=password1, phone=phone)
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


class LoginView(View):
    def get(self, request):
        # if request.session.get('uid', None) is None:
        return render(request, 'landing/public/Login.html')

    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']

        user = User.objects.get(phone=phone)
        if not user.check_password(password):
            messages.add_message(request, messages.ERROR, "your password wrong")
            return render(request, 'landing/public/Login.html')
        request.session['uid'] = user.id
        from product.Cart import Cart
        from order.order_item_add import Order_User
        cart = Cart(request)
        user = Order_User(user)
        user.add_session(cart)
        len_order_user = user.get_user()
        cart.clear()
        # set cookie
        user = {
            'user': user,
        }
        response = render(request, 'landing/public/Home.html', context=user)
        response.set_cookie('count', len_order_user[3])

        return response


class LogoutView(View):

    def get(self, request):
        if request.session.get('uid', None) is None:
            return render(request, 'landing/public/Home.html')
        del request.session['uid']
        return render(request, 'landing/public/Home.html')


class profileView(View):
    # permission_required = "landing.see_profile"

    def get(self, request):
        user = User.objects.get(id=request.session.get('uid', None))
        user = {
            'user': user

        }

        return render(request, 'landing/public/profile.html', context=user)
