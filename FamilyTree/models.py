from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    maiden_name = models.CharField(max_length=50, blank=True)
    birth_city = models.CharField(max_length=75, blank=True)
    birth_country = models.CharField(max_length=75, blank=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    profile_pic = models.ImageField(upload_to='profile_folder/', 
                                    default='profile_folder/None/no-img.jpg')

    
    
    
    def __str__(self):
        return self.last_name + ', ' + self.first_name + ' ' + self.middle_name
    
    
