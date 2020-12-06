from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request):
#	return render(request, 'home.html', {})

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False

	else:
		post.likes.add(request.user)
		liked == True

	return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

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

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		stuff= get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

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



	