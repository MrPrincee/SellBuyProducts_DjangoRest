from rest_framework import serializers


from product.models import Products, Profile
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'price']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        product = Products.objects.create(**validated_data)

        return product

    def validate_price(self,value):
        if value == 0:
            raise serializers.ValidationError("Price can't be 0!")
        return value


class SellProductsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Products
        fields =['id','price']

    def create(self,validated_data):
        product_for_sale = Products.objects.get(id=validated_data['id'])
        if product_for_sale.owner == self.context['request'].user:
            product_for_sale.available_for_sale = True
            product_for_sale.price = validated_data['price']
            product_for_sale.save()
        return product_for_sale


class BuyProductsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Products
        fields = ['id']

    def create(self,validated_data):
        product_to_buy = Products.objects.get(id=validated_data['id'])
        product_owner_profile = Profile.objects.get(user = product_to_buy.owner)
        user_profile = Profile.objects.get(user=self.context['request'].user)  # Assuming Profile has a ForeignKey to User
        if user_profile.balance >= product_to_buy.price:
            if product_to_buy.available_for_sale:
                product_owner_profile.balance += product_to_buy.price
                product_owner_profile.save()

                product_to_buy.owner = self.context['request'].user
                product_to_buy.available_for_sale = False
                product_to_buy.save()

                user_profile.balance -= product_to_buy.price
                user_profile.save()

        return product_to_buy



