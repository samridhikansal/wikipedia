from django.db import models

# Create your models here.

class Topics(models.Model):
     heading = models.CharField(max_length=500)
     desc= models.CharField(max_length= 2000)
     author_name = models.CharField(max_length=200)
     image = models.ImageField(upload_to="images/", default=None)
     def __str__(self):
          return self.heading

class Authors(models.Model):
     author_name = models.CharField(max_length=200)
     password = models.CharField(max_length=50)

class Comments(models.Model):
     each_topic = models.ForeignKey(Topics, on_delete = models.CASCADE)
     comments = models.CharField(max_length=1000)
     def __str___(self):
          return self.comments
class LikesDislikes(models.Model):
          each_topic = models.ForeignKey(Topics, on_delete = models.CASCADE)
          like = models.IntegerField(default=0, blank=True)
          dislike= models.IntegerField(default=0 , blank=True)