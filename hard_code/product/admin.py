from django.contrib import admin

from product.models import Product, UserProductAccess, Lesson, LessonView


admin.site.register(Product)
admin.site.register(UserProductAccess)
admin.site.register(Lesson)
admin.site.register(LessonView)