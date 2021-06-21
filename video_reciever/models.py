from django.db import models

class Videos(models.Model):
    title = models.CharField(max_length=100, blank=True)
    video = models.FileField(upload_to='videos/', verbose_name="")
    size = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title