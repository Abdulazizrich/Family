from django.db import models
from django.contrib.auth.models import User


class Suv(models.Model):
    brend=models.CharField(max_length=25)
    narx=models.PositiveIntegerField()
    litr=models.PositiveSmallIntegerField()
    batafsil=models.TextField()

    def __str__(self):
        return f"{self.brend}  {self.litr}"

class Mijoz(models.Model):
    ism=models.CharField(max_length=25)
    tel=models.CharField(max_length=30)
    manzil=models.CharField(max_length=50)
    qarz=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.ism}  {self.tel}"

class Admin(models.Model):
    ism=models.CharField(max_length=25)
    yosh=models.PositiveSmallIntegerField(max_length=30)
    ish_vaqti=models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism}  {self.yosh}"

class Haydovchi(models.Model):
    ism = models.CharField(max_length=25)
    tel = models.CharField(max_length=30)
    kiritilgan_sana=models.DateField()

    def __str__(self):
        return f"{self.ism}  {self.tel}"

class Buyurtma(models.Model):
    suv=models.ForeignKey(Suv,on_delete=models.CASCADE)
    sana=models.DateField()
    mijoz=models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    miqdor=models.PositiveIntegerField()
    umumiy_narx=models.PositiveIntegerField()
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    haydovchi=models.ForeignKey(Haydovchi,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.miqdor} {self.umumiy_narx}"


