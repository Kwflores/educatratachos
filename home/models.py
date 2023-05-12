from django.db import models

from wagtail.models import Page
from wagtail.core.models import Page, Orderable
from wagtail.core.blocks import URLBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core import blocks 
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from administracion.models import *
class HomePage(Page):
    imagen1 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #1', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_imagen1 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    imagen2 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #2', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_imagen2 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ], null=True, blank=True,)
    imagen3 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #3', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_imagen3 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ], null=True, blank=True,)
    imagen4 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #4', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_imagen4 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ], null=True, blank=True,)
    imagen5 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN #5', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_imagen5 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    imagen6 = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN UN DIA COMO HOY', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)


    sobre_nosotros =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('Nombre_Enlace1', blocks.TextBlock()),
        ('enlace_interno1', PageChooserBlock()),
        ('Nombre_Enlace2', blocks.TextBlock()),
        ('enlace_interno2', PageChooserBlock()),
        ('Nombre_Enlace3', blocks.TextBlock()),
        ('enlace_interno3', PageChooserBlock()),
        ('Nombre_Enlace4', blocks.TextBlock()),
        ('enlace_interno4', PageChooserBlock()),
        ('Nombre_Enlace5', blocks.TextBlock()),
        ('enlace_interno5', PageChooserBlock()),
    ])

    fecha_destacada =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
        
    ])

    # seccion de sitios externos
    banner1 = models.ForeignKey('wagtailimages.Image', verbose_name='BANNER #1', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_banner1 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    banner2 = models.ForeignKey('wagtailimages.Image', verbose_name='BANNER #2', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_banner2 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    banner3 = models.ForeignKey('wagtailimages.Image', verbose_name='BANNER #3', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_banner3 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    banner4 = models.ForeignKey('wagtailimages.Image', verbose_name='BANNER #4', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_banner4 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,)
    banner5 = models.ForeignKey('wagtailimages.Image', verbose_name='BANNER #5', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    data_banner5 =  StreamField([
        ('titulo', blocks.CharBlock(classname="full title")),
        ('descripcion', blocks.TextBlock()),
        ('enlace_externo', URLBlock()),
        ('enlace_interno', PageChooserBlock()),
    ],null=True, blank=True,) 


    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
        FieldPanel('imagen1'),
        FieldPanel(('data_imagen1'), heading="DETALLES DE IMAGEN 1",
        classname="collapsible collapsed"),
        FieldPanel('imagen2'),
        FieldPanel(('data_imagen2'), heading="DETALLES DE IMAGEN 2",
        classname="collapsible collapsed"),
        FieldPanel('imagen3'),
        FieldPanel(('data_imagen3'), heading="DETALLES DE IMAGEN 3",
        classname="collapsible collapsed"),
        FieldPanel('imagen4'),
        FieldPanel(('data_imagen4'), heading="DETALLES DE IMAGEN 4",
        classname="collapsible collapsed"),
        FieldPanel('imagen5'),
        FieldPanel(('data_imagen5'), heading="DETALLES DE IMAGEN 5",
         classname="collapsible collapsed"),
        ], heading="IMAGENES DE PRESENTACIÓN",
         classname="collapsible collapsed"),
        FieldPanel(('sobre_nosotros'), heading="SOBRE NOSOTROS",
         classname="collapsible collapsed"),
        FieldPanel(('fecha_destacada'), heading="UN DIA COMO HOY",
         classname="collapsible collapsed"),
        FieldPanel('imagen6'),

        #seccion de sitios externos
        MultiFieldPanel([
        FieldPanel('banner1'),
        FieldPanel(('data_banner1'), heading="DETALLES DE BANNER 1",
        classname="collapsible collapsed"),
        FieldPanel('banner2'),
        FieldPanel(('data_banner2'), heading="DETALLES DE BANNER 2",
        classname="collapsible collapsed"),
        FieldPanel('banner3'),
        FieldPanel(('data_banner3'), heading="DETALLES DE BANNER 3",
        classname="collapsible collapsed"),
        FieldPanel('banner4'),
        FieldPanel(('data_banner4'), heading="DETALLES DE BANNER 4",
        classname="collapsible collapsed"),
        FieldPanel('banner5'),
        FieldPanel(('data_banner5'), heading="DETALLES DE BANNER 5",
         classname="collapsible collapsed"),
        ], heading="COLABORADORES",
        classname="collapsible collapsed"),
        
    
     
    ]
    
    
class HomePagePage(Orderable):
        page = ParentalKey(HomePage, related_name='sec_destacadas')
        title = models.CharField(max_length=300,blank=True, null=True, verbose_name='DESCRIPCIÓN BREVE')
        page_interna = models.ForeignKey('wagtailcore.Page', verbose_name='PÁGINA INTERNA', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
        enlace_externo = models.URLField(verbose_name='ENLACE EXTERNO', max_length=800, blank=True, null=True)
        icon = models.ForeignKey('wagtailimages.Image', verbose_name='IMAGEN DEL ICONO', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
        
        panels = [
            FieldPanel('title'), 
            PageChooserPanel('page_interna'), 
            FieldPanel('enlace_externo'), 
            FieldPanel('icon'),
            
        ]


 