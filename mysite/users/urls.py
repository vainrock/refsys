from django.urls import path
from . import views

urlpatterns = [
    path('send-auth-code/', views.send_auth_code, name='send_auth_code'),
    path('verify-auth-code/', views.verify_auth_code, name='verify_auth_code'),
    path('set-invite-code/', views.set_invite_code, name='set_invite_code'),
    path('get-user-profile/<str:phone_number>/', views.get_user_profile, name='get_user_profile'),
]
