"""pastebin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from paste.views import crear
from paste.views import mostrar
#cuenta
from usuario.views import registro, logout, logoutt, listar

#paste.views.Reporte()

#import django
#djang.conf.urls.url()




urlpatterns = [
    url(r'^list',listar,name="contenido"),
    url(r'^q',logoutt),
    url(r'^log',logout,name="loguin"),
    url(r'^acct$',registro,name="registro"),
    #url(r'^register/$',registro),
    url(r'^([0-9a-f]{5})$',mostrar,name="must"),
    url(r'^$',crear,name="create"),
    url(r'^admin/', admin.site.urls),
]
