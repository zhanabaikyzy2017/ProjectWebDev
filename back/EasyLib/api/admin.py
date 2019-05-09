from django.contrib import admin
<<<<<<< HEAD
from api.models import Book,Category,Author,Publisher,UserProfile,Review
=======
from ..api.models import Book,Category,Author,Publisher,UserProfile
>>>>>>> 0faff589a477b1fe35164cd60c6f2f26620c23ea


# admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Review)


@admin.register(Book)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','title','description',)

