from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('aboutus/', views.aboutus),
    path('myprofile/', views.myprofile),
    path('contactus/', views.contactus),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('process/', views.process),
    path('logout/', views.logout),
    path('mybooking/', views.mybooking),

]
