from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.personal_of_day,name=personalToday),
]