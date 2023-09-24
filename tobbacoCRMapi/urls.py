from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views.bales import BalesDetail, BalesList
from .views.bales_quality import BalesQaulityList, BalesQualityDetail
from .views.contact import ContactsDetail, ContactsList
from .views.contract import ContractsDetail, ContractsList
from .views.season import SeasonsList
from .views.season_names import SeasonNamesDetail, SeasonsNamesList
from .views.season_workflows import SeasonWorkflowList, SeasonWorkflowsDetail

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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    path('seasons', SeasonsList.as_view(), name='create-seasons'),
    path('seasons/<uuid:pk>/',
         SeasonNamesDetail.as_view(), name='operations-With-Id'),

    path('seasons/names', SeasonsNamesList.as_view(), name='create-seasons'),
    path('seasons/names/<uuid:pk>/',
         SeasonNamesDetail.as_view(), name='operations-With-Id'),

    path('seasons/workflows', SeasonWorkflowList.as_view(),
         name='create-seasons'),
    path('seasons/workflows/<uuid:pk>/',
         SeasonWorkflowsDetail.as_view(), name='operations-With-Id'),

    path('contacts', ContactsList.as_view(), name='create-contacts'),
    path('contacts/<uuid:pk>/',
         ContactsDetail.as_view(), name='contacts-With-Id'),

    path('contracts', ContractsList.as_view(), name='create-contracts'),
    path('contracts/<uuid:pk>/',
         ContractsDetail.as_view(), name='contracts-With-Id'),

    path('bales', BalesList.as_view(), name='create-contracts'),
    path('bales/<uuid:pk>/',
         BalesDetail.as_view(), name='contracts-With-Id'),

    path('bales/qaulity', BalesQaulityList.as_view(), name='create-contracts'),
    path('bales/qaulity/<uuid:pk>/',
         BalesQualityDetail.as_view(), name='contracts-With-Id'),
]
