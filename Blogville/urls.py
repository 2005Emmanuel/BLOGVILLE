from django.urls import path
from .import views
from .views import UpdatePostView

urlpatterns = [
    path('', views.blogs, name='blogs'),
    
    #Authentication urls
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    
    
    #User profile urls
    path('profile/', views.profile, name='profile') ,
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('user_profile/<int:myid>/', views.user_profile, name='user_profile'),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    
    
    path('add_Blog/', views.add_Blog, name='add_Blog'),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("blog/<str:slug>/", views.blog_comments, name="blog_comments"),
    path("Delete_Comment/<int:user_id>/", views.Delete_Comment, name='Delete_Comment'),
    path("blog_search/", views.blog_search, name='blog_search'),
    
    
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name="blogpost_like"),
    
#    path('like_article/<int:Blogpost_id>/', views.like_article, name="like_article"),
#    path('unlike_article/<int:Blogpost_id>/', views.unlike_article, name="unlike_article"),
    #  path('like_toggle/<int:id>/', views.like_toggle, name='like_toggle'),
    

    
    # path('folower_profile/<int:user_id>/', views.folower_profile, name='folower_profile')
]