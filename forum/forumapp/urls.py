
from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.index, name='index' ),
    path('forum/<str:slug>', views.category, name='category'),
    path('forum/nova_tema/<int:category_id>', views.new_topic, name='new_topic'),

]