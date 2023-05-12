from django.db import models
from wagtail.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks 
from wagtail.core.blocks import URLBlock
from wagtail.core.blocks import PageChooserBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from django.template.defaultfilters import date as _date
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from django.contrib.auth.models import User

from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
# Create your models here.
#articulo page 
class ArticuloPage(Page):
    imagen1 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #1', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    imagen2 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #2', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    imagen3 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #3', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    descripcion= RichTextField(blank=True, null=True, verbose_name='DESCRIPCION DEL ARTÍCULO')
    titulo= models.TextField(blank=True, null=True, verbose_name='TÍTULO DEL ARTÍCULO')
    
    data =  StreamField([
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
        FieldPanel('imagen1'),
        FieldPanel('imagen2'),
        FieldPanel('imagen3'),
        FieldPanel('titulo'),
        FieldPanel('descripcion'),
        FieldPanel(('data'), heading="Enlaces",
        classname="collapsible collapsed"),
        ], heading="DETALLES DE ARTÍCULO",
         classname="collapsible collapsed"), 
    ]

class ArticuloPagePage(Orderable):
    page = ParentalKey(ArticuloPage, related_name='Articulos')
    title = models.CharField(max_length=300,blank=True, null=True, verbose_name='DESCRIPCIÓN BREVE')
    panels = [
            FieldPanel('title'), 
    ] 


class AdministracionPage(Page):
    pass


#----------------------------- un dia como hoy---------------------------------------------------------#
class DayPage(Page):
   

    content_panels = Page.content_panels + [
        
        InlinePanel('day', label="SECCION DESTACADA"),
    ]



class DayGaleriaPage(Page):
    pass 

class DayGaleriaPagePage(Orderable):
    title = models.CharField(max_length=300,blank=True, null=True, verbose_name='DESCRIPCIÓN BREVE')
    page = ParentalKey(DayPage, related_name='day')
    imagen1 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN 1', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    descripcion= RichTextField(blank=True, null=True, verbose_name='DESCRIPCION DEL DIA')
    titulo= models.TextField(blank=True, null=True, verbose_name='TÍTULO DEL DIA')
    fecha = models.DateField("FECHA DESTACADA" , blank=True, null=True)
    likes = models.ManyToManyField(User, blank=True, default=None, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, default=None)

    data =  StreamField([
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)

    panels = [
        FieldPanel('title'), 
        MultiFieldPanel([
        FieldPanel('imagen1'),
        FieldPanel('titulo'),
        FieldPanel('descripcion'),
        FieldPanel('fecha'),
        FieldPanel(('data'), heading="Enlaces",
        classname="collapsible collapsed"),
        ], heading="DIA COMO HOY",
        classname="collapsible collapsed"),
    ] 


class NoticiasPage(Page):
    pass

class NoticiasPagePage(Orderable):
    page = ParentalKey(ArticuloPage, related_name='Noticias')
    title = models.CharField(max_length=300,blank=True, null=True, verbose_name='DESCRIPCIÓN BREVE')
    panels = [
            FieldPanel('title'), 
    ] 
