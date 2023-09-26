from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views.bales import BalesDetail, BalesList
from .views.bales_quality import BalesQaulityList, BalesQualityDetail
from .views.comment import CommentsDetail, CommentsList
from .views.contact import ContactsDetail, ContactsList
from .views.contract import ContractsDetail, ContractsList
from .views.contract_status import ContactsStatusList, ContractsStatusDetail
from .views.farmer import FarmerDetail, FarmerList
from .views.farmer_status import FarmerStatusDetail, FarmerStatusList
from .views.files import FilesDetailView, FilesList
from .views.images import ImageDetailView, ImagesList
from .views.land_type import LandTypeDetail, LandTypeList
from .views.season import SeasonsDetail, SeasonsList
from .views.season_names import SeasonNamesDetail, SeasonsNamesList
from .views.season_workflows import SeasonWorkflowList, SeasonWorkflowsDetail
from .views.supplies import SuppliesDetail, SuppliesList
from .views.supplies_type import SuppliesTypeDetail, SuppliesTypeList

schema_view = get_schema_view(
    openapi.Info(
        title="Big Tobbaco API",
        default_version="v1",
        description="This is the api spec for Big Tobbaco Endpoint",
        terms_of_service="https://www.bigtobbaco.com/terms/",
        contact=openapi.Contact(email="bigtobbaco@company.net"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("seasons", SeasonsList.as_view(), name="season-create-index"),
    path("seasons/<uuid:pk>/", SeasonsDetail.as_view(),
         name="season-get-patch-delete"),
    path("seasons/names", SeasonsNamesList.as_view(),
         name="season-names-create-index"),
    path(
        "seasons/names/<uuid:pk>/",
        SeasonNamesDetail.as_view(),
        name="season-names-get-patch-delete",
    ),
    path(
        "seasons/workflows",
        SeasonWorkflowList.as_view(),
        name="season-workflows-create-index",
    ),
    path(
        "seasons/workflows/<uuid:pk>/",
        SeasonWorkflowsDetail.as_view(),
        name="season-workflows-get-patch-delete",
    ),
    path("contacts", ContactsList.as_view(), name="contacts-create-index"),
    path(
        "contacts/<uuid:pk>/",
        ContactsDetail.as_view(),
        name="contacts-get-patch-delete",
    ),
    path("contracts", ContractsList.as_view(), name="contracts-create-index"),
    path(
        "contracts/<uuid:pk>/",
        ContractsDetail.as_view(),
        name="contracts-get-patch-delete",
    ),
    path(
        "contracts/status",
        ContactsStatusList.as_view(),
        name="contract-statuses-create-index",
    ),
    path(
        "contracts/status/<uuid:pk>/",
        ContractsStatusDetail.as_view(),
        name="contract-statuses-get-patch-delete",
    ),
    path("bales", BalesList.as_view(), name="bales-create-index"),
    path("bales/<uuid:pk>/", BalesDetail.as_view(),
         name="bales-get-patch-delete"),
    path(
        "bales/qaulity", BalesQaulityList.as_view(), name="bale-qualities-create-index"
    ),
    path(
        "bales/qaulity/<uuid:pk>/",
        BalesQualityDetail.as_view(),
        name="bale-qualities-get-patch-delete",
    ),
    path("comment", CommentsList.as_view(), name="comments-create-index"),
    path(
        "comment/<uuid:pk>/", CommentsDetail.as_view(), name="comments-get-patch-delete"
    ),
    path("farmers", FarmerList.as_view(), name="farmers-create-index"),
    path("farmers/<uuid:pk>/", FarmerDetail.as_view(),
         name="farmers-get-patch-delete"),
    path(
        "farmers/status",
        FarmerStatusList.as_view(),
        name="farmer-statuses-create-index",
    ),
    path(
        "farmers/status/<uuid:pk>/",
        FarmerStatusDetail.as_view(),
        name="farmer-statuses-get-patch-delete",
    ),
    path("land-type", LandTypeList.as_view(), name="land-types-create-index"),
    path(
        "land-type/<uuid:pk>/",
        LandTypeDetail.as_view(),
        name="land-types-get-patch-delete",
    ),
    path("supplies", SuppliesList.as_view(), name="supplies-create-index"),
    path(
        "supplies/<uuid:pk>/",
        SuppliesDetail.as_view(),
        name="supplies-get-patch-delete",
    ),
    path("supplies/type", SuppliesTypeList.as_view(),
         name="supply-types-create-index"),
    path(
        "supplies/type/<uuid:pk>/",
        SuppliesTypeDetail.as_view(),
        name="supply-types-get-patch-delete",
    ),
    path("images", ImagesList.as_view(), name="images-create-index"),
    path("images/<uuid:pk>/", ImageDetailView.as_view(), name="images-get-delete"),
    path("files", FilesList.as_view(), name="files-create-index"),
    path("files/<uuid:pk>/", FilesDetailView.as_view(), name="files-get-delete"),
]
