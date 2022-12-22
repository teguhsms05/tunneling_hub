from django.db import models
import datetime

today = datetime.datetime.utcnow()+datetime.timedelta(hours=7)

# Create your models here.
class GroupDomain(models.Model): 
    group_domain = models.CharField(max_length=200, null=False)
    cpanel_domain = models.CharField(max_length=200, null=False)
    created_by = models.CharField(max_length=200)
    createdAt = models.DateTimeField(default=today)

    class Meta:
        db_table = 'domain_group'
