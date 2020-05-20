from browser import document, html, window, alert, timer
from  browser.html import *
"""
Script to create a canvas, load a picture and create a number of hightlight areas that produce a popup on mouseover.

The highlight areas are rectangles that invisibly overlay the image. When the mouse enters the highlight area
a popup appears over the area. The coordinates in he table below give the 
top left and bottom right of the overlay, relative to the coordinates of the underlying image. These are
converted to absolute coordinates by adding the XY coordinates of the image.

The mouse coordinates are displayed in the table for diagnostic purposes.

"""
cols=['name','topleft','bottomright','tooltip']
cvs= ((100,200),(680,500),'') # XY coordinates and dimesions of canvas

highlight = {
    'factory': ((427,100),(590,200),''),
    'tractor': ((345,231),(426,300),''),
    'bus': ((467,267),(666,380),''),
    'lorry':((275,340),(451,436),''),
    'car': ((71,336),(221,436),''),
    'house': ((0,200),(162,336),''),
    'trees': ((104,116),(269,210),''),
    'aircraft': ((8,16),(103,86),''),
}


def bib():
    canvasXY=cvs[0]
    bottomright=cvs[1]
    canvas = CANVAS(id="canvas",width = bottomright[0], height = bottomright[1])
    canvas.style={"position": "absolute", "left": str(canvasXY[0])+"px", "top": str(canvasXY[1])+"px" }    
    document <= canvas # this brython operator writes the canvas to the base document
    
    """ Cant work out how to load image into canvas with brython so drop into javascript here   """
    window.loadImage('canvas','traffic.png',bottomright[0],bottomright[1]) # keep these same as canvas dimensions
    for name,(topleft,bottomright,tooltip) in highlight.items(): 
        """ Create the individual highlight areas """
        c2 = CANVAS(id=name,width=bottomright[0]-topleft[0],height=bottomright[1]-topleft[1])
        c2.style={"position": "absolute", "left": str(topleft[0]+canvasXY[0])+"px", "top": str(topleft[1]+canvasXY[1])+"px" }
        ct2 = canvas.getContext('2d')
        document <= c2
        tooltip=DIV("This is a "+name,id="t"+name,Class="tooltiptext")
        tooltip.style={"position": "absolute", "left": str((topleft[0]+bottomright[0])/2+canvasXY[0])+"px", "top": str((topleft[1]+bottomright[1])/2+canvasXY[1])+"px","zIndex": 1,'visibility': 'hidden' }
        document <= tooltip
        
    """ Create a little table to display the mouse details.
        This is much more civilised than HTML or javascript.
    """
    table = TABLE()
    table <= TR(TD( H1("Mouse over image demo"),colspan=2)) 
    table <= TR(TD(DIV(id="trace3"))+TD(DIV(id="trace1")))
    
    """ Finally write the table to document """
    document <= table 
    
    """ Bind the mouse events to the individual highlight areas """
    for elt_id in highlight.keys():
        document[elt_id].bind('mouseenter', mouseenter)
        document[elt_id].bind('mouseleave', mouseleave)
    
    document["canvas"].bind("mousemove", mousemove)

""" mouse events """
def mousemove(ev):
    document["trace3"].text = f"coordinates : {ev.layerX}, {ev.layerY}"


def mouseenter(ev):
    document["trace1"].text = f'entering {ev.currentTarget.id}'
    document["t"+ev.currentTarget.id].style['visibility']='visible' # turn popup on 

def mouseleave(ev):
    document["trace1"].text = f'leaving {ev.currentTarget.id}'
    document["t"+ev.currentTarget.id].style['visibility']='hidden' # turn popup off

