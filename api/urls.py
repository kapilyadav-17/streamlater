from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path('video/', views.getVideos),
    path('downloadvideo/',views.downloadvideo),
    path('video/create/',views.creteVideo),
    path('video/<str:pk>/', views.getVideo)

]