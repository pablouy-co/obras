from django.db import models

class PendType(models.Model):
    pend_type = models.CharField(verbose_name = 'Tipo de pendiente', max_length = 50)

    def __str__(self):
        return self.pend_type

class WorkSheet(models.Model):
    site = models.CharField(verbose_name = 'Sigla', max_length = 12)
    oppera = models.CharField(verbose_name = 'No. Oppera', max_length =  10)
    cs_date = models.DateField(verbose_name = 'Fecha CS',null = True)
    cs_comments = models.CharField(verbose_name = 'Comentarios sobre CS', null = True , blank = True, max_length = 200)
    cs_pics_link = models.CharField(verbose_name = 'Fotos Supervision de obra', max_length = 200, null = True, blank = True)
    pendings_date = models.DateField(verbose_name = 'Fecha SA',null = True, blank = True)
    claim_date = models.DateField(verbose_name = 'Fecha reclamo pendientes',null = True, blank = True)
    asp = models.CharField(verbose_name = 'ASP responsable', max_length = 15, null = True , blank = True)
    claim_pending_comments = models.CharField(verbose_name = 'Cometarios sobre el reclamo a ASP', null = True , blank = True, max_length = 200)
    ca_date = models.DateField(verbose_name = 'Fecha CA',null = True, blank = True)
    ca_comments = models.CharField(verbose_name = 'Comentarios sobre CA', null = True , blank = True, max_length = 200)
    ca_pics_link = models.CharField(verbose_name = 'Fotos para servidor Antel', max_length = 200, null = True, blank = True)
    pend_type = models.ManyToManyField(PendType, verbose_name = 'Tipo de pendiente', blank = True)
    CLOSED = (
        ('s','Si'),
        ('n','No')
    )
    closed = models.CharField(max_length = 1, choices = CLOSED, blank = True, default = 'n', verbose_name = 'Obra cerrada')

    class Meta:
        ordering = ['oppera','site',]