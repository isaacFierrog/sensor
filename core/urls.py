from django.contrib import admin
from django.urls import path
from django.urls import include
from apps.usuario.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('api/', include('apps.modulo.routers'))
]
