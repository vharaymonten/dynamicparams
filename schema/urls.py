from unicodedata import name
from django.urls import path

from . import views
from  . import api 
app_name = "schema"
urlpatterns = [
    path('', views.schema_creator, name="schema_creator"),
    path('schema-test/', api.IOTDeviceCheckInAPI.as_view(), name="api"),
    path('preview/<uuid:pk>/', views.iot_device_preview, name="preview"),
    path('preview-schema/<uuid:pk>/', views.preview_schema, name="preview_schema"),
]