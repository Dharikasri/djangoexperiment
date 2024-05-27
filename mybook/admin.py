from django.contrib import admin
from .models import mybook, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'author')

admin.site.register(mybook, BookAdmin)  

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

admin.site.register(Author, AuthorAdmin) 
