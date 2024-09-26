from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'region')  # Region bilan birgalikda tuman nomi unikal bo'lishi kerak

    def __str__(self):
        return f"{self.name} ({self.region.name})"

class MyModel(models.Model):
    barcode = models.CharField(max_length=20, null=True, blank=True)
    fish = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    post_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)  # Rasmni yuklash

    def __str__(self):
        return self.barcode if self.barcode else "No Barcode"  # Barcode yo'q bo'lganda maxsus xabar ko'rsatish
