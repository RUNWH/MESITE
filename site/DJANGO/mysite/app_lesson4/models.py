from django.db import models

class Lesson4(models.Model):
    title=models.CharField("Загаловок",max_length=128)
    Description=models.TextField("Описание")
    Price=models.DecimalField("Цена",max_digits=8,decimal_places=2)
    auction=models.BooleanField("ТОрг",help_text="если готовы торговаться отметье")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.Price:.2f})"


    class Meta:
        db_table='advertisements'