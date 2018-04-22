from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class ArtFolder(models.Model):
    class Meta:
        db_table = 'artfolder'

    artfolder_name = models.CharField(verbose_name='Название альбома', max_length=200, default='New folder')
    artfolder_date = models.DateTimeField(null=True)
    artfolder_user = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
class Arts(models.Model):
    class Meta:
        db_table = 'arts'

    art_title = models.CharField(max_length=200, default='New art')
    art_text = models.TextField(null=True)
    art_date = models.DateTimeField(null=True)
    art_likes = models.IntegerField(default=0)
    art_link = models.TextField(null=True)
    art_folder = models.ForeignKey(ArtFolder, on_delete=models.CASCADE, null=True)


class Comments_art(models.Model):
    class Meta:
        db_table = 'comments_art'

    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_arts = models.ForeignKey(Arts, on_delete=models.CASCADE)
    comments_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
