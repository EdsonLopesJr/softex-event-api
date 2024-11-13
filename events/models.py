from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    start_date = models.DateTimeField(verbose_name='Início')
    end_date = models.DateTimeField(verbose_name='Fim')

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Evento'

    def __str__(self):
        return self.name