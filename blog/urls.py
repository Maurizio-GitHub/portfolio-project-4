from . import views
from django.urls import path

# When using class-based views, we need to add the 'as_view' method at the end
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]
