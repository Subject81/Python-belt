from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('user',views.index),
    path('new',views.new),
    path('create',views.create),
    path('welcome',views.welcome),
    path('registration',views.registration),
    path('login', views.login),
    path('logout', views.logout),
    path('job/joblist', views.indexs),
    path('job', views.indexs),
    path('job/new',views.news),
    path('job/create',views.creates),
    path('job/<int:num>/view',views.information),
    path('job/show/<int:num>',views.show),
    path('job/<int:num>/edit', views.edit),
    path('job/<int:num>/update', views.update),
    path('job/<int:num>/destroy', views.destroy),
    path('job/<int:num>add', views.add),
]