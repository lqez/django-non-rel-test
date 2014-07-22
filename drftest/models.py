from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class OtherInfo(models.Model):
    info_1 = models.CharField(max_length=200)
    info_2 = models.CharField(max_length=200)
    info_3 = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s %s' % (self.info_1, self.info_2, self.info_3)


class ModelInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    other_info = ListField(EmbeddedModelField(OtherInfo))

    def __unicode__(self):
        return u'%s %s' % (self.name, self.email)
