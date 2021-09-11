from django.db import models


# The Category model and the individual details each category will have 
class Category(models.Model):

    # This will correct the spelling in Django admin to the correct plural spelling
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=200, blank=False)
    friendly_name = models.CharField(max_length=200, null=True,
            blank=True)

    # To return the name of the category in the Django admin
    def __str__(self):
        return self.name

    # To return the friendly name of the category in the Django admin
    def get_friendly_name(self):
        return self.friendly_name

# The Product model and the individual details each product will have 
class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    p_id = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    # Always use DecimalField for money. Even simple operations like addition and subtraction are not immune to float rounding issues. https://stackoverflow.com/questions/2569015/django-floatfield-or-decimalfield-for-currency

    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # To return the name of the Product in the Django admin
    def __str__(self):
        return self.name