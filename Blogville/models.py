from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Profile(models.Model): #User profile model(Table)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True )
    image = models.ImageField(upload_to='profile_pictures', default='media\profile_pictures\kindpng_4212275.png', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    Twitter = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return str (self.user) #Returning the string representation of the object attribute user
    
    
class Blogpost(models.Model): #Blogpost model(Table)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #column author has a relationship with a column in the User table
    slug = models.CharField(max_length=130)
    content = models.TextField()
    image = models.ImageField(upload_to='profile_pictures', blank=True, null=True,)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    def __str__(self):
        return str (self.author) + " Blog Title: " + self.title #Returning the string representation of the object attribute author + Blog Title string and title
    
    def number_of_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse('blogs')
    


class Comment(models.Model): #Comment model(Table)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    datetime = models.DateTimeField(default=now)
    def number_of_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.user.username + " comment: " + self.content #Returning the string representation of the object attribute user and the user's username + comment string and cntent
       
    
class Follower_Following(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_on = models.DateTimeField(auto_now_add=True)
    



# class Like(models.Model):
#     blog = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
# class BlogPost(models.Model):
#     likes = models.ManyToManyField(User, related_name='blogpost_like')

#     def number_of_likes(self):
#         return self.likes.count()