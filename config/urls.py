from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewset, LivrosViewSet, AutorViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editora", EditoraViewset)
router.register(r"autor", AutorViewSet)
router.register(r"livros", LivrosViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
