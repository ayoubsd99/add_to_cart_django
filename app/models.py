from django.db import models

# Create your models here.

class Item(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()

    def __str__(self):
        return self.title

    def get_images(self):
        images=[]



class ItemImages(models.Model):
    item=models.ForeignKey("app.Item",on_delete=models.CASCADE)    
    image=models.TextField()

    def __str__(self):
        return self.pk
    