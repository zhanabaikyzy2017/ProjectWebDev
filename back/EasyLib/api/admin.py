from django.contrib import admin

from api.models import Book,Category,Author,Publisher,UserProfile,Review

#from ..api.models import Book,Category,Author,Publisher,UserProfile



# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(Author)
# admin.site.register(Publisher)
# admin.site.register(Review)
# admin.site.register(UserProfile)


@admin.register(Book)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','title','description',)

@admin.register(Category)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Author)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','date_of_birth','date_of_death')

@admin.register(Publisher)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Review)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','user','book','text','creation_date')


@admin.register(UserProfile)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','user')

