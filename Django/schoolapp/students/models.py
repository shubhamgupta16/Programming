from django.db import models

class RegistrationForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    roll_no = models.IntegerField(unique = True, null=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    
    
    def __str__(self):
        self.name = self.first_name + " " + self.last_name 
        return self.name

    class Meta:
        db_table = "student"