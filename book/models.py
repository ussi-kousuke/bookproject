from django.db import models
from .consts import MAX_RATE
from cloudinary.models import CloudinaryField



# Create your models here.

CATEGORY = (('business', 'ビジネス'), ('science ・Technology', '科学・テクノロジー'), ('Humanities ・ ideas', '人文・思想'), ('computer・IT', 'コンピュータ・IT'))
RATE_CHOICES = [(x, str(x))for x in range(0, MAX_RATE + 1)]

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = CloudinaryField('image', null=True, blank=True)
    img_url = models.URLField(null=True, max_length=1000)
    category = models.CharField(
        max_length = 100,
        choices = CATEGORY
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url=''
        return url
    


   
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



        


