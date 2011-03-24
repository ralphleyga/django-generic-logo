import os.path

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from imagekit.models import ImageModel
from django.conf import settings


try:
    from PIL import Image
except ImportError:
    import Image


def photo_file_path(instance=None, filename=None, user=None):
    return os.path.join('glogo', filename)

class Glogo(ImageModel):
    image = models.ImageField(upload_to=photo_file_path)
    date_added = models.DateTimeField(editable=False, \
                                        auto_now_add=True)
    is_primary = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    user = models.ForeignKey(User)
    
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = settings.GLOGO_SPECS
        cache_dir = 'glogo'
        image_field = 'image'
        save_count_as = 'num_views'
