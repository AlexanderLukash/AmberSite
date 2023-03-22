from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from mainsite.models import News


# Register your models here.
class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_author", "get_image", "draft")
    list_display_links = ("title", "get_image")
    search_fields = ("title",)
    save_on_top = True
    save_as = True
    form = NewsAdminForm
    actions = ["published", "unpublished"]
    list_editable = ("draft",)

    def get_image(self, obj):

        return mark_safe(f'<img style="border-radius: 10%;" src={obj.banner.url} width="135" height="60"')

    def get_author(self, obj):
        return mark_safe(f'<b>{obj.author}</b>')

    def unpublished(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запис був оновлений."
        else:
            message_bit = f"{row_update} записів було оновлено."
        self.message_user(request, f"{message_bit}")

    def published(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запис був опублікований."
        else:
            message_bit = f"{row_update} записів було опубліковано."
        self.message_user(request, f"{message_bit}")


    get_image.short_description = "Банер"
    get_author.short_description = "Автор"
    published.short_description = "Опублікувати"
    published.allowed_permissions = ("change",)
    unpublished.short_description = "Зняти з публікації"
    unpublished.allowed_permissions = ("change",)