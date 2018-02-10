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
]
