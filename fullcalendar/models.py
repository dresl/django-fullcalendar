# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class CalendarEvent(models.Model):
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    description = models.TextField(_('Description'), blank=True, null=True)
    all_day = models.BooleanField(_('All day'), default=False)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.title
