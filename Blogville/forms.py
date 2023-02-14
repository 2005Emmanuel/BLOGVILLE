from .models import Profile, Blogpost
from django import forms
class Profileform(forms.ModelForm):
    class Meta:
     model = Profile
     fields = ('user', 'image', 'bio', 'facebook', 'instagram', 'Twitter')
     
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ('title', 'slug', 'content', 'image')
        widget = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of your Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of Your Blog'}),
            
        }