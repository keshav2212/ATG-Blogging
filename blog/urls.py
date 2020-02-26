from django.urls import path,include
from blog import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.home),
    path('register/',views.register),
    path('login/',LoginView.as_view(template_name='login.html')),
    path('logout/',LogoutView.as_view(template_name='logout.html')),
    path('dashboard/',views.dashboard),
    path('newarticle/',views.newarticle),
    path('delete/<int:id>',views.deletearticle,name="deletearticle"),
    url(r'^captcha/', include('captcha.urls')),
    path('otherarticle/<str:search>',views.otherarticle),
]
