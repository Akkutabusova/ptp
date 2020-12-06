from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm#, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordsChangeForm, ProfilePageForm
from django.views.generic import DetailView, CreateView 
from ablog.models import Profile

# Create your views here.

class CreateProfilePageView(CreateView):
	"""docstring for CreateProfilePageView"""
	model = Profile
	form_class = ProfilePageForm
	template_name = 'registration/create_profile_page.html'
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
	"""docstring for EditProfilePAgeView"""
	model = Profile
	template_name = 'registration/edit_profile_page.html'
	fields = ['bio', 'profile_pic', 'website_url', 'facebook_ur', 'twitter_url', 'linkedin_url', 'github_url']
	success_url = reverse_lazy('home')

	"""
	def __init__(self, arg):
		super EditProfilePAgeView, self).__init__()
		self.arg = arg
		"""

class ProfilePageView(DetailView):
	"""docstring fos ProfilePageView"""
	model = Profile
	template_name = 'registration/profile.html'

	def get_context_data(self, *args, **kwargs):
		#user = Profile.objects.all()
		context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
		page_user = get_object_or_404 (Profile, id=self.kwargs['pk'])
		context["page_user"] = page_user
		return context
		

class PasswordsChangeView(PasswordChangeView):
	#easy case
	#form_class = PasswordChangeForm
	#success_url = reverse_lazy('home')
	#custom case
	form_class = PasswordsChangeForm
	success_url = reverse_lazy('password_succes')

def password_succes(request):
	return render(request, 'registration/password_succes.html',{})

class UserCreationView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user