from django.contrib import admin

from blog.forms import ContentForm
from blog.models import Category, Content, Tags

admin.site.register(Category)
admin.site.register(Tags)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    form = ContentForm
    list_display = ["title", "slug", "category"]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_filter = ["category"]
    list_per_page = 10
    readonly_fields = ["slug"]
    fieldsets = (
        ("Primary", {"fields": ("title",)}),
        ("Secondary", {"fields": ("category", "tags", "publish")}),
        (None, {"fields": ("body",)}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        if user.groups.filter(name="Creator").exists():
            return qs.filter(created_by=user)
        return qs

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        user = request.user
        if user.groups.filter(name="Creator").exists():
            fieldsets[1][1]["fields"] = ("category", "tags")
        else:
            fieldsets[1][1]["fields"] = ("category", "tags", "publish")
        return fieldsets

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            title = obj.title
            obj.slug = title.lower().replace(" ", "-")
            obj.created_by = request.user
        super(ContentAdmin, self).save_model(request, obj, form, change)
