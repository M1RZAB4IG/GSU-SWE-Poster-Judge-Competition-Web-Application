"""
URL configuration for go project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from. import index





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.webpage1, name='webpage1' ),
    path('page2',index.webpage2, name='webpage2' ),
    path('page3',index.webpage3, name='webpage3' ),
    path('page4',index.webpage4, name='webpage4' ),
    path('page5',index.webpage5, name='webpage5' ),
    path('page6',index.webpage6, name='webpage6' ),
    path('page7',index.webpage7, name='webpage7' ),
    path('page8',index.webpage8, name='webpage8' ),
    path('page9',index.webpage9, name='webpage9' ),

    
    
    

    



   
]

