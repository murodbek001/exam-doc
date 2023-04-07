from .models import *
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id", )
    


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        read_only_fields = ("id", )




class ProductSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()



    class Meta:
        model = Product
        fields = ("id", "title", "desc", "image", "price", "cat_id", "cat", 'brand_id', 'brand')
        read_only_fields = ('id', 'cat', 'brand')

    def get_cat(self, obj):
        return obj.cat_id.title



    def get_brand(self, obj):
        return obj.brand_id.title