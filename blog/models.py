from django.db import models


# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # This is first heading
    heading_1 = models.CharField(max_length=200)
    heading_1_content = models.CharField(max_length=5000)
    # This is first heading subheading.
    sub_heading_1 = models.CharField(max_length=200)
    sub_heading_1_content = models.CharField(max_length=5000)
    # This is second heading.
    heading_2 = models.CharField(max_length=200)
    heading_2_content = models.CharField(max_length=5000)
    # This is second sub heading.
    sub_heading_2 = models.CharField(max_length=200)
    sub_heading_2_content = models.CharField(max_length=5000)
    # This is third heading
    heading_3 = models.CharField(max_length=200)
    heading_3_content = models.CharField(max_length=5000)
    # This is third sub heading.
    sub_heading_3 = models.CharField(max_length=200)
    sub_heading_3_content = models.CharField(max_length=5000)
    # publication date
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title
