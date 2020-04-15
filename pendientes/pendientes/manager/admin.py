from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . import models
from .models import WorkSheet


class WorkSheetAdmin(admin.ModelAdmin):
    list_display = ('id','site','oppera','cs_date','pendings_date',)
    list_filter = ('cs_date','pendings_date','claim_date','asp','ca_date','pend_type',)

class PendTypeAdmin(admin.ModelAdmin):
    list_display = ('pend_type',)

admin.site.register(models.WorkSheet, WorkSheetAdmin)
admin.site.register(models.PendType, PendTypeAdmin)

'''@admin.register(models.WorkSheet)
class WorksheetAdmin(ImportExportModelAdmin):
    pass

class WorkSheetResource(resources.ModelResource):
    class Meta:
        model = WorkSheet'''