from django.db import models

# Create your models here.
class Article(models.Model):
   author=models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name="Yazar")
   title=models.CharField(max_length=50,verbose_name="Başlık")
   content=models.TextField()
   created_date=models.DateField(auto_now_add=True)
   def __str__(self):  
    return self.title