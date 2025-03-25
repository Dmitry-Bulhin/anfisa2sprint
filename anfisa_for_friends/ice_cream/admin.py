from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper


admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline): # admin.StackedInline or admin.TabularInline
    model = IceCream
    extra = 1  # количество пустых форм в конце


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )


# ...и регистрируем её в админке:
# admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
# admin.site.register(IceCream)
# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)