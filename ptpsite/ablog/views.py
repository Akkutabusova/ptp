from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	#ordering = ['-id']
	ordering = ['-date_post']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class EditView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'edit.html'
	#fields = '__all__'
	#fields= ('title','body') 
	#можно выбирать какие поля могут заполнять юзеры

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'update.html'
	fields= ['title','body','desc']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = reverse_lazy('home')



	