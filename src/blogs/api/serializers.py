from rest_framework import serializers
from blogs.models import Language, Blog, Country


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('blogId', 'name', 'website', 'youtube', 'instagram', 'facebook', 'about',
                'flaTravelWithChildren', 'flaTravelWithAnimals', 'flaOrganizeTrips', 'countries', 'languages')
        read_only_fields = ('userId',)


class UsersBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('blogId', 'name')
