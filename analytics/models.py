import os

from django.db import models
from django.utils.translation import gettext_lazy as _


def _performance_upload_to(instance, filename):
    date_part = f'{instance.received_on:%Y%m%d%H%M%S}'
    name, ext = os.path.splitext(filename)
    return f'performance/{name}_{date_part}{ext}'


class Performance(models.Model):
    received_on = models.DateTimeField(_("received on"))
    downloaded_on = models.DateTimeField(_("downloaded on"))
    worksheet = models.FileField(_("worksheet"), upload_to=_performance_upload_to)

    class Meta:
        db_table = "performance"
        verbose_name = _("performance")
        verbose_name_plural = _("performance")

    def __str__(self):
        return self.worksheet.name


class Forecast(models.Model):
    received_on = models.DateTimeField(_("received on"))
    downloaded_on = models.DateTimeField(_("downloaded on"))
    worksheet = models.FileField(_("worksheet"), upload_to="forecast")

    class Meta:
        db_table = "forecast"
        verbose_name = _("forecast")
        verbose_name_plural = _("forecast")

    def __str__(self):
        return self.worksheet.name


class PerformanceRow(models.Model):
    performance = models.ForeignKey(Performance, verbose_name=_("performance"), on_delete=models.CASCADE, related_name="rows")
    start_time = models.TimeField(_('start time'), null=True, blank=True)
    end_time = models.TimeField(_('end time'), null=True, blank=True)
    player = models.CharField(_('player'), max_length=32)
    metrics = models.CharField(_('metrics'), max_length=32, null=True, blank=True)
    abandoned_over_14 = models.IntegerField(_('abandoned over 14'), default=0)
    responses = models.IntegerField(_('responses'), default=0)
    short_calls = models.IntegerField(_('short calls'), default=0)
    login_time = models.IntegerField(_('login time'), default=0)
    login_time_nt = models.IntegerField(_('login time nt'), default=0)
    not_ready_time = models.IntegerField(_('not ready time'), default=0)
    wait_time = models.IntegerField(_('not ready time'), default=0)
    # ...
    managed = models.IntegerField(_('managed'), default=0)

    is_total = models.BooleanField(_('is total?'), default=False)

    class Meta:
        db_table = 'performance_rows'
        verbose_name = _('performance row')
        verbose_name_plural = _('performance rows')

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'
