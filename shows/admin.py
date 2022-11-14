from django.contrib import admin

# Register your models here.
from .models import Line, Show

admin.site.register(Line)
# admin.site.register(Show)


@admin.register(Show)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id','show_name']
  
  def tags(self):
    return self.line.line_text