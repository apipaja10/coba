from tkinter import CASCADE
from django.db import models

# Create your models here.
class pakaian(models.Model):
    idpakaian = models.CharField(max_length=5, primary_key=True)
    jenispakaian = models.CharField(max_length=30)
    ukuranpakaian = models.CharField(max_length=10)
    hargapakaian = models.FloatField()
    konfirmasipakaian = models.BooleanField(null=True)
   

    def __str__(self):
        return str(self.jenispakaian)

class charge(models.Model):
    idcharge = models.CharField(max_length=5, primary_key=True)
    durasimaksimalpeminjaman = models.CharField(max_length=10)
    jenischarge = models.CharField(max_length=30)
    hargacharge = models.FloatField()

    def __str__(self):
        return str(self.jenischarge)

class owner(models.Model):
    idowner = models.CharField(max_length=5, primary_key=True)
    nama = models.CharField(max_length=50)
    jeniskelamin = models.CharField(max_length=10)
    nohandphone = models.IntegerField()
    alamat = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nama)

class pelanggan(models.Model):
    idpelanggan = models.CharField(max_length=5, primary_key=True)
    nama = models.CharField(max_length=50)
    jeniskelamin = models.CharField(max_length=10)
    nohandphone = models.IntegerField()
    alamat = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nama)

class peminjaman (models.Model):
    idpeminjaman = models.CharField(max_length=5, primary_key=True)
    idpakaian = models.ForeignKey(pakaian,on_delete=models.CASCADE)
    idpelanggan = models.ForeignKey(pelanggan,on_delete=models.CASCADE)
    idowner = models.ForeignKey(owner,on_delete=models.CASCADE)
    tanggalsewa = models.DateField()
    lamasewa = models.CharField(max_length=30)
    tanggalkembali = models.DateField()
    statuspeminjaman = models.BooleanField(null=True)


  
    def __str__(self):
        return str(self.tanggalsewa)

class detailcharge (models.Model):
    iddetailcharge = models.CharField(max_length=5, primary_key=True)
    idpeminjaman = models.ForeignKey(peminjaman,on_delete=models.CASCADE)
    idcharge = models.ForeignKey(charge,on_delete=models.CASCADE)
    jumlahitemcharge = models.IntegerField()

    def __str__(self):
        return str(self.idcharge)

