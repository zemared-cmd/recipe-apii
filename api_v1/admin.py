from django.contrib import admin
from .models import Category, Ingredient, Recipe, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'unit']
    search_fields = ['name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'difficulty', 'cook_time_min', 'author', 'created_at']
    list_filter = ['category', 'difficulty']
    search_fields = ['title', 'description']
    filter_horizontal = ['ingredients']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'rating', 'text_preview', 'user', 'created_at']
    list_filter = ['rating']
    search_fields = ['text']

    def text_preview(self, obj):
        return obj.text[:60] + ('...' if len(obj.text) > 60 else '')
    text_preview.short_description = 'Текст отзыва'
