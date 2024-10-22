from django.urls import path
from .views import homepage,register,loginuser
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',homepage,name='home'),
    path('signup/',register,name='signup'),
    path('login/',loginuser,name='login'),
    path('logout',LogoutView.as_view(next_page='home'),name='logout')
]