from django.db import models
from django.urls import reverse

class Detail(models.Model):
    name = models.CharField(max_length=255, unique=True)
    detail_name = models.CharField(max_length=255)
    detail_mark = models.CharField(max_length=255)
    eskd_mark = models.CharField(max_length=255, blank=True)
    standard_name = models.CharField(max_length=255)
    standard_mark = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    depth = models.CharField(max_length=255)
    cost_result_without_cover = models.CharField(max_length=255)
    cost_result_in_cover = models.CharField(max_length=255)
    # cost = None
    type_of_execution = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    # cat = models.ForeignKey('Category') # on_delete=models.PROTECT

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = "Detail"
        
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
#     def __str__(self):
#         return self.name    