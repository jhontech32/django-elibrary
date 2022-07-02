from django.db import models
from django.conf import settings

from PIL import Image
from io import BytesIO
from django.core.files import File

import os

# Create your models here.
class TblBook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    author = models.CharField(max_length=100, blank=False, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='uploads/')

    class Meta:
        managed = False
        db_table = 'tbl_book'

    # Image processing function
    def save(self):
        #self is model name ex: TblBook
        # Membuka image dari formdata
        im = Image.open(self.picture)

        print('ISI DARI IM', im)
        print('ISI DARI SelfPic', self.picture)

        # Uncomment for resize image uploaded
        # basewidth = 200
        # wpercent = basewidth / float(im.size[0])
        # hsize = im.size[1] * wpercent
        # size_f = (basewidth, int(hsize))
        # im = im.resize(size_f, Image.NEAREST)

        # Pengecekan file apakah sudah pernah ada atau belum
        if os.path.exists(settings.MEDIA_ROOT + 'uploads/' + self.picture.name):
            os.remove(settings.MEDIA_ROOT + 'uploads/' + self.picture.name)
            return super(TblBook, self).save()
        else:
            # Convert gambar sesuai dengan mode

            output = BytesIO()
            if im.mode == "JPEG":
                im.save(fp=output, format='JPEG', quality=95)
            elif im.mode in ["RGBA", "P"]:
                im = im.convert("RGB")
                im.save(fp=output, format='JPEG', quality=95)
            else:
                im.save(fp=output, format='JPEG', quality=95)
            self.picture = File(output, name=self.picture.name)
            return super(TblBook, self).save()

