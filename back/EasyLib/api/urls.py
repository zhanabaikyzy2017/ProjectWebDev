from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path('books/',views.BookList.as_view()),
    path('books/<int:pk>/reviews/', views.ReviewListOfOneBook.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),

    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>',views.CategoryDetail.as_view()),
    path('categories/<int:pk>/books', views.CategoryBooks.as_view()),
    path('categories/<int:pk>/books/<int:pk2>/',views.BookCreate.as_view()),

    path('authors/',views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('authors/<int:pk>/books', views.AuthorBooks.as_view()),

    path('reviews/', views.ReviewList.as_view()),
    path('users/', auth.UserList.as_view()),
    path('this_user',auth.this_user),

    path('login/',auth.login),
    path('logout/', auth.logout),
    path('signup/', auth.signup),

    path('user_profiles/',views.UserProfileList.as_view()),
    path('user_profile/<int:pk>/books', views.UserProfBooks.as_view()),
    path('user_profiles/<int:pk>', views.UserProfileDetail.as_view())


]