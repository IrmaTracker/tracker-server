from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from api.v1 import views

schema_view = get_schema_view(
    title="Irma Tracker Schema"
)

router = DefaultRouter(trailing_slash=False)
router.register(r'areas', views.AreaViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'announcements', views.AnnouncementViewSet)
router.register(r'supply', views.SupplyViewSet)
router.register(r'supply-shares', views.SupplySharingViewSet)
router.register(r'supply-requests', views.SupplyRequestViewSet)
router.register(r'emergency-requests', views.EmergencyRequestViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'helpline', views.HelpLineViewSet)
router.register(r'emergencies', views.EmergencyViewSet)
router.register(r'needs', views.NeedViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema$', schema_view)
]