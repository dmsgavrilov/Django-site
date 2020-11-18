from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'Задачи'

class Document(models.Model):
    description = models.CharField("Key", max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file(self):
        return self.document

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'Files'