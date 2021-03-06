from django.contrib import admin

# Register your models here.

from .models import Report
from .models import ReportImage

class ReportImageInline(admin.StackedInline):
    model = ReportImage
    extra = 1

class ReportAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None, {'fields' : ['type']}),
        ('Pet info', {'fields' : ['animal', 'name', 'genre', 'breed', 'color']}),
        ('Location info', {'fields' : ['city', 'zone', 'n_hood']}),
        ('Report', {'fields' : ['reporter_name', 'email', 'phone', 'comment'] }),
                 ]
    inlines = [ReportImageInline]
    
    
    
admin.site.register(Report, ReportAdmin)
admin.site.register(ReportImage)
