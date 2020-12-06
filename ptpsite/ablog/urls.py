from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, EditView, UpdatePostView, DeletePostView, CategoryView,LikeView

urlpatterns = [
  #  path('', views.home, name="home"),
  path('', HomeView.as_view(), name = "home"),
  path('article/<int:pk>', ArticleDetailView.as_view(), name = 'post-detail'),
  path('add_post/', EditView.as_view(), name = 'add-post'),
  path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update-post'),
  path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete-post'),
  path('category/<str:cats>/', CategoryView, name = 'category'),
  path('like/<int:pk>', LikeView, name="like_post"),
]