from django.db import models # type: ignore

# Create your models here.
class Post(models.Model):
  sno = models.AutoField(primary_key=True)
  title = models.CharField(max_length = 255)
  content = models.TextField()
  author = models.CharField(max_length=15)
  slug = models.CharField(max_length=150)
  timeStamp = models.DateTimeField(blank=True)
  image = models.ImageField(upload_to='post_images/', blank=True,
  null=True)
  
  def __str__(self):
    return self.title + '-' + self.author
  
class Member(models.Model):			
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  email = models.EmailField(max_length=200)
  passwd = models.CharField(max_length=50)
  age = models.IntegerField()
  def __str__(self):
    return self.fname + ' ' + self.lname