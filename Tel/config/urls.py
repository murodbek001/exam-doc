from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import *
from dj_rest_auth.registration import urls
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as drf_schema_view
from drf_yasg import openapi

schema_view = drf_schema_view(
    openapi.Info(
        title="Mobile API",
        description="API description here",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="umid656bek@gmail.com"),
    ),
    public=True,
    permission_classes=(AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('api/v1/register/', RegisterAPIView.as_view(), name="register"),
    path('api/v1/login/', LoginAPIView.as_view(), name="login"),
    path('api/v1/logout/', LogoutAPIView.as_view(), name="logout"),
    path('schema/', get_schema_view(title="Mobile API", description="API description here", version='1.0.0'), name="openapi-schema"),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-docs"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-docs"),
    path('api/v1/', include('api.urls')),
    path('', include("main.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)