from rest_framework import serializers
from .models import Category, Ingredient, Recipe, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit']


class ReviewSerializer(serializers.ModelSerializer):
    recipe = serializers.StringRelatedField(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
        source='recipe',
        write_only=True,
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'recipe', 'recipe_id', 'text', 'rating', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5.')
        return value


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True,
    )
    ingredients = serializers.StringRelatedField(many=True, read_only=True)
    ingredient_ids = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(),
        source='ingredients',
        write_only=True,
        many=True,
        required=False,
    )
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'instructions',
            'cook_time_min', 'servings', 'difficulty',
            'category', 'category_id',
            'ingredients', 'ingredient_ids',
            'author', 'created_at',
        ]
        read_only_fields = ['author', 'created_at']
