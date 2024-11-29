from django.urls import path
from .views import register
from django.contrib.auth.views import LogoutView,LoginView,PasswordChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/',register,name='signup'),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    # path('login/',loginuser,name='login'),
    path('login/',LoginView.as_view(template_name = 'accounts/login.html', next_page='home'),name='login'),
    path('logout',LogoutView.as_view(next_page='home'),name='logout'),
    # path('register/',signup,name='signup')
]