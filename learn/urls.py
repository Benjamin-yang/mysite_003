from django.conf.urls import url

from learn import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^add/$', views.add,name='add'),
    url(r'^add/(\d+)/(\d+)/$', views.old_up),  # 让旧的（/add/4/4/）变新的(new_add/4/4)
    url(r'^new_add/(\d+)/(\d+)/', views.add2, name='add2'),
]