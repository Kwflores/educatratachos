from django.shortcuts import render
from administracion.models import * 
from datetime import datetime


#----------GALERIA-------------------------------------#
def galeria_fd(request):
  dias = DayGaleriaPagePage.objects.all().values('page_ptr_id', 'descripcion', 'titulo', 'imagen1_id__file', 'data','fecha')
  print(dias)
  ctx = {'dias_destacados': dias}
  return render(request,'../templates/administracion/day_page.html', ctx)

#un dia como hoy 
def dia_destacado(request):
 #obtener la fecha actual en la variable now
  now = datetime.now()
 #se extrae el mes de la variable  now 
  month = now.strftime("%m")
 #se extrae el dia de la variable now
  day = now.strftime("%d")

  ctx = {
         'dias_destacados': DayGaleriaPagePage.objects.filter(fecha__month=month).filter(fecha__day=day).first(),
        }
  print(ctx)
  return render(request,'../templates/home/home_page.html', ctx)



  