from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
   
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'username'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'username'}))
    class Meta:
        model = models.Post
        fields = ('author','title','text')
       

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'username'}),
            'text': forms.Textarea(attrs={'class': 'username'}),
        }


class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'username'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'username'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username'}))
    
    class Meta:
        fields = ('username','email','password1','password2')
        model = models.User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username'}),
            'email': forms.TextInput(attrs={'class': 'username'}),
        }
       

   

       



