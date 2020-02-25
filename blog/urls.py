from django.urls import path
from blog import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.home),
    path('register/',views.register),
    path('login/',LoginView.as_view(template_name='login.html')),
    path('logout/',LogoutView.as_view(template_name='logout.html')),
    path('dashboard/',views.dashboard),
    path('newarticle/',views.newarticle),
    path('newarticledone',views.newarticledone)
]
