from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Q
from django.urls import reverse
from hitcount.models import HitCount


# Create your models here.
class NewsManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query))
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class News(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описання", max_length=335)
    banner = models.ImageField("Банер", upload_to="news/banners/", null=True)
    image = models.ImageField("Зображення", upload_to="news/images/", null=True, blank=True)
    text = models.TextField("Зміст")
    premiere = models.DateField("Дата публікації", default=date.today)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    url = models.SlugField(max_length=255, unique=True, default="Введіть унікальний аудентифікатор")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    draft = models.BooleanField("Чернетка", default=False)
    objects = NewsManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_details", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"
