from django.conf.urls import url
from apis import views

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url(r'^risks/$',
        views.RiskListCreateAPI.as_view(),
        name='risks'),
    url(r'^risktypes/$',
        views.RiskTypeListCreateAPI.as_view(),
        name='risk_types'),
    url(r'^riskfields/$',
        views.RiskFieldListCreateAPI.as_view(),
        name='risk_fields'),
    url(r'^risktypes/(?P<pk>[0-9]+)/$',
        views.RiskTypeRetrieveUpdateDestroyAPI.as_view(),
        name='risk_type'),
    url(r'^riskfields/(?P<pk>[0-9]+)/$',
        views.RiskFieldsRetrieveUpdateDestroyAPI.as_view(),
        name='risk_field'),
    url(r'^risks/(?P<pk>[0-9]+)/$',
        views.RiskRetrieveUpdateDestroyAPI.as_view(),
        name='risk'),
]
