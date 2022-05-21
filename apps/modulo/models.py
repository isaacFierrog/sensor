from django.db import models


class ModuloModel(models.Model):
    modulo_id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del modulo', max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'modulos'
        db_table = 'modulo'
        
    def __str__(self):
        return f'{self.nombre}'