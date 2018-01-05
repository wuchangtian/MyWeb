from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from .models import Comment
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date','avatar',)
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body','category',)

class worksForm(forms.ModelForm):
    class Meta:
        model=works
        fields=('titles','intorduce','tags','work',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
