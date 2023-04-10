
from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.index, name='index' ),
    path('forum/<str:category_slug>', views.category, name='category'),
    path('forum/nova_tema/<int:category_id>', views.new_topic, name='new_topic'),
    path('forum/<str:category_slug>/<str:topic_slug>', views.topic, name='topic'),
    path('forum/nova_poruka/<int:category_id>/<int:topic_id>', views.new_post, name='new_post'),
]