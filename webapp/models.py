from django.db import models


class general_setting(models.Model):
    id = models.AutoField(primary_key=True)

    company_Logo = models.ImageField()
    company_title = models.CharField(max_length = 500)
    company_mobile = models.CharField(max_length = 500)
    company_email = models.CharField(max_length = 500)

    def __str__(self):
        return self.company_title
# Create your models here.

class Slider(models.Model):
    id = models.AutoField(primary_key=True)

    image = models.ImageField()
    title = models.CharField(max_length = 500)
    def __str__(self):
        return self.title

class Tutorial(models.Model):
   id = models.AutoField(primary_key=True)

   name = models.CharField(max_length = 50)
   discription = models.CharField(max_length = 255)
   
   def __str__(self):
       return self.name

class Caurses(models.Model):
   caurse_id = models.AutoField(primary_key=True)

   title = models.CharField(max_length = 50)
   about_title = models.CharField(max_length = 50 )
   price = models.IntegerField(default="")
   image = models.ImageField(upload_to='media', null=True, blank=True)
   topic = models.CharField(max_length = 255)
   
   def __str__(self):
       return self.title

class footer_discription(models.Model):
   id = models.AutoField(primary_key=True)

   title = models.CharField(max_length = 50)
  
   discription = models.CharField(max_length = 255)
   
   def __str__(self):
       return self.title

class Contact(models.Model):
   id = models.AutoField(primary_key=True)

   firstname = models.CharField(max_length = 50)
  
   lastname = models.CharField(max_length = 50)
   mob = models.CharField(max_length = 50)
   email = models.EmailField()
   message = models.CharField(max_length=500)
   
   def __str__(self):
       return self.firstname

class email_templates(models.Model):
   id = models.AutoField(primary_key=True)

   name = models.CharField(max_length = 50)
   sub = models.CharField(max_length = 50)
   content = models.TextField()
   def __str__(self):
       return self.name

class Topic(models.Model):
   topic_id = models.AutoField(primary_key=True)
   caurse_id = models.IntegerField()
   name = models.CharField(max_length = 50)
   content = models.TextField()
   def __str__(self):
        return self.name
