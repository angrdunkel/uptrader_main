from django.db import models
from django.utils.translation import gettext_lazy as _

class Menu(models.Model):
    name = models.CharField(
        _('name'),
        max_length = 128,
    )
    position = models.IntegerField(
        _('position'),
        default=1
    )
    active = models.BooleanField(
        _('active'), 
        default=True,        
    )
    created_at = models.DateTimeField(
        _('created at'), 
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menu')

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    menu = models.ForeignKey(
        _('menu'),
        Menu,
    )
    parent = models.ForeignKey(
        'self',
        _('parent'),
        related_name = u'child',
        blank = True,
        null = True,
    )
    name = models.CharField(
        _('name'),
        max_length = 150,
    )
    uri = models.SlugField(
        _('URL'),
        help_text = _('If you do not want to connect this item to your models, you can specify a URL explicitly'),
        blank = True,
        null = True,
    )
    active = models.BooleanField(
        _('Active'), 
        default=True,        
    )
    css_class = models.CharField(
        _('CSS class'),
        max_length = 50,
        help_text = u'',
        blank = True,
        null = True,
    )
    
    class Meta:
        verbose_name = _('Menu item')
        verbose_name_plural = _('Menu items')
    
    def get_absolute_url(self):
        return '/%s' % self.uri
    
    def __str__(self):
        return self.name