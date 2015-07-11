'''
Created on Jul 11, 2015

@author: Patrick
'''
import bpy
import bgl
import blf

def draw3d_polyline(context, points, color, thickness, LINE_TYPE):
    if LINE_TYPE == "GL_LINE_STIPPLE":
        bgl.glLineStipple(4, 0x5555)  #play with this later
        bgl.glEnable(bgl.GL_LINE_STIPPLE)  
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(*color)
    bgl.glLineWidth(thickness)
    bgl.glDepthRange(0.0, 0.997)
    bgl.glBegin(bgl.GL_LINE_STRIP)
    for coord in points: bgl.glVertex3f(*coord)
    bgl.glEnd()
    bgl.glLineWidth(1)
    if LINE_TYPE == "GL_LINE_STIPPLE":
        bgl.glDisable(bgl.GL_LINE_STIPPLE)
        bgl.glEnable(bgl.GL_BLEND)  # back to uninterrupted lines  

def draw3d_closed_polylines(context, lpoints, color, thickness, LINE_TYPE):
    if LINE_TYPE == "GL_LINE_STIPPLE":
        bgl.glLineStipple(4, 0x5555)  #play with this later
        bgl.glEnable(bgl.GL_LINE_STIPPLE)  
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(*color)
    bgl.glLineWidth(thickness)
    bgl.glDepthRange(0.0, 0.997)
    for points in lpoints:
        bgl.glBegin(bgl.GL_LINE_STRIP)
        for coord in points:
            bgl.glVertex3f(*coord)
        bgl.glVertex3f(*points[0])
        bgl.glEnd()
    bgl.glLineWidth(1)
    if LINE_TYPE == "GL_LINE_STIPPLE":
        bgl.glDisable(bgl.GL_LINE_STIPPLE)
        bgl.glEnable(bgl.GL_BLEND)  # back to uninterrupted lines
        
def draw3d_quad(context, points, color):
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(*color)
    bgl.glDepthRange(0.0, 0.999)
    bgl.glBegin(bgl.GL_QUADS)
    for coord in points: bgl.glVertex3f(*coord)
    bgl.glEnd()
    
def draw3d_quads(context, lpoints, color):
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(*color)
    bgl.glDepthRange(0.0, 0.999)
    bgl.glBegin(bgl.GL_QUADS)
    for points in lpoints:
        for coord in points:
            bgl.glVertex3f(*coord)
    bgl.glEnd()
    
def draw3d_points(context, points, color, size):
    bgl.glColor4f(*color)
    bgl.glPointSize(size)
    bgl.glDepthRange(0.0, 0.997)
    bgl.glBegin(bgl.GL_POINTS)
    for coord in points: bgl.glVertex3f(*coord)  
    bgl.glEnd()
    bgl.glPointSize(1.0)