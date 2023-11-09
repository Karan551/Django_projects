from django.db import models


# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length=50)
    prod_desc = models.TextField(max_length=700)
    prod_reg_date = models.DateField()
    # this added new.
    prod_price = models.IntegerField(default=0)
    prod_image = models.ImageField(upload_to='eshop/images', default='')
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')

    def __str__(self):
        # To show the product name in admin field.
        return self.prod_name


class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='', primary_key=True)
    phone = models.CharField(max_length=15, default='')
    desc = models.CharField(max_length=500, default='')

    def __str__(self):
        # To show the username in the database.
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=6000, default='')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=6000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:15] + "...."
