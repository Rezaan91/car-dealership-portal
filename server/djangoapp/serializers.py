from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CarMake, CarModel, Dealer, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['id', 'name', 'description']


class CarModelSerializer(serializers.ModelSerializer):
    make_name = serializers.CharField(source='make.name', read_only=True)
    
    class Meta:
        model = CarModel
        fields = ['id', 'make', 'make_name', 'name', 'car_type', 'year']


class DealerSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Dealer
        fields = ['id', 'name', 'address', 'city', 'state', 'zip_code', 
                  'phone', 'email', 'website', 'short_desc', 'full_desc', 'review_count']
    
    def get_review_count(self, obj):
        return obj.reviews.count()


class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.username', read_only=True)
    dealer_name = serializers.CharField(source='dealer.name', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'dealer', 'dealer_name', 'customer', 'customer_name', 
                  'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year',
                  'review_text', 'sentiment', 'created_at', 'updated_at']
        read_only_fields = ['customer', 'sentiment', 'created_at', 'updated_at']
