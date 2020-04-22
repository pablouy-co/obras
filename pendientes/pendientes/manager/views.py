import xlwt
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from  tablib import Dataset
from .models import WorkSheet
from .forms import WorkSheetForm, UpdateWorkForm


@login_required
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales

    num_works = WorkSheet.objects.all().count() #Todas las obras ingresadas  
    num_only_cs = WorkSheet.objects.filter(pendings_date__exact=None).count()   #solo CS   
    num_pend_to_send = WorkSheet.objects.filter(                                #pendientes a enviar por Ericsson
        ~Q(pendings_date = None) & Q(ca_date = None)
        ).count()
    num_pend_sent = WorkSheet.objects.filter(                                   #pendientes enviados a Antel (sin respuesta y estan del lado de Antel)
        ~Q(pendings_date = None) & ~Q(ca_date = None) & Q(closed = 'n') & Q(pend_side = 'a')
        ).count()
    num_pend_sent_nr = WorkSheet.objects.filter(                                   #pendientes enviados a Antel y volvieron (cancha de Ericsson)
        ~Q(pendings_date = None) & ~Q(ca_date = None) & Q(closed = 'n') & Q(pend_side = 'e')
        ).count()
    num_type_pend_az = WorkSheet.objects.filter(                                #pendientes de AZ tool
        Q(pend_type__pend_type__contains = 'AZ tool') & Q(closed = 'n') & Q(ca_date = None)
    ).count()
    num_type_pend_doc = WorkSheet.objects.filter(                               #pendientes de documentacion
        Q(pend_type__pend_type__contains = 'Documentacion') & Q(closed = 'n') & Q(ca_date = None)
    ).count()
    num_type_pend_pics = WorkSheet.objects.filter(                              #pendientes de fotos en servidor
        Q(pend_type__pend_type__contains = 'Fotos en servidor') & Q(closed = 'n') & Q(ca_date = None)
    ).count()
    num_type_pend_instal = WorkSheet.objects.filter(                              #pendientes de instalacion
        Q(pend_type__pend_type__contains = 'Instalacion') & Q(closed = 'n') & Q(ca_date = None)
    ).count()
   
 

    return render(
        request,
        'index.html',
        context={
            'num_works':num_works,
            'num_only_cs':num_only_cs,
            'num_pend_to_send':num_pend_to_send,
            'num_pend_sent':num_pend_sent,
            'num_type_pend_az':num_type_pend_az,
            'num_type_pend_doc':num_type_pend_doc,
            'num_type_pend_pics':num_type_pend_pics,
            'num_type_pend_instal':num_type_pend_instal,
            'num_pend_sent_nr':num_pend_sent_nr,
            }
    )

'''-------------------------------------------------------------------------VISTAS-------------------------------------------------------------------------------'''

#Detalle de la obra (worksheet_detail.html)
class ViewWorkDetail(generic.DetailView):
    model = WorkSheet

#Buscado de obras (LoginRequiredMixin,worksheet_list.html)
class SearchWork(generic.ListView):             
    model = WorkSheet
    #paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query != None:
            object_list = WorkSheet.objects.filter(
                Q(site__icontains=query) | Q(oppera__icontains=query)
            )
            return object_list


#Muestra solo los que tienen CS enviados (worksheet_list.html)
@login_required
def onlycs(request):

    title = 'Conformes supervisor enviados (Antel no visitó)'
    filter = WorkSheet.objects.filter(
            pendings_date__exact=None
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestra los que tienen pendientes a enviar por Ericsson (worksheet_list.html)
@login_required
def pendtosend(request):

    title = 'Obras con pendientes a enviar por Ericsson'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & Q(ca_date = None)
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestro los que tienen pendientes enviados a Antel y no han sido contestados por Antel (pend_side = 'a')(worksheet_list.html)
@login_required
def pendcontested(request):

    title = 'Obras con pendientes, solucionados y enviados a Antel, pero no han contestado'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & ~Q(ca_date = None) & Q(closed = 'n') & Q(pend_side = 'a')
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestro los que tienen pendientes enviados a Antel, volvieron, y Ericsson tiene que voler a responder (pend_side = 'e')(worksheet_list.html)
@login_required
def pendcontestedNR(request):

    title = 'Obras con pendientes enviados a Antel y devueltos (Ericsson debe replicar)'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & ~Q(ca_date = None) & Q(closed = 'n') & Q(pend_side = 'e')
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestro los que tienen pendientes AZ tool (worksheet_list.html)
@login_required
def pendaztool(request):

    title = 'Obras con pendientes de AZ tool'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & Q(ca_date = None) & Q(closed = 'n') & Q(pend_type = 1)
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestro los que tienen pendientes de instalacion (worksheet_list.html)
@login_required
def pendinstall(request):

    title = 'Obras con pendientes de instalacion'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & Q(ca_date = None) & Q(closed = 'n') & Q(pend_type = 2)
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestro los que tienen pendientes de documentacion (worksheet_list.html)
@login_required
def penddoc(request):

    title = 'Obras con pendientes de documentacion'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & Q(ca_date = None) & Q(closed = 'n') & Q(pend_type = 3)
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )

#Muestro los que tienen pendientes de fotos a servidor (worksheet_list.html)
@login_required
def pendpic(request):

    title = 'Obras con pendientes de documentacion'
    filter = WorkSheet.objects.filter(
            ~Q(pendings_date = None) & Q(ca_date = None) & Q(closed = 'n') & Q(pend_type = 5)
        )
    
    return render(
        request,
        'manager/worksheet_list.html',
        context = {
            'filter':filter,
            'title':title,
        }
    )


'''--------------------------------------------------------------CREAR, EDITAR, BORRAR----------------------------------------------------------------'''

#Crea nuevo CS
class AddPending(PermissionRequiredMixin,generic.CreateView):
    model = WorkSheet
    permission_required = 'manager.can_mark_returned'
    form_class = WorkSheetForm
    template_name = 'manager/cs_form.html'
    success_url = "/manager/workdetail/{id}"


#Edita una obra existente
class UpdateWork(PermissionRequiredMixin,generic.UpdateView):
    model = WorkSheet
    permission_required = 'manager.can_mark_returned'
    form_class = UpdateWorkForm
    template_name = 'manager/worksheet_form.html'
    success_url = "/manager/workdetail/{id}"

    
class DeleteWorkSheet(PermissionRequiredMixin,generic.DeleteView):
    model = WorkSheet
    permission_required = 'manager.can_mark_returned'
    success_url = "/manager/onlycs/"


'''------------------------------------------------------------------------EXPORT----------------------------------------------------------------------------'''
@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="listado de obras.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sites')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = [
        'Sigla', 'Oppera','Fecha CS','Comentarios CS','Fecha SA',
        'Fecha pendientes a ASP','ASP','Comentarios reclamo pendientes','Fecha CA','Comentarios CA','Fotos para Antel','Cerrado',
        ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows

    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'

    rows = WorkSheet.objects.all().values_list(
        'site', 'oppera','cs_date','cs_comments','pendings_date','claim_date','asp',
        'claim_pending_comments','ca_date','ca_comments','ca_pics_link','closed',
        )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], date_format)

    wb.save(response)
    return response
