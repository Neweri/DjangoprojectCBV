from django.urls import path
from dogs.views import index, BreedListView, DogBreedListView, DogListView, DogCreateView, DogDetailView, DogUpdateView, \
    DogDeleteView, DogDeactivatedListView, dog_toggle_activity, DogSearchListView, BreedSearchListView
from dogs.apps import DogsConfig


app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    # breeds
    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('breeds/<int:pk>/dogs', DogBreedListView.as_view(), name='breeds_dogs'),
    path('breeds/search/', BreedSearchListView.as_view(), name='breeds_search'),

    #dogs
    path('dogs/', DogListView.as_view(), name='dogs_list'),
    path('dogs/deactivated', DogDeactivatedListView.as_view(), name='dogs_list_deactivated'),
    path('dogs/search/', DogSearchListView.as_view(), name='dogs_search'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/detail/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/toggle/<int:pk>/', dog_toggle_activity, name='dog_toggle'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]
