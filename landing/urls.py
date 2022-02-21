from django.urls import path

from .views import HomeView, LoginView, registerView, LogoutView,profileView

app_name = 'landing'
urlpatterns = [
    path('', HomeView.as_view(),name ='Home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', registerView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profileView.as_view(), name='profile'),
]
