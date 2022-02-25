from rest_framework import serializers

from product.models import Product, Category, Discount


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'category_root', 'product_set']

    # product_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name_product = serializers.CharField(max_length=20)
    brand = serializers.CharField(max_length=20)
    descriptions = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    number_store = serializers.IntegerField()
    status = serializers.ChoiceField(choices=[('exist', True), ('Not exist', False)], default=False)
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    image = serializers.FileField(default='NO_pic.png')
    discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all())
    category = CategorySerializer(read_only=True)

    def update(self, instance: Product, validated_data: dict) -> Product:
        pass

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
