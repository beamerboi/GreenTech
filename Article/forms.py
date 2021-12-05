from django import forms

from Article.models import PetPost


class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = PetPost
		fields = ['title', 'body', 'image']


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = PetPost
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		pet_post = self.instance
		pet_post.title = self.cleaned_data['title']
		pet_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			pet_post.image = self.cleaned_data['image']

		if commit:
			pet_post.save()
		return pet_post
