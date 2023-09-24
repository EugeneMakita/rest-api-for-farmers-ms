from django.urls import path, re_path
from .views.season_names import SeasonNamesDetail, SeasonsNamesList
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Big Tobbaco API",
        default_version='v1',
        description="This is the api spec for Big Tobbaco Endpoint",
        terms_of_service="https://www.bigtobbaco.com/terms/",
        contact=openapi.Contact(email="bigtobbaco@company.net"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('seasons/names', SeasonsNamesList.as_view(), name='create-seasons'),
    path('seasons/names/<uuid:pk>/', SeasonNamesDetail.as_view(), name='operations-With-Id'), 
]
