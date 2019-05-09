from django.contrib import admin
from api.models import Book,Category,Author,Publisher,UserProfile


# admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
#admin.site.register(UserProfile)


@admin.register(Book)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','title','description',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)