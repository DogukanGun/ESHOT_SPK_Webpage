from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from search_engine.views import search_engine
app_name="authentication"
urlpatterns = [  
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},name="logout"), 
]
