from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewset, LivrosViewSet, AutorViewSet

router = DefaultRouter()
router.register(r"autor", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"editora", EditoraViewset)
router.register(r"livros", LivrosViewSet)


urlpatterns = [
    path("api/media/", include(uploader_router.urls)),
    path("api/", include(usuario_router.urls)),
    path("token/",TokenObtainPairView.as_view(), name="ttoken_obtain_pair" ),
    path("token/refresh/",TokenRefreshView.as_view(), name="ttoken_refresh" ),
    path("admin/", admin.site.urls),
     path("", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)

