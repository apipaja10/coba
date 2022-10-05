from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.pelanggan)
admin.site.register(models.owner)
admin.site.register(models.charge)
admin.site.register(models.peminjaman)
admin.site.register(models.pakaian)
admin.site.register(models.detailcharge)