from django.urls import path
from.views import arbustos,flores,index,maceteros,quienessomos,tierradehoja
from .views import RegisterAPI,LoginAPI
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path(' ', arbustos, name="arbustos"),
    path(' ', flores, name="flores"),
    path(' ', index, name="index"),
    path(' ', maceteros, name="maceteros"),
    path(' ', quienessomos, name="quienessomos"),
    path(' ', tierradehoja, name="tierradehoja"),
]

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]