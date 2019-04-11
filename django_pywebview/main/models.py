from django.db import models
import os
import random
from django.utils.translation import gettext_lazy as _



def get_category_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
    



def category_upload_image_path(instance,filename):
    new_filename = random.randint(1,1234567890)
    name,ext = get_category_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "categories_images_uploads/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )



class Category(models.Model):
    """
    A product category. Merely used for navigational purposes; has no
    effects on business logic.
    """
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    slug = models.SlugField(_("Slug"),max_length=128, blank=True,unique=True)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Image'), upload_to=category_upload_image_path, blank=True,
                              null=True, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['-timestamp']

    def __str__(self):
        return self.name