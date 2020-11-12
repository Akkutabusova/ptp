from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choices_list = [item for item in choices]

class PostForm(forms.ModelForm):
	class Meta:
		"""docstring for Meta"""
		model = Post
		fields = ('title', 'author','category', 'body','desc')
		widgets = {
				'title': forms.TextInput(attrs={'class':'form-control'}),
				'author': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'usr', 'type':'hidden'}), 
				'image': forms.TextInput(attrs={'class':'form-control'}),
				'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
				'body': forms.Textarea(attrs={'class':'form-control'}),
				'desc': forms.Textarea(attrs={'class':'form-control'}),
			}
			
			
