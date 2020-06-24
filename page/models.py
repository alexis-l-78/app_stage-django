from django.db import models

class Actor(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



class FILMS(models.Model):
    nom = models.CharField(max_length=100)
    actor = models.ManyToManyField(Actor, related_name='film', blank=True)

    def __str__(self):
        return self.nom
    
class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.tutorial_category
    
class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name=("Catégorie"), on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"
    
    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateField("date  published")
    tutorial_series = models.ForeignKey(TutorialCategory, default=1, verbose_name=("Series"), on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title
    
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")
    
    def __str__(self):
        return self.nom

