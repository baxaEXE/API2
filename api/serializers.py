from rest_framework import serializers 
from app.models import Book,CustomUser

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if object.image:
            image = obj.image.url
            return request.build_absolute_uri(image)
        return None
    
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'password',
            'username',
            'phone_number'
        ]

    