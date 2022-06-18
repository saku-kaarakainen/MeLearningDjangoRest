from django.urls import path
from . import views

# TODO: This could be helpful
# https://github.com/ukjin1192/django-rest-framework-example/blob/master/mysite/apps/main/urls.py
urlpatterns = [

  # GET files?organizationId={org_id}
  # GET files?userId={user_id}
  path('', views.FileList.as_view(), name='get_files_list'),

  # GET files/{file_id}
  path('<int:pk>/', views.FileDownload.as_view(), name='download_file'),

  # POST files/upload 
  path('upload/', views.FileUpload.as_view(), name='upload_file'),
]