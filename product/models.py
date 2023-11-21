from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name= _("parent"), blank= True, null= True, on_delete= models.CASCADE)
    title = models.CharField(_('name'), max_length = 50)
    description = models.TextField(_('description'), blank= True)
    avatar = models.ImageField(_('avatar'), blank= True, upload_to= 'categories/')
    is_enable = models.BooleanField(_('is enable'), default= True)
    created_time = models.DateTimeField(_('created time'), auto_now_add= True)
    updated_time = models.DateTimeField(_('update'), auto_now_add = True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('name'), max_length = 50)
    description = models.TextField(_('description'), blank= True)
    avatar = models.ImageField(_('avatar'), blank= True, upload_to= 'products/')
    categories = models.ManyToManyField('Category', verbose_name= _('categories'), blank= True)
    is_enable = models.BooleanField(_('is enable'), default= True)
    created_time = models.DateTimeField(_('created time'), auto_now_add= True)
    updated_time = models.DateTimeField(_('update'), auto_now_add = True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title



class File(models.Model):

    AUDIO_TYPE = 1
    VIDEO_TYPE = 2
    PDF_TYPE = 3
    FILE_TYPE = (
        (AUDIO_TYPE, _('audio')),
        (VIDEO_TYPE, _('video')),
        (PDF_TYPE, _('pdf'))
    )


    product = models.ForeignKey('Product', verbose_name= _('product'), on_delete= models.CASCADE)
    title = models.CharField(_('name'), max_length = 50)
    description = models.TextField(_('description'), blank= True)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices= FILE_TYPE, default= 2)
    file = models.FileField(_('file'), upload_to= 'files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'), default= True)
    created_time = models.DateTimeField(_('created time'), auto_now_add= True)
    updated_time = models.DateTimeField(_('update'), auto_now_add = True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('fils')

    def __str__(self):
        return self.title
