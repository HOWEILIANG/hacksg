from django.contrib.auth.views import LogoutView
from django.urls import path

from dbschallenge.views import (
    call,
    dashboard,
    result,
    signup,
    user_input_view,
    user_login,
)

urlpatterns = [
    path('', user_input_view, name='user_input'),
    path('signup/',signup , name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('result/<int:pk>/', result, name='result'),
    path('dashboard/', dashboard, name='dashboard'),
    path('call/', call, name='call'),

]
