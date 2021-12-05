from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('browse_jobs',views.browse_jobs,name="browse_jobs"),
    path(r'^ job_page/(?P<jid>\d+)/$', views.job_page, name='job_page'),
    path('apply',views.apply,name='apply')
]