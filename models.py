from django.db import models

# Create your models here.




class RecipeDump(models.Model):
    class Meta:
        db_table = "addrecipe"
        ordering = ['name']
    def __unicode__(self):
        return self.name

    #imported_pk = models.IntegerField()
    category_name = models.CharField(max_length = 100)
    something = models.CharField(max_length = 100, null=True, blank=True)
    name =  models.CharField(max_length = 100)
    ingredients =  models.TextField()
    instructions = models.TextField()
    image = models.CharField(max_length=100, null=True, blank=True)
    blah = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    foo = models.CharField(max_length=100)
    bar = models.CharField(max_length=100)
    baz = models.CharField(max_length=100)
    
   
    
