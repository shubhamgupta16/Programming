from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Books(models.Model):
    isbn = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    genere = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField()


    def __str__(self):
        return self.title

    class Meta:
        db_table = "LibraryManagementTool"

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Books)
def my_callback(sender, instance, **kwargs):
    if instance.quantity == 0 :
        instance.available = False
    else:
        instance.available = True
