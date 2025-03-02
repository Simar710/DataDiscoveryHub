# datahub/urls.py

from django.urls import path
from .views import DatasetListView, DatasetCreateView, DatasetListAPI, trigger_error

urlpatterns = [
    path('', DatasetListView.as_view(), name='dataset-list'),
    path('add/', DatasetCreateView.as_view(), name='dataset-add'),
    path('api/datasets/', DatasetListAPI.as_view(), name='dataset-list-api'),
    path("sentry-test/", trigger_error, name="sentry-test"),
]
