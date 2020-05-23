from django.db import models


# Create your models here.
class HepepServices:
    service_name: str
    logo: str
    service_desc: str


class HepepsTeam(models.Model):
    # name = models.CharField(max_length=200)
    # img = models.ImageField(upload_to='pics')
    # Desc = models.TextField()
    # Read_more = models.CharField(max_length=200)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_names = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='pics')
    Bio = models.TextField()
    role = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Hepeps Team'


class BackgroundImages(models.Model):
    img = models.ImageField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Background Images'


class Services(models.Model):
    service_name = models.CharField(max_length=200)
    service_desc = models.TextField()
    service_img = models.ImageField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Services'


class Blog(models.Model):
    post_title = models.CharField(max_length=200)
    post_desc = models.TextField()
    post_img = models.ImageField(upload_to='pics')
    img_title = models.CharField(max_length=200)
    post_category = models.CharField(max_length=200)
    post_date = models.DateTimeField()
    post_by = models.ForeignKey(HepepsTeam, default=1, verbose_name="Post By", on_delete=models.SET_DEFAULT)
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Blog'
    def __str__(self):
        return self.post_title

    def category_count(self):
        # Your filter criteria can go here.
        return self.post_category_set.count()


# # Configuration models
# class Regions(models.Model):
#     region_name = models.CharField(max_length=200)
#     status = models.BooleanField()
#
#
# class Districts(models.Model):
#     district_name = models.CharField(max_length=200)
#     status = models.BooleanField()
#
#
# class Country(models.Model):
#     country_name = models.CharField(max_length=200)
#     status = models.BooleanField()

# Configuration models
# class Addresses(models.Model):
#   address_line1 = models.TextField()
#  address_line2 = models.TextField()
# postBox_or_code = models.CharField(max_length=200)
#   district = models.CharField(max_length=200)
#  region = models.CharField(max_length=200)
#  country = models.CharField(max_length=200)


# class HepepsConfiguration(models.Model):
#   company_name = models.CharField(max_length=100)
#  Logo = models.ImageField(upload_to='pics')
#   Vision = models.TextField()
#  Mission = models.TextField()
#  Address = models.TextField()
#  Country = models.CharField(max_length=100)
# Email = models.CharField(max_length=100)
# status = models.BooleanField()
