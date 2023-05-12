from django.shortcuts import render
from administracion.models import * 
from django.views.generic import TemplateView
from datetime import datetime

def fecha_destacada(request):
  dias = DayGaleriaPagePage.objects.all().values('id','data', 'descripcion', 'imagen1_id__file', 'titulo','fecha')
  #print(dias)
  ctx = {'dias_destacados': dias}
  return render(request,'../templates/administracion/day_page.html', ctx)



# Create your views here.
def galeria_noticias(request):
  articulos = ArticuloPage.objects.all().values('page_ptr_id__slug','page_ptr_id__id','page_ptr_id', 'descripcion', 'titulo', 'imagen1_id__file', 'data')
  #noticias = ArticuloPage.objects.all().order_by('-titulo').values()
  #print(noticias)
  ctx = {'articulos_noticias': articulos}
  return render(request,'../templates/administracion/noticias_page.html',ctx)



