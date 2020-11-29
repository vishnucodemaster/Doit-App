from django.db import models

# Create your models here.
class mydoit(models.Model):
	##id = models.Autofield(primary_key=True)
	mydoit_text = models.CharField(max_length=200)
	added_on = models.DateTimeField(auto_now =True)
	updated_on = models.DateTimeField(auto_now=True)


def __str__(self):
	return self.mydoit_text

class Meta:	
	ordering=['-id']