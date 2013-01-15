from django.db import models
from django.template.defaultfilters import slugify
from django.core.files import File
from django.db.models.fields.related import ForeignKey

CATEGORY_OPT = (
        (u'GEN', u'General'),
        (u'VIS', u'Visualization'),
        (u'RNA', u'Screening'),
        (u'SEQ', u'Sequencing'),
    )

class Rscripts(models.Model):
    name = models.CharField(max_length=15, unique=True)
    inln = models.CharField(max_length=75)
    details = models.CharField(max_length=350)
    categoty = models.CharField(max_length=3, choices=CATEGORY_OPT)

    def file_name(self, filename):
        fname, dot, extension = filename.rpartition('.')
        slug = slugify(self.name)
        return 'r_scripts/%s/%s.%s' % (slug, slug, extension)

    docxml = models.FileField(upload_to=file_name)
    code = models.FileField(upload_to=file_name)
    logo = models.FileField(upload_to=file_name)

    def __unicode__(self):
        return self.name


class Jobs(models.Model):
    jname = models.CharField(max_length=55)  # , unique=True)
    script = ForeignKey(Rscripts)
    # status may be changed to NUMVER later
    status = models.CharField(max_length=15)

    def file_name(self, filename):
        fname, dot, extension = filename.rpartition('.')
        slug = slugify(self.jname)
        return 'jobs/%s/%s.%s' % (slug, slug, extension)

    docxml = models.FileField(upload_to=file_name)

    def __unicode__(self):
        return self.jname
