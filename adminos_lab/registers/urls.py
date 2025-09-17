from django.urls import path
from . import views

app_name = 'registers'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('health/', views.health_check, name='health_check'),
    path('registers/', views.register_list, name='register_list'),
    path('registers/<int:register_id>/<int:year>-<int:month>-<int:day>/', views.register_date_detail, name='register_date_detail'),
    path('bundles/daily/', views.daily_bundle, name='daily_bundle'),
    path('bundles/weekly/', views.weekly_bundle, name='weekly_bundle'),
    path('bundles/pending/', views.pending_due_bundle, name='pending_due_bundle'),
]
