from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from rest_framework import status
from rest_framework.response import Response
from blogs.models import Blog, Language, Country
from .serializers import BlogSerializer, LanguageSerializer, CountrySerializer
import pdb


class LanguageListView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def addBlog(request):
    # request.data is like dictionary
    serializer = BlogSerializer(data=request.data)
    breakpoint()
    if serializer.is_valid():
        serializer.save(UserId=request.user)
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
