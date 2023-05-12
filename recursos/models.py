from django.db import models

from wagtail.models import Page
from wagtail.core.models import Page, Orderable
from wagtail.core.blocks import URLBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core import blocks 
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms
 
 
@register_snippet
class categorias(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='CATEGORIA', help_text=u'¡¡Importante!! -- NO APLICAR ACENTOS A LOS TIPOS DE DOCUMENTOS')

    panels = [
        FieldPanel('nombre'),
    ]

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'CATEGORÍAS'
        
        
@register_snippet
class areas(models.Model):
    codigo = models.CharField(max_length=16, verbose_name='CÓDIGO')
    area = models.CharField(max_length=128, verbose_name='ÁREAS DE CONOCIMIENTO')
    imagen_portada = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN DE PORTADA', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)

    panels = [
        FieldPanel('codigo'),
        FieldPanel('area'),
        FieldPanel('imagen_portada'),
        
    ]

    def __str__(self):
        return self.area

    class Meta:
        verbose_name_plural = 'ÁREAS DE CONOCIMIENTO'


       


@register_snippet
class nivel_academico(models.Model):
    nivel_academico = models.CharField(max_length=128, verbose_name='NIVEL ACADEMICO')

    panels = [
        FieldPanel('nivel_academico')
    ]

    def __str__(self):
        return self.nivel_academico

    class Meta:
        verbose_name_plural = 'NIVEL ACADEMICO'


@register_snippet
class grados(models.Model):
    codigo =  models.CharField(max_length=255, verbose_name='CÓDIGO')
    nombre = models.CharField(max_length=255, verbose_name='NOMBRE')
    nivel_academico = models.ForeignKey('recursos.nivel_academico', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='NIVEL ACADEMICO')
    
    panels = [
        FieldPanel('codigo'),
        FieldPanel('nombre'),
        FieldPanel('nivel_academico'),
    ]

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'GRADOS'
  
@register_snippet
class clases(models.Model):
    codigo =  models.CharField(max_length=255, verbose_name='CÓDIGO')
    nombre = models.CharField(max_length=255, verbose_name='NOMBRE DE LA CLASE')
    area =  models.ForeignKey('recursos.areas', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='ÁREA DE CONOCIMIENTO')
    grado = models.ManyToManyField('recursos.grados',blank=True,  verbose_name='SELECCIONE EL O LOS GRADOS A LOS QUE PERTENECE LA CLASE :')
    icono_1 = models.ForeignKey('wagtailimages.Image', verbose_name='ICONO ALUMNO', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    icono_2 = models.ForeignKey('wagtailimages.Image', verbose_name='ICONO DOCENTE', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    icono_3 = models.ForeignKey('wagtailimages.Image', verbose_name='ICONO PADRE', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
   
   
    panels = [
        FieldPanel('codigo'),
        FieldPanel('nombre'),
        FieldPanel('area'),
        FieldPanel('grado', widget=forms.CheckboxSelectMultiple),
        FieldPanel('icono_1'),
        FieldPanel('icono_2'),
        FieldPanel('icono_3')
    ]

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'CLASES' 
class RepositoriosIndexPage(Page):
    pass 

class RepositoriosIndexPagePage(Orderable):
    page = ParentalKey(RepositoriosIndexPage, related_name='repositorios_index')
    title = models.CharField(max_length=300,blank=True, null=True, verbose_name='DESCRIPCIÓN BREVE')
    panels = [
            FieldPanel('title'), 
    ] 

class RepositorioPage(Page):
    OPCIONES_DIRIGIDO_A= (
        ('1','ALUMNOS' ),
        ('2','DOCENTES'),
        ('3','PADRES DE FAMILIA'),
        ('4','TODOS')
    )
     
    titulo = models.TextField(blank=True, null=True, verbose_name='TITULO DEL REPOSITORIO :')
    descripcion= RichTextField(blank=True, null=True, verbose_name='DESCRIPCION DEL REPOSITORIO : ')
    visitas =  models.CharField(verbose_name=u"VISITAS",blank= True, null= True, max_length = 300)
    me_gusta =  models.CharField(verbose_name=u"ME GUSTA",blank= True, null= True,  max_length = 300)
    no_megusta =  models.CharField(verbose_name=u"NO ME GUSTA",blank= True, null= True,  max_length = 300)
    grados = models.ForeignKey('recursos.grados',blank=True,null=True, on_delete=models.SET_NULL,  verbose_name='SELECCIONE EL GRADO:')
    dirigido_a = models.CharField(max_length = 14, choices=OPCIONES_DIRIGIDO_A)
    imagen_portada = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN DE PORTADA', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
   
    content_panels = Page.content_panels + [
        FieldPanel('titulo'),
        FieldPanel('descripcion'),
        FieldPanel('grados'),
        FieldPanel('imagen_portada'), 
        FieldPanel('dirigido_a'),
        InlinePanel('repositorio_recursos',heading="RECURSO  DEL REPOSITORIO :", label="RECURSOS"),
    ]
    parent_page_types = ['RepositoriosIndexPage']
    
class RepositorioPageDatos(Orderable):
    OPCIONES_FUENTE= (
        ('oficial','OFICIAL' ),
        ('no_oficial','NO OFICIAL'),
    )
    
   
    
    OPCIONES_MES= (
        ('1','ENERO' ),
        ('2','FEBRERO'),
        ('3','MARZO'),
        ('4','ABRIL'),
        ('5','MAYO'),
        ('6','JUNIO'),
        ('7','JULIO'),
        ('8','AGOSTO'),
        ('9','SEPTIEMBRE'),
        ('10','OCTUBRE'),
        ('11','NOVIEMBRE'),
        ('12','DICIEMBRE')    
        
    )
    nombre = models.TextField(blank=True, null=True, verbose_name='NOMBRE DEL RECURSO :')
    descripcion= RichTextField(blank=True, null=True, verbose_name='DESCRIPCION DEL RECURSO: ')
    page = ParentalKey(RepositorioPage, related_name='repositorio_recursos')
    categoria = models.ForeignKey('recursos.categorias', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='CATEGORÍA')
    palabra_clave = models.TextField(blank=True, null=True, verbose_name='PALABRA CLAVE')
    clase  = models.ForeignKey('recursos.clases', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='CLASES')
    fuente = models.CharField(max_length = 10, choices=OPCIONES_FUENTE)
    mes = models.CharField(max_length = 10, choices=OPCIONES_MES)
    macromedia = models.FileField(upload_to='repocitorios/macromedia/%Y/%m/%d/', null=True, blank=True, verbose_name="ARCHIVOS MACROMEDIA", help_text=u'¡¡Importante!! -- SOLO ARCHIVOS COMPRIMIDOS FORMATO .RAR')
    video = models.FileField(upload_to='videos/%Y/%m/%d/', null=True, blank=True, verbose_name="VIDEOS", help_text=u'¡¡Importante!! -- SOLO DOCUMENTOS FORMATO VIDEO')
    pdf = models.FileField(upload_to='documentos/recursos', verbose_name="ARCHIVO DE PDF", null=True, blank=True, help_text=u'¡¡Importante!! -- SOLO DOCUMENTOS FORMATOS PDF')
    imagen = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data =  StreamField([
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    activo = models.BooleanField(default=True)
 
   
    content_panels = Page.content_panels + [
        FieldPanel('categoria'),
        FieldPanel('palabra_clave'),
        FieldPanel('clase'),
        FieldPanel('fuente'),
        FieldPanel('mes'),
        FieldPanel('macromedia'),
        FieldPanel('video'),
        FieldPanel('pdf'),
        FieldPanel('imagen'),
        FieldPanel('data'),
        FieldPanel('activo'),
    ]

 
class RecursosPage(Page):
    OPCIONES_FUENTE= (
        ('oficial','OFICIAL' ),
        ('no_oficial','NO OFICIAL'),
    )
    
    OPCIONES_DIRIGIDO_A= (
        ('1','ALUMNOS' ),
        ('2','DOCENTES'),
        ('3','PADRES DE FAMILIA'),
        ('4','TODOS')
    )
    
    OPCIONES_MES= (
        ('1','ENERO' ),
        ('2','FEBRERO'),
        ('3','MARZO'),
        ('4','ABRIL'),
        ('5','MAYO'),
        ('6','JUNIO'),
        ('7','JULIO'),
        ('8','AGOSTO'),
        ('9','SEPTIEMBRE'),
        ('10','OCTUBRE'),
        ('11','NOVIEMBRE'),
        ('12','DICIEMBRE')    
        
    )
    titulo = models.TextField(blank=True, null=True, verbose_name='TITULO :')
    descripcion= RichTextField(blank=True, null=True, verbose_name='DESCRIPCION DEL RECURSO : ')
    visitas =  models.CharField(verbose_name=u"VISITAS",blank= True, null= True, max_length = 300)
    me_gusta =  models.CharField(verbose_name=u"ME GUSTA",blank= True, null= True,  max_length = 300)
    no_megusta =  models.CharField(verbose_name=u"NO ME GUSTA",blank= True, null= True,  max_length = 300)
    grados = ParentalManyToManyField('recursos.grados',blank=True,  verbose_name='SELECCIONE LOS GRADOS A LOS QUE PERTENECE El RECURSO:')
    categoria = models.ForeignKey('recursos.categorias', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='CATEGORÍA')
    palabra_clave = models.TextField(blank=True, null=True, verbose_name='PALABRA CLAVE')
    clase  = models.ForeignKey('recursos.clases', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='CLASES')
    fuente = models.CharField(max_length = 10, choices=OPCIONES_FUENTE)
    dirigido_a = models.CharField(max_length = 14, choices=OPCIONES_DIRIGIDO_A)
    mes = models.CharField(max_length = 10, choices=OPCIONES_MES)
    macromedia = models.FileField(upload_to='repocitorios/macromedia/%Y/%m/%d/', null=True, blank=True, verbose_name="ARCHIVOS MACROMEDIA", help_text=u'¡¡Importante!! -- SOLO ARCHIVOS COMPRIMIDOS FORMATO .RAR')
    video = models.FileField(upload_to='videos/%Y/%m/%d/', null=True, blank=True, verbose_name="VIDEOS", help_text=u'¡¡Importante!! -- SOLO DOCUMENTOS FORMATO VIDEO')
    pdf = models.FileField(upload_to='documentos/recursos', verbose_name="ARCHIVO DE PDF", null=True, blank=True, help_text=u'¡¡Importante!! -- SOLO DOCUMENTOS FORMATOS PDF')
    imagen = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data =  StreamField([
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    activo = models.BooleanField(default=True)
    imagen_portada = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN PORTADA', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
 
   
    content_panels = Page.content_panels + [
        FieldPanel('titulo'),
        FieldPanel('descripcion'),
        FieldPanel('categoria'),
        FieldPanel('palabra_clave'),
        FieldPanel('clase'),
        FieldPanel('grados', widget=forms.CheckboxSelectMultiple),
        FieldPanel('fuente'),
        FieldPanel('dirigido_a'),
        FieldPanel('mes'),
        FieldPanel('macromedia'),
        FieldPanel('video'),
        FieldPanel('pdf'),
        FieldPanel('imagen'),
        FieldPanel('data'),
        FieldPanel('activo'),
        FieldPanel('imagen_portada'),
    ]
    parent_page_types = ['RepositoriosIndexPage']
    


