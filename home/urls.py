from django.contrib import admin
from django.urls import path
from home import views
from .views import ProfileFollowToggee
from django.contrib.auth import views as auth_views



urlpatterns = [ 
    path('',views.index, name="index"),
    path('index',views.index, name="index"),
    path('home',views.home, name="home"),
    path('login',views.loginUser, name="login"),
    path('reset_password_complete/login',views.loginUser, name="login"),
    path('new',views.new, name="new"),
    path('search',views.search, name="search"),
    path('writer_search',views.writer_search, name="writer_search"),
    path('main/<int:pk>',views.showblog, name="main"),
    path('main/<int:pk>/comment', views.postComment, name='comment-blog'),
    path('logout',views.logoutUser, name="logout"),
    path('user_profile/<int:pk>', views.user_profile, name="user-profile"),
    path('feedback',views.feedback, name="feedback"),
    path('liked/', views.like_unlike_post, name='like-post-view'),
    path('likes/', views.like, name='like'),
    path('like/', views.likePost, name='like-post'),
    path('likeView/', views.likeView, name='like-view'),
    path('create_blog', views.create_blog , name='create_blog'),
    path('delete_post/<int:pk>', views.delete_post, name='delete-post'),
    path('editprofile', views.edit_profile , name='edit-profile'),
    path('viewprofile/<int:pk>', views.view_profile , name='view-profile'),
    path('writers', views.view_writer , name='view-writer'),
    path('ansBlog/<int:pk>', views.ansblog , name='ansBlog'),
    path('profile-follow/<int:pk>', ProfileFollowToggee.as_view() , name='follow'),
    path('seeBlog/<int:pk>', views.seeblog , name='seeBlog'),
    path('privacypolicy', views.privacypolicy , name='privacypolicy'),
    path('termcondition', views.termcondition , name='termcondition'),
    path('about_us', views.about_us , name='about_us'),
    path('confirm_password', views.confirm_password , name='confirm-password'),
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),
]

# template_name="template/confirm_password.html"