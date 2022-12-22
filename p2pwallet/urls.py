from django.contrib import admin
from django.urls import path,include, re_path as path

from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView


schema_view = get_schema_view(
    openapi.Info(
        title="Fintech API",
        default_version='v1',
        description="Fintech API",
        terms_of_service="http://127.0.0.1:8000",
        contact=openapi.Contact(email="webmaster@mail.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True, # to display all the api link
    # public=False, # all api will not be displayed except authentication
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('index', TemplateView.as_view(template_name="index.html"), name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
		name='schema-swagger-ui'),  #<-- Here
	path(r'^doc(?P<format>\.json|\.yaml)$',
		schema_view.without_ui(cache_timeout=0), name='schema-json'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
