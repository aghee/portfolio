from django.contrib import admin
from .models import Tag, Project, ProjectImage,Contact

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model=ProjectImage
    extra=1

class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "github_link",
        "app_link"
    )
    inlines=[ProjectImageInline]
    search_fields=("title", "description")
    list_filter=("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display=("name",)
    search_fields=("name",)

class ContactAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "phone_number",
        "email",
        "organization",
    )
    search_fields=("name","email")


admin.site.register(Tag,TagAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Contact,ContactAdmin)