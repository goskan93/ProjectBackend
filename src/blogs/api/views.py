from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from blogs.models import Blog, Language, Country
from .serializers import BlogSerializer, LanguageSerializer, CountrySerializer, UsersBlogsSerializer
import pdb


class LanguageListView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class BlogListView(ListAPIView):
    # queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        """Returns a list of of People that match the critera"""
        # get query parameters
        # countries = self.request.query_params.get('Countries', None)
        # languages = self.request.query_params.get('Languages', None)
        countries = self.request.GET.getlist('Countries')
        languages = self.request.GET.getlist('Languages')
        # return the filter set based on parameters sent
        if countries and languages:
            return Blog.objects.filter(Countries__id__in=countries).filter(Languages__id__in=languages)
        elif countries and not languages:
            return Blog.objects.filter(Countries__id__in=countries)
        elif not countries and languages:
            return Blog.objects.filter(Languages__id__in=languages)
        else:
            return Blog.objects.all()  # returns everyone if no filters set


class BlogByUserListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = UsersBlogsSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Blog.objects.filter(UserId=self.request.user)

class BlogView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'BlogId'


class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(UserId=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'Message': 'You have successfully add your blog.'}, status=status.HTTP_201_CREATED, headers=headers)


# second wayto do this
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addBlog(request):
    # request.data is like dictionary
    breakpoint()
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(UserId=request.user)
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
