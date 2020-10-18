import os
import time

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import inch

from reportlab.graphics.shapes import Drawing, Rect, String, Group, Line
from reportlab.graphics.widgets.markers import makeMarker

from shutil import rmtree

doc = SimpleDocTemplate('GraficosWin.pdf', pagesize=A4)
story = []
estilo = getSampleStyleSheet()


gatos_dir='C:/Users/TRIGUN/Desktop/TrabajoWIN/garfield'
contenido=os.listdir(gatos_dir)
rmtree('C:/Users/TRIGUN/Desktop/TrabajoWIN/garfield_Procesado')
os.mkdir('C:/Users/TRIGUN/Desktop/TrabajoWIN/garfield_Procesado')
tim_to_gray=[]
tim_to_hist=[]
imgs=[]


for fichero in contenido:
    if os.path.isfile(os.path.join(gatos_dir,fichero)) and fichero.endswith('.jpg'):
        nombre=str(fichero)
        t0=time.time()        
        os.system('magick convert C:/Users/TRIGUN/Desktop/TrabajoWIN/garfield/'+nombre+ ' -colorspace gray C:/Users/TRIGUN/Desktop/TrabajoWIN/garfield_Procesado/F'+nombre)       
        t1=time.time()
        val=(t1-t0)
        tim_to_gray.append(round(val,2))
        imgs.append(fichero)
print('teminado conversion al Gray')
print('=============================')

for fichero in contenido:
        if os.path.isfile(os.path.join(gatos_dir,fichero)) and fichero.endswith('.jpg'):
                #imgs.append(fichero)
                nombre=str(fichero)
                t00=time.time()
                os.system('magick convert C:/Users/TRIGUN/Desktop/TrabajoWIN/garfield/'+nombre+' HISTOGRAM:-')
                t11=time.time()
                val=(t11-t00)
                tim_to_hist.append(round(val,2))

print('teminado calculo de histograma')
print('=============================')
print('Tiempos:',tim_to_gray)
print('=============================')
print('Tiempos:',tim_to_hist)
print('=============================')
print('Archivos:',imgs)

#

#EJEMPLO 06: Gráfico linear
#==========
from reportlab.graphics.charts.linecharts import HorizontalLineChart

titulo = Paragraph("PROCESOS REALIZADOS EN WINDOWS", estilo['title'])
story.append(titulo)
story.append(Spacer(0, inch*.20))

titulo = Paragraph("Tiempos de ejecución proceso conversión a escala de grises", estilo['title'])
story.append(titulo)
story.append(Spacer(0, inch*.1))

d = Drawing(400, 200)
lc = HorizontalLineChart()
lc.x = 30
lc.y = 50
lc.height = 125
lc.width = 350
#lc.data = [[0.7,0.1,0.5,0.2]]
datos=[]
datos.append(tim_to_gray)
lc.data = datos
lc.categoryAxis.categoryNames = imgs#lista de las imagenes
lc.categoryAxis.labels.boxAnchor = 'n'
lc.categoryAxis.labels.angle=90
lc.categoryAxis.labels.dy=-45
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 0.5     
lc.valueAxis.valueStep = 0.1  # Los pasos pueden ser tambien [10, 15, 30, 35, 40]
lc.lines[0].strokeWidth = 1
lc.lines[0].symbol = makeMarker('FilledCircle') # círculos rellenos
lc.lines[1].strokeWidth = 1.5
d.add(lc)
story.append(d)

#SEGUNDA GRAFICA
story.append(Spacer(0, inch*.50))#Es una esecie de salto de linea 
titulo = Paragraph("Tiempos de ejecución proceso calculo de histograma", estilo['title'])
story.append(titulo)
story.append(Spacer(0, inch*.1))

d = Drawing(400, 200)
lc = HorizontalLineChart()
lc.x = 30
lc.y = 50
lc.height = 125
lc.width = 350
#lc.data = [[0.7,0.1,0.5,0.2]]
datos=[]
datos.append(tim_to_hist)
lc.data = datos

lc.categoryAxis.categoryNames = imgs#lista de las imagenes
lc.categoryAxis.labels.boxAnchor = 'n'
lc.categoryAxis.labels.angle=90
lc.categoryAxis.labels.dy=-45
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 2
lc.valueAxis.valueStep = 0.5  # Los pasos pueden ser tambien [10, 15, 30, 35, 40]
lc.lines[0].strokeWidth = 1
lc.lines[0].symbol = makeMarker('FilledCircle') # círculos rellenos
lc.lines[1].strokeWidth = 1.5
d.add(lc)

story.append(d)

doc.build(story)


