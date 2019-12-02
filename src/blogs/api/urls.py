from django.urls import path
from .views import BlogListView, LanguageListView, CountryListView, addBlog, BlogCreateView, BlogByUserListView, BlogView

urlpatterns = [
    path('GetBlogList/', BlogListView.as_view()),
    path('GetLanguagesList/', LanguageListView.as_view()),
    path('GetCountriesList/', CountryListView.as_view()),
    path('CreateBlog/', BlogCreateView.as_view()),
    path('GetUsersBlogs/', BlogByUserListView.as_view()),
    path('GetBlog/<uuid:BlogId>', BlogView.as_view()),
    # path('AddBlog/', addBlog),
]
