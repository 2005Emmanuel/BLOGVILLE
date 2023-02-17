from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Blogpost, Comment, Follower_Following
from .forms import Profileform, BlogPostForm
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @csrf_exempt
def Register(request): #User Registration views
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('Register')
 
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'Authentication/Login.html')  
    return render(request, "Authentication/Register.html")

# @csrf_exempt
def Login(request):  #User Authentication Logic
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Succesfully logged in as {username}')
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, 'Authentication/Authentication_error.html') 
    return render(request, 'Authentication/Login.html' )

def Logout(request):
    logout(request)
    return redirect(blogs)


#User profile Details Logic
def profile(request):
    return render(request, 'profiles/Profile.html')

def user_profile(request, myid):
    post = Blogpost.objects.filter(id=myid)
    return render(request, 'profiles/user_profile.html', {'post' : post})

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method=="POST":
        form = Profileform(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "profiles/edit_profile.html", {'alert':alert})
    else:
        form=Profileform(instance=profile)
    return render(request, "profiles/edit_profile.html", {'form':form})



  
            

#Blogs Logic     
@login_required(login_url='/login')
def add_Blog(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, 'Home_page/index.html', {'obj' : obj, 'alert' : alert})
    else:
            form = BlogPostForm()
            return render(request, 'blog/add_blog.html', {'form' : form})

def blogs(request):
    posts = Blogpost.objects.all()
    posts = Blogpost.objects.filter().order_by('-datetime')  
    return render(request, 'Home_page/index.html', {'posts': posts})


def blog_comments(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        blog_id = request.POST.get('blog_id', '')
        comment  = Comment(user=user, content=content, blog=post)
        comment.save()
    return render(request, 'blog/blog_comments.html', {'post':post , 'comments' : comments})

def blog_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = Blogpost.objects.filter(title__contains=searched)
        return render(request, 'search/search.html', {"searched":searched, "blogs":blogs})
    else:
            return render(request, 'search/search.html')
        

def follow(request, user_id):
    followed_user = User.objects.get(id=user_id)
    Follower_Following.objects.create(following=request.user, follower=followed_user)
    return redirect(user_profile, user_id)

def unfollow(request, user_id):
    followed_user = User.objects.get(id=user_id)
    Follower_Following.objects.filter(following=request.user, follower=followed_user).delete()
    return redirect(user_profile, user_id)



def BlogPostLike(request, pk):
    post = get_object_or_404(Blogpost, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse(user_profile, args=[str(pk)]))

class BlogPostDetailView(DetailView):
    model = Blogpost
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Blogpost, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data
    
class UpdatePostView(UpdateView):
    model = Blogpost
    template_name = 'blog/edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'image']

def Delete_Blog_Post(request, slug):
    posts = Blogpost.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'blog/delete_blog_post.html', {'posts':posts})

def Delete_Comment(request,  user_id):
     post = Blogpost.objects.filter(id=user_id).first()
     comments = Comment.objects.filter(blog=post)
     if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        blog_id = request.POST.get('blog_id', '')
        comment  = Comment(user=user, content=content, blog=post)
        comment.delete()
     return render(request, 'blog/blog_comments.html', {'post':post , 'comments' : comments})

    # comments = Comment.objects.filter(id=user_id)
    # if request.method == "POST":
    #     comments.delete()
    #     return redirect('/')
    # return render(request, 'blog/blog_comments.html', { 'comments':comments})

# def friend_list(request):
# 	p = request.user.Profile
# 	friends = p.friends.all()
# 	context={
# 	'friends': friends
# 	}
# 	return render(request, "users/friend_list.html", context)     
    


# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'hilaryemmanuel841@gmail.com',
#     ['ehilary689@yahoo.com'],
#     fail_silently=False,
# )




