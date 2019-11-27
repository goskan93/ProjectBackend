from django.urls import path
from .views import BlogListView, LanguageListView, CountryListView, addBlog

urlpatterns = [
    path('GetBlogList/', BlogListView.as_view()),
    path('GetLanguagesList/', LanguageListView.as_view()),
    path('GetCountriesList/', CountryListView.as_view()),
    path('AddBlog/', addBlog),
]
