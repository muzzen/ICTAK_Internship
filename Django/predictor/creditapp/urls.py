from django.urls import path
# from .views import HomeView, PredictResultView
from . import views

# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('predict/', PredictResultView.as_view(), name='predict_result'),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_result, name='predict_result'),
]