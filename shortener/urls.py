from django.urls import path

from shortener import views


urlpatterns = [
    path('urls/', views.UrlListAPIView.as_view()),
    path('create/', views.UrlCreateAPIView.as_view()),
    path('<slug:slug>/', views.UrlRetrieveDestroyAPIView.as_view()),
    path('update/<slug:slug>/', views.UrlUpdateAPIView.as_view())
]
