from django.urls import path
from .views import AddPhoto, GalleryView, PhotoView, RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', GalleryView, name='gallery'),
    path('add-photo/', AddPhoto, name='add-photo'),
    path('view-photo/<str:pk>', PhotoView, name='view-photo'),

]
