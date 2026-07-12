from django.urls import path
from dogs.views import index, breeds_list, breeds_dogs_list, dogs_list_view
from dogs.apps import DogsConfig


app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    # breeds
    path('breeds/', breeds_list, name='breeds'),
    path('breeds/<int:pk>/dogs', breeds_dogs_list, name='breeds_dogs'),

    #dogs
    path('dogs/', dogs_list_view, name='dogs_list')
]
