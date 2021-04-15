from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    path('',views.allshows, name='allshows'),
    path('new_page',views.new_page, name='new_page'),
    path('show_detail/(?P<show_id>\+d)',views.show_detail, name='show_detail'),
    path('edit_show/(?P<show_id>\+d)',views.update_show, name='edit_show'),
    path('delete_show/(?P<delete_id>\+d)',views.delete_show, name='delete_show'),
    path('search_show',views.search_show, name='search_show')
]