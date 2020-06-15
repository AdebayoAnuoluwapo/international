from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'blog'

urlpatterns = [
      path('', views.HomeView.as_view(), name='home'),
      path('list/', views.PostListView.as_view(), name='list'),
      path('about/', views.AboutView.as_view(), name='about'),
      path('signup/', views.SignUp.as_view(), name='signup'),
      path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"),name='login'),
      path('logout/', auth_views.LogoutView.as_view(), name="logout"),
      path('<int:pk>/', views.PostDetailView.as_view(), name="detail"),
      path('post/new/', views.CreatePostView.as_view(), name="create"),
      path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name="edit"),
      path('drafts/', views.DraftListView.as_view(), name="drafts"),
      path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="delete"),
      path('post/<int:pk>/publish', views.post_publish, name='publish'),
      path('post/<int:pk>/comment/', views.add_comment_post, name='add'),
]