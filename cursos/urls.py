from django.urls import path
from cursos import views

urlpatterns = [
    path('course/', views.CourseListCreateAPIView.as_view(), name='courses'),
    path('rating/', views.RatingListCreateAPIView.as_view(), name='ratings'),
    path('course/<int:pk>', views.CourseRetrieveUpdateDestroyAPIView.as_view(), name='course'),
    path('rating/<int:pk>', views.RatingRetrieveUpdateDestroyAPIView.as_view(), name='rating'),
]
