from django.contrib import admin
from .models import Product, Category, Brand, Testimony


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'brand',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_brand_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class TestimonyAdmin(admin.ModelAdmin):
    """ Structure the admin testimony field """
    list_display = ('body', 'product', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['body']
    actions = ['approve_testimonies']

    def approve_testimonies(self, request, queryset):
        """ Approves tesimonies """
        queryset.update(approve=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Testimony)
