from django.db import models

# Create your models here.

class Line(models.Model):
    CATEGORY = (
        ('1','Actor 1'),
        ('2','Actor 2'),
        ('3','Actor 3'),
        ('4','Actor 4'),
        ('5','Actor 5'),
        ('6','Actor 6'),
        ('7','Actor 7'),
        ('s','Speakers'),
        ('n1','Narator 1'),    
        ('n2','Narator 2'),                            
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
    