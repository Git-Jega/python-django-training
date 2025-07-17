from django.contrib import admin
from .models import Book,Author,Review,BorrowedBook

admin.site.site_header = "Custom Admin Project"

admin.site.site_title = "Custom Admin"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ("title","description","publication_date","author","full_title","is_available","copies")
  list_display_links = ('title',"publication_date","description","is_available","author")
  list_filter = ('title','author')
  search_fields = ('title__startswith','author__name','copies__lte')
  raw_id_fields = ("author",)
  list_per_page = 3
  # __gte -> greaterthan and equalto
  # __gt -> greater than
  # __lte -> lesserthan and equalto
  # __lt -> lesser than
  # list_editable = ('author',)
  # @admin.display(boolean=True,description="New Name")
  @admin.display(description="New Name")
  def full_title(self, obj):
    return f"{obj.title}-{obj.publication_date}"
    # return True
  # full_title.short_description = "CompleteName"

  # exclude = ("description",)
  # fields = ("title","description","author")
  # fieldsets = ((None,{
  #     'fields': ('title','description')
  # }),('Extra Info',{
  #   'classes':('collapse','wide'),
  #   'description':"this is a new group",
  #   'fields':('author',"publication_date")
  # }))

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ("name","bio","birth_date")
  search_fields = ("name","bio")
  # ordering = ("name",)
  def get_ordering(self, request):
    if(request.user.is_superuser):
      return('name',)
    else:
      return ('-name',)
@admin.register(Review)   
class ReviewAdmin(admin.ModelAdmin):
  list_display = ("book","user","created_at")
  search_fields = ("user__username",)
  list_display_links = ("book","user","created_at")

@admin.register(BorrowedBook)
class BorrowAdmin(admin.ModelAdmin):
  pass
# Register your models here.
# admin.site.register(Book,BookAdmin)
# admin.site.register(Author)