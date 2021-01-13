from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from bank.views import BranchAutocompleteView, BranchSearchView


schema_view = get_schema_view(
    openapi.Info(
        title="",
        default_version='v1',
        description="Swagger API UI for",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/branches/autocomplete', BranchAutocompleteView),
    path('api/branches', BranchSearchView),
]

# adding routes to user uploaded files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
