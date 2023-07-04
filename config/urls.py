from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewset, LivrosViewSet, AutorViewSet

router = DefaultRouter()
router.register(r"autor", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"editora", EditoraViewset)
router.register(r"livros", LivrosViewSet)

urlpatterns = [
    path("api/", include(usuario_router.urls)),
    path("token/",TokenObtainPairView.as_view(), name="ttoken_obtain_pair" ),
    path("token/refresh/",TokenRefreshView.as_view(), name="ttoken_refresh" ),
    path("admin/", admin.site.urls),
     path("", include(router.urls)),
]

