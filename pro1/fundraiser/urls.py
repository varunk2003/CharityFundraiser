from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="index1"),
    path('login/',views.login,name="login"),
    path('login/signup/',views.signup,name="signup"),
    path('login/signup/back/',views.back,name="back"),
    path('login/signup/createuser/',views.createuser,name="createuser"),
    path('login/signin/',views.signin,name="signin"),
    path('logout/',views.logout,name="logout")
    ]