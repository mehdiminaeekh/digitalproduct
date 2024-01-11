from rest_framework import serializers

from .models import Category, File, Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title', 'description', 'avatar']

class FileSerializers(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id','title', 'file_type', 'file']

    def get_file_type(self, obj):
        return obj.get_file_type_display()

class ProductSerializes(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializers(many = True)
    # file_set = FileSerializers(many = True)

# 'file_set was delete becuse do authentication'

    class Meta:
        model = Product
        fields = ['id','title', 'description', 'avatar', 'categories', 'url']