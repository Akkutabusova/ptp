
from django.urls import path
from .views import UserCreationView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
#from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
  #  path('', views.home, name="home"),
  path('registration/', UserCreationView.as_view(), name="registration"),
  path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
  #path('login/', UserCreationView.as_view(), name="registration"),
  #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
  path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
  path('password_succes', views.password_succes, name ="password_succes"),
  path('<int:pk>/profile/', ProfilePageView.as_view(), name = "profile_page"),
  path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name = "edit_profile_page"),
   path('create_profile/', CreateProfilePageView.as_view(), name = "create_profile_page"),
 ]