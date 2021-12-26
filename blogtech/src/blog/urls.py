from django.urls import path
from .views import BlogPostHomeView, BlogPostDetailsView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = "posts"

urlpatterns = [
    path('', BlogPostHomeView.as_view(), name="home"),
    path('create/', BlogPostCreateView.as_view(), name="create-post"),
    path('delete/<str:slug>/', BlogPostDeleteView.as_view(), name="delete-post"),
    path('update/<str:slug>/', BlogPostUpdateView.as_view(), name="update-post"),
    path('<str:slug>/', BlogPostDetailsView.as_view(), name="post-detail"),

]
