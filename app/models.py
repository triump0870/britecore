"""Models for the ``app`` application."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from django.utils.text import slugify

FIELDCHOICES = (
    ('text', 'Text'),
    ('number', 'Number'),
    ('date', 'Date'),
    ('checkbox', 'Enum')
)


@python_2_unicode_compatible
class RiskField(models.Model):
    """
    Model to create custom information holders.

    :name: Name of the attribute.
    :description: Description of the attribute.
    :type: type of the db field

    """
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
    )

    slug = models.SlugField(
        max_length=50,
        blank=True, null=True
    )

    description = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name=_('Description'),
        help_text=_('Description for the risk field.')
    )

    type = models.CharField(
        max_length=50,
        choices=FIELDCHOICES,
        help_text=_('Field type choices')
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(RiskField, self).save(*args, **kwargs)


@python_2_unicode_compatible
class RiskType(models.Model):
    """
    Model to create risk template.

    :name: Name of the type.
    :description: Description of the type.
    :risk_fields: Custom fields for the risk template.

    """
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
    )
    description = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name=_('Description'),
    )

    risk_fields = models.ManyToManyField(
        'app.RiskField',
        verbose_name=_('Risk fields'),
        blank=True
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return '{0}'.format(self.name)


@python_2_unicode_compatible
class Risk(models.Model):
    """
    Model, which represents one single risk.
    
    :name: Name of the risk.
    :risk_type: Type of the risk.
    :description: Description of the risk.
    """
    name = models.CharField(max_length=50)

    description = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name=_('Description of the risk'),
    )

    risk_type = models.ForeignKey(
        'app.RiskType',
        verbose_name=_('Risk type'),
        related_name='risks',
    )

    data = JSONField(default='{]',
                     help_text=_('Data for the insurance. Default Null'),
                     blank=True, null=True)

    def __str__(self):
        return str(self.pk)
