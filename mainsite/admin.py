from django.contrib import admin

from mainsite.models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "draft")
    list_display_links = ("title",)
    search_fields = ("title",)
    save_on_top = True
    save_as = True
    actions = ["published", "unpublished"]
    list_editable = ("draft",)

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

    published.short_description = "Опублікувати"
    published.allowed_permissions = ("change",)
    unpublished.short_description = "Зняти з публікації"
    unpublished.allowed_permissions = ("change",)