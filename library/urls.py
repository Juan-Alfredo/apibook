"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include
from catalogo.views import Author_list
from catalogo.views import AuthorCreate
from catalogo.views import BookCreate
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from catalogo import views
from catalogo import viewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('books', viewsets.BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^catalog[\/]?$', views.catalog_list),
    #path('catalog/books', views.new_book),
    # /catalog.html
    # /catalog.json 

    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    #path('books', views.BookCreate.as_view()),
    #path('book/<pk>/', views.BookUpdate.as_view()),
    path('authors', views.AuthorCreate.as_view()),
    path('authors/list', views.Author_list.as_view()),
    


    path('catalog/books', views.new_book),
    path('catalog/book/<pk>/update', views.update_book),

    #/catalog/planeta/books?year=2020   "2020"
    #/catalog/planeta/books?year=       ""
    #/catalog/planeta/books             None

    #re_path(r'catalog\/(?P<editorial>[a-zA-Z]+)\/books', views.get_books_by_editorial)

    path('catalog/<editorial>/books', views.get_books_by_editorial)
    
]
