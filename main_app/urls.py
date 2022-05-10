from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('seeds/', views.seeds_index, name='index'),
    path('seeds/<int:seed_id>/', views.seeds_detail, name='detail'),
    path('seeds/create/', views.SeedCreate.as_view(), name='seeds_create'),
    path('seeds/<int:pk>/update/', views.SeedUpdate.as_view(), name='seeds_update'),
    path('seeds/<int:pk>/delete/', views.SeedDelete.as_view(), name='seeds_delete'),
    path('seeds/<int:seed_id>/add_watering/', views.add_watering, name='add_watering'),
]

