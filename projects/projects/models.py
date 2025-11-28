from django.db import models

class Project(models.Model):
    PROJECT_TYPES = [('pinui_binui', 'פינוי בינוי'), ('tama_38_2', 'תמא 38/2'), ('tama_hizuk', 'תמא חיזוק')]
    STATUS_CHOICES = [('pre_stage', 'שלב מקדמי'), ('contract_signing', 'חתימת הסכם'), ('permit', 'היתר בניה'), ('execution', 'ביצוע'), ('completed', 'הסתיים')]
    
    name = models.CharField('שם הפרויקט', max_length=255)
    project_type = models.CharField('סוג', max_length=50, choices=PROJECT_TYPES, default='pinui_binui')
    address = models.CharField('כתובת', max_length=500)
    city = models.CharField('עיר', max_length=100, blank=True)
    developer = models.CharField('יזם', max_length=255, blank=True)
    status = models.CharField('סטטוס', max_length=50, choices=STATUS_CHOICES, default='pre_stage')
    total_apartments = models.IntegerField('סהכ דירות', default=0)
    signed_count = models.IntegerField('חתימות', default=0)
    notes = models.TextField('הערות', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'פרויקט'
        verbose_name_plural = 'פרויקטים'
    
    def __str__(self):
        return self.name
