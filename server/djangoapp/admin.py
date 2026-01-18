from django.contrib import admin
from .models import CarMake, CarModel, Dealer, Review


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering = ['name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'make', 'car_type', 'year']
    list_filter = ['make', 'car_type', 'year']
    search_fields = ['name', 'make__name']
    ordering = ['make__name', 'name', 'year']


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone', 'email']
    list_filter = ['state', 'city']
    search_fields = ['name', 'city', 'state', 'email']
    ordering = ['state', 'city', 'name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'short_desc', 'full_desc')
        }),
        ('Contact Information', {
            'fields': ('address', 'city', 'state', 'zip_code', 'phone', 'email', 'website')
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['customer', 'dealer', 'purchase', 'sentiment', 'created_at']
    list_filter = ['purchase', 'sentiment', 'dealer', 'created_at']
    search_fields = ['customer__username', 'dealer__name', 'review_text']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Review Information', {
            'fields': ('dealer', 'customer', 'review_text', 'sentiment')
        }),
        ('Purchase Details', {
            'fields': ('purchase', 'purchase_date', 'car_make', 'car_model', 'car_year')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
