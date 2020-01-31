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
    def validate(self, data):
        if not data['instagram'] and not data['facebook'] and not data['youtube'] and not data['website']:
            raise serializers.ValidationError("At least one social media or website must be given.")
        return data

    ## check this later
    def validate_countries(self, countries):
        if countries.length <= 0:
            raise serializers.ValidationError("At least one country must be given.")
        return countries

    class Meta:
        model = Blog
        fields = ('blogId', 'name', 'website', 'youtube', 'instagram', 'facebook', 'about',
                'flaTravelWithChildren', 'flaTravelWithAnimals', 'flaOrganizeTrips', 'countries', 'languages')
        read_only_fields = ('userId',)
    
    
class UsersBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('blogId', 'name')
