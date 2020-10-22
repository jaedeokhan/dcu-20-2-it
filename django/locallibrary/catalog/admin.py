from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.
#admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
#admin.site.register(BookInstance)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# add ModelAdmin 
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # List로 뿌려 주는 것 : list_display
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#  Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # def display_genre 
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'imprint', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Book', {
            'fields' : ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields' : ('status', 'due_back')
        })
    )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('book', 'name')

