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
        fields = ('BlogId', 'Name', 'Website', 'Youtube', 'Instagram', 'Facebook', 'About',
                'flaTravelWithChildren', 'flaTravelWithAnimals', 'flaOrganizeTrips', 'Countries', 'Languages')
        read_only_fields = ('UserId',)


class UsersBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('BlogId', 'Name')
