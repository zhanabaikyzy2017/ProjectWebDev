from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path('books/',views.BookList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('publishers/',views.PublisherList.as_view()),
    path('authors/',views.AuthorList.as_view()),
    path('books/<int:pk>/reviews/',views.ReviewListOfOneBook.as_view()),
    path('books/<int:pk>/reviews',views.ReviewListOfOneBook.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('users/',auth.UserList.as_view()),
    path('login/',auth.login),
    path('logout/', auth.logout),
    path('user_profile/',views.UserProfileList.as_view()),
    path('categories/<int:pk>/books', views.CategoryBooks.as_view()),
    path('authors/<int:pk>/books', views.AuthorBooks.as_view()),
    path('user_profile/books', views.UserProfileDetail.as_view())
]