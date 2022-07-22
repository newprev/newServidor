from django.db import models
from django.utils.timezone import now


class SyncIpca(models.Model):
    # db_table = 'syncIpca'

    syncId = models.AutoField(primary_key=True, unique=True, blank=False, auto_created=True)
    dataSync = models.DateTimeField(default=now, blank=False, null=False)
    qtdSync = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'SyncIpca'

    def __str__(self):
        return f"syncId: {self.syncId}, dataSync: {self.dataSync}, qtdSync: {self.qtdSync}"
