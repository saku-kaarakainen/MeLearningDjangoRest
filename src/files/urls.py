from django.urls import path
from . import views

# TODO: This could be helpful
# https://github.com/ukjin1192/django-rest-framework-example/blob/master/mysite/apps/main/urls.py
urlpatterns = [

  # GET files?organizationId={org_id}
  # GET files?userId={user_id}
  path('', views.file_list),
  path('/', views.file_list),

  # GET files/{file_id}
  path('/<int:pk>', views.file_download),
  path('/<int:pk>/', views.file_download),

  # POST files/upload 
  path('/upload', views.file_upload),
  path('/upload/', views.file_upload),
]