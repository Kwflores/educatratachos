from itertools import groupby
from django.http import JsonResponse
from django.db.models import Count
from django.shortcuts import render
from django.db.models import Sum
import zipfile
from zipfile import ZipFile
from recursos.models import *
from django.db.models import F
# Create your views here.
def nivelacademico(request,id_dirigido):
        nc = nivel_academico.objects.all() 
        grado = grados.objects.all()
        clase = clases.objects.all()
        recursos_data = list(RecursosPage.objects.filter(dirigido_a = id_dirigido).values('page_ptr_id','dirigido_a', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id', 'imagen_portada_id__file', 'grados','grados__nivel_academico__nivel_academico').annotate(grados_id=F('grados'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
        repositorios = list(RepositorioPage.objects.values('page_ptr_id', 'dirigido_a','titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id', 'grados_id__nivel_academico','grados_id__nivel_academico__nivel_academico').filter(dirigido_a = id_dirigido))
        print(repositorios + recursos_data)
        ctx = {'nivel_academico': nc,'grados': grado,'clases': clase,'repositorio': repositorios + recursos_data}
        return render(request,'../templates/recursos/repositorios_index_page.html', ctx)

def repositorios(request, id_dirigido,id_nivel,id_clase,id_grado):
        if id_dirigido and id_nivel == 0 and id_clase == 0 and id_grado == 0:
            repositorio = list(RepositorioPage.objects.values('page_ptr_id', 'dirigido_a','titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id','grados__nivel_academico_id','grados__nivel_academico__nivel_academico').filter(dirigido_a = id_dirigido))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido).values('page_ptr_id','dirigido_a', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados','grados__nivel_academico_id','grados__nivel_academico__nivel_academico').annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success1",'repositorio': data}
            else: 
                data ={'message': "+Not Found1"}
            return JsonResponse(data)
        elif id_nivel  != 0  and id_dirigido != 0 and id_clase != 0 and id_grado == 0:
            repositorio = list(RepositorioPage.objects.filter(dirigido_a = id_dirigido,grados_id__nivel_academico = id_nivel, grados__clases = id_clase).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id','grados__clases','grados__nivel_academico_id','grados__nivel_academico__nivel_academico'))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido,grados__nivel_academico_id=id_nivel,clase_id = id_clase).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados__nivel_academico_id','grados__nivel_academico__nivel_academico','grados').annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico=F('grados__nivel_academico_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success2",'repositorio': data}
            else: 
                data ={'message': "Not Found2"}
            return JsonResponse(data)
        elif id_clase and id_dirigido != 0 and id_nivel == 0 and id_grado == 0:
            repositorio = list(RepositorioPage.objects.filter(dirigido_a = id_dirigido, grados__clases = id_clase ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id', 'grados__nivel_academico_id','grados__nivel_academico__nivel_academico'))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido,  clase_id = id_clase ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados__nivel_academico_id','grados__nivel_academico__nivel_academico','grados').annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico=F('grados__nivel_academico_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success3",'repositorio': data}
            else: 
                data ={'message': "Not Found3"}
            return JsonResponse(data)
        elif id_grado and id_dirigido != 0 and id_clase == 0 and id_nivel == 0 :
            repositorio = list(RepositorioPage.objects.filter(dirigido_a= id_dirigido, grados_id = id_grado ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id', 'grados_id__nivel_academico','grados_id__nivel_academico__nivel_academico'))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido,grados = id_grado ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados__nivel_academico_id','grados__nivel_academico__nivel_academico',).annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico=F('grados__nivel_academico_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success4",'repositorio': data}
            else: 
                data ={'message': "Not Found4"}
            return JsonResponse(data)
        elif id_dirigido != 0 and id_nivel != 0 and id_clase != 0 and id_grado != 0:
            repositorio = list(RepositorioPage.objects.filter(dirigido_a = id_dirigido, grados_id__nivel_academico = id_nivel, grados__clases = id_clase, grados_id = id_grado ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id', 'grados_id__nivel_academico','grados_id__nivel_academico__nivel_academico'))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido,grados__nivel_academico_id=id_nivel, clase_id = id_clase, grados = id_grado ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados__nivel_academico_id','grados__nivel_academico__nivel_academico','grados').annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico=F('grados__nivel_academico_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success5",'repositorio': data}
            else: 
                data ={'message': "Not Found5"}
            return JsonResponse(data)
        if  id_dirigido != 0  and id_nivel != 0:
            repositorio = list(RepositorioPage.objects.values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id', 'grados_id__nivel_academico','grados_id__nivel_academico__nivel_academico').filter(dirigido_a = id_dirigido, grados_id__nivel_academico = id_nivel))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido,grados__nivel_academico_id=id_nivel).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados__nivel_academico_id','grados__nivel_academico__nivel_academico','grados').annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico=F('grados__nivel_academico_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success6",'repositorio': data}
            else: 
                data ={'message': "Not Found6"}
            return JsonResponse(data)
        if  id_dirigido != 0  and  id_clase != 0 and id_grado != 0:
            repositorio = list(RepositorioPage.objects.filter(dirigido_a = id_dirigido,grados__clases = id_clase, grados_id = id_grado ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'me_gusta', 'no_megusta', 'imagen_portada_id__file','grados_id', 'grados_id__nivel_academico','grados_id__nivel_academico__nivel_academico'))
            recursos = list(RecursosPage.objects.filter(dirigido_a = id_dirigido, clase_id = id_clase, grados = id_grado ).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','grados__nivel_academico_id','grados__nivel_academico__nivel_academico','grados').annotate(grados_id=F('grados'),nombre=F('titulo'),id=F('page_ptr_id'),grados_id__nivel_academico=F('grados__nivel_academico_id'),grados_id__nivel_academico__nivel_academico=F('grados__nivel_academico__nivel_academico')))
            data = repositorio + recursos
            if(len(data)>0):
                data={'message':"success7",'repositorio': data}
            else: 
                data ={'message': "Not Found6"}
            return JsonResponse(data)
        
def repositorio_detalle(request, id_repositorio):
        repositorios = list(RepositorioPageDatos.objects.filter(page_id=id_repositorio))
        data_repositorio = RepositorioPageDatos.objects.filter(page_id__page_ptr_id=id_repositorio).values('page_id__page_ptr_id','page_id__titulo','page_id__descripcion','page_id__imagen_portada_id__file','page_id__grados_id__nombre','page_id__grados__nivel_academico__nivel_academico').first()
        recursos_data = list(RecursosPage.objects.filter(page_ptr_id=id_repositorio))
        recursos = list(RecursosPage.objects.filter(page_ptr_id=id_repositorio).values('page_ptr_id', 'titulo', 'descripcion', 'visitas', 'clase_id', 'imagen_id__file', 'imagen_portada_id__file','macromedia','video','pdf','data').annotate(nombre=F('titulo'),id=F('page_ptr_id')))
        repositorio =  list(RepositorioPageDatos.objects.filter(page_id = id_repositorio).values('id','macromedia','video','pdf','page_id','page_id','descripcion', 'nombre','data'))
        print(recursos + repositorio)
        for r in repositorios:
             
            if r.macromedia != '':
                with zipfile.ZipFile( r.macromedia, 'r') as zip_ref:
                        zip_ref.extractall('media/repositorio/macromedia/'+ str(r.id) )
            break
        for r in recursos_data:
           
            if  r.macromedia != '':
                with zipfile.ZipFile( r.macromedia, 'r') as zip_r:
                        zip_r.extractall('media/repositorio/macromedia/'+ str(r.id) )
        
        
        ctx = { "repositorio" : recursos + repositorio, "data_repositorio" : data_repositorio }
        
        return render(request,'../templates/recursos/detalle_recurso.html',ctx)
                
         
        
        if(len(repositorio)>0):
                data={'message': "success",'repositorio':{'data': extract_Archivo}}
        else: 
                data ={'message': "+Not Found1"}
        return JsonResponse(data)
            
        
    
   
    
        
    
def grados_academicos(request, id, id_grado ):
    if id != 0 and  id_grado == 0:
        grado = list(grados.objects.filter(nivel_academico_id = str(id)).values())
        clase = list(clases.objects.values('id','nombre','grado')) 
        if(len(grado)>0):
            data={'grados': grado,'clase':clase }
        else: 
                data ={'message1': "Not Found"}
        return JsonResponse(data)   
         
        
    
    else:
        grado = list(grados.objects.values())
        print(grado)
        if id_grado:
            clase = list(clases.objects.filter(grado = id_grado).annotate(dcount=Count('nombre')).values('id','nombre','grado'))
        
        else:
            clase = list(clases.objects.values('id','nombre','grado')) 
            
        if(len(clase)>0):
                data={'grados':grado,'clases': clase }
        else: 
                data ={'message': "Not Found"}
        return JsonResponse(data)
 
      
          
     
           
          
      
      
      
 
      