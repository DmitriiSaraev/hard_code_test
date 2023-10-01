from rest_framework import serializers

from product.models import Product, Lesson, LessonView, UserProductAccess


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductAccess
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = '__all__'