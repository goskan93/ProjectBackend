from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from blogs.models import Blog, Language, Country
from .serializers import BlogSerializer, LanguageSerializer, CountrySerializer
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
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    # filter_backends = [SearchFilter, ]
    # search_fields = ['Name']
    # lekcja 12 query list of blogs - ale mysle zeby jakos zrobic u mnie filter po jezyku(kilka) i panstwach (jeden lub np max 3)


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
