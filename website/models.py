from django.db import models




class record2(models.Model):
	domain=models.CharField(max_length=100)
	subdomain=models.CharField(max_length=100)
	coursename=models.CharField(max_length=100,default="Unknown")
	instructor=models.CharField(max_length=100,default="Unknown")
	video=models.CharField(max_length=1000)


	def __str__(self):
		return self.domain