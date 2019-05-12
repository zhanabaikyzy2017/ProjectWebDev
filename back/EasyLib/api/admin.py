from django.contrib import admin

from api.models import Book,Category,Author,Publisher,UserProfile,Review

#from ..api.models import Book,Category,Author,Publisher,UserProfile



# admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Review)
admin.site.register(UserProfile)


@admin.register(Book)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','title','description',)

