from django.db import models

# Create your models here.

class Line(models.Model):
    CATEGORY = (
        ('A1','Actor 1'),
        ('A2','Actor 2'),
        ('A3','Actor 3'),
        ('A4','Actor 4'),
        ('A5','Actor 5'),
        ('A6','Actor 6'),
        ('A7','Actor 7'),
        ('S','Speakers'),
        ('N1','Narator 1'),    
        ('N2','Narator 2'),                            
    )
    
    
    spoken_by = models.CharField(max_length=200, choices=CATEGORY)
    line_text = models.TextField()
    # Show  = models.ForeignKey(Show, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.spoken_by}: {self.line_text}'

    
class Show(models.Model):
    show_name = models.CharField(max_length=128)
    lines = models.ManyToManyField(Line)
    def __str__(self):
        return self.show_name
    