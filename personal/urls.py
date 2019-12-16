from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$', views.personal_of_day, name = 'personalToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_personal,name = 'pastPersonal'),
    url(r'^search/', views.search_results, name='search_results') 
]