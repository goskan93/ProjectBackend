from django.urls import path
from .views import BlogListView, LanguageListView, CountryListView, BlogCreateView, BlogByUserListView, BlogView

urlpatterns = [
    path('GetBlogList/', BlogListView.as_view()),
    path('GetLanguagesList/', LanguageListView.as_view()),
    path('GetCountriesList/', CountryListView.as_view()),
    path('CreateBlog/', BlogCreateView.as_view()),
    path('GetUsersBlogs/', BlogByUserListView.as_view()),
    path('GetBlog/<uuid:BlogId>', BlogView.as_view()),
    path('UpdateBlog/<uuid:BlogId>', BlogView.as_view()),
    path('DeleteBlog/<uuid:BlogId>', BlogView.as_view()),
    # path('AddBlog/', addBlog),
]
