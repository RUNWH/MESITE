from django.db import models
from django.contrib import admin

class Lesson4(models.Model):
    title=models.CharField("Загаловок",max_length=128)
    description=models.TextField("Описание")
    price=models.DecimalField("Цена",max_digits=8,decimal_places=2)
    auction=models.BooleanField("ТОрг",help_text="если готовы торговаться отметье")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price:.2f})"


    class Meta:
        db_table='advertisements'

    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time=self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="дата обновления")
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            nowted_time=self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold">Сегодня в {}</span>', nowted_time
            )
        return self.created_at.strftime(" %d.%m.%Y в %H:%M:%S")        