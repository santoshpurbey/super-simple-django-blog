from django.conf import settings
from django.contrib import admin
from .models import BlogEntry


class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'is_published', 'view_on_site',)

    def view_on_site(self, blog_entry):
        view_on_site = ''

        absolute_url = blog_entry.get_absolute_url()
        if absolute_url:
            view_on_site += u'<a href="{}" title="View on site" target="_blank">view on site</a>'.format(absolute_url)
        return view_on_site

    view_on_site.short_description = ''
    view_on_site.allow_tags = True


admin.site.register(BlogEntry, BlogEntryAdmin)
