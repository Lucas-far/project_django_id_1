

from django.db import models

class Base(models.Model):
    created = models.DateTimeField('Data de criação', auto_now_add=True)
    updated = models.DateTimeField('Última atualização', auto_now=True)

class Tasks(Base):
    task = models.CharField('Qual a tarefa a ser adicionada?', max_length=1500)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
