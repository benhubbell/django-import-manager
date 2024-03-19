from django.urls import path

from presto import views
from presto.api.views import log_test


urlpatterns = [
    path('', views.index, name='presto_index'),
    path('old', views.index_old, name='index_old'),
    path('start-download', views.start_download, name='start_download'),
    path('log-test', log_test, name='log_test'),
]
