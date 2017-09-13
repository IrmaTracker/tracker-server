from django.conf.urls import url, include
from tracker import views


app_name = "tracker"
urlpatterns = [
    url(r'^$', views.AreaListView.as_view(), name='area_list'),
    url(r'^areas/$', views.AreaListView.as_view(), name='area_list'),
    url(r'^areas/(?P<slug>[\w-]+)/', include([
        url(r'^$', views.AreaDetailView.as_view(), name='area_detail'),
        url(r'^persons/$', views.PersonListView.as_view(), name='person_list'),
        url(r'^persons/safe/$', views.PersonMarkedSafeListView.as_view(), name='safe_person_list'),
        url(r'^persons/missing/$', views.PersonMissingListView.as_view(), name='missing_person_list'),
        url(r'^persons/(?P<pk>\d+)/$', views.UpdatePersonView.as_view(), name='update_person'),
        url(r'^persons/add/$', views.CreatePersonView.as_view(), name='create_person'),
        url(r'^supplies/$', views.SubmitSupplyShareRequestView.as_view(), name='submit_supplies'),
        url(r'^supplies/request/$', views.SubmitSupplyRequestView.as_view(), name='request_supplies'),
        url(r'^emergencies/$', views.SubmitEmergencyRequestView.as_view(), name='submit_emergency'),
    ]))
]