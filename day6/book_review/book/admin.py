from django.contrib import admin
from .models import Book,Author

admin.site.site_header = "Custom Admin Project"

admin.site.site_title = "Custom Admin"

class BookAdmin(admin.ModelAdmin):
  list_display = ("title","description","publication_date","author")
  # fields = ("title","description","author")
  fieldsets = ((None,{
      'fields': ('title','description')
  }),('Extra Info',{
    'classes':('collapse',),
    'description':"this is a new group",
    'fields':('author',"publication_date")
  }))

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass

# Register your models here.
admin.site.register(Book,BookAdmin)
# admin.site.register(Author)