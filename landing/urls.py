from django.urls import path

from .views import HomeView, LoginView

app_name = 'landing'
urlpatterns = [
    path('', HomeView.as_view()),
    path('login/', LoginView.as_view(), name='login'),

]
