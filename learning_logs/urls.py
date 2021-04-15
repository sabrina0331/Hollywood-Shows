from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics',views.topics, name='topics'),
    path('topics/(?P<topic_id>\d+)', views.topic, name='topic'),
    path('new_topic', views.create_topic, name='new_topic'),
    path('new_entry/(?P<topic_id>\d+)',views.create_entry, name='new_entry'),
    path('edit_entry/(?P<entry_id>\d+)',views.update_entry, name='edit_entry'),
]

