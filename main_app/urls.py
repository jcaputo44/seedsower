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
    path('seeds/<int:seed_id>/assoc_plot/<int:plot_id>/', views.assoc_plot, name='assoc_plot'),
    path('seeds/<int:seed_id>/unassoc_plot/<int:plot_id>/', views.unassoc_plot, name='unassoc_plot'),
    path('plots/', views.PlotList.as_view(), name='plots_index'),
    path('plots/<int:pk>/', views.PlotDetail.as_view(), name='plots_detail'),
    path('plots/create/', views.PlotCreate.as_view(), name='plots_create'),
    path('plots/<int:pk>/update/', views.PlotUpdate.as_view(), name='plots_update'),
    path('plots/<int:pk>/delete/', views.PlotDelete.as_view(), name='plots_delete'),
]

