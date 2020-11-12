
from django.urls import path
from .views import UserCreationView, UserEditView

urlpatterns = [
  #  path('', views.home, name="home"),
  path('registration/', UserCreationView.as_view(), name="registration"),
  path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
  #path('login/', UserCreationView.as_view(), name="registration"),

 
]