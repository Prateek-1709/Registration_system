from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signupPage,name='signup'),
    path('home',views.indexPage,name="home"),
    path('login',views.loginPage,name="login"),
    path('logout',views.logoutPage,name="logout")
]
