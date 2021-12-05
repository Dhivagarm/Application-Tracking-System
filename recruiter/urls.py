from django.urls import path


from . import views

urlpatterns = [
    path('add_job',views.add_job,name='add_job'),
    path('manage_applications',views.manage_applications,name='manage_applications')
]

