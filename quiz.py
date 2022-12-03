from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut

import random as rd

pos_jwb = [(170, 300), (720, 840)]
txt_soal = ["1. Dasar negara Indonesia adalah", "2. Mage apa yang terkuat"]
jawaban = [["Pancasila", "UUD 1945"],["Magewati", "Kagura"]]

def soal():
    drawTextBold(txt_soal[0],410,500)

def jwb_benar():
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(0,105,255)
    glVertex2f(170, 275)
    glVertex2f(170, 340)
    glVertex2f(300, 340)
    glVertex2f(300, 275)
    glEnd()

    drawTextBold(txt_benar2[0],195,300)
    glPopMatrix()

def jwb_salah():
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(0,105,255)
    glVertex2f(720, 275)
    glVertex2f(720, 340)
    glVertex2f(840, 340)
    glVertex2f(840, 275)
    glEnd()

    drawTextBold(txt_salah2[0],750,300)
    glPopMatrix()

def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def iterate():
    glViewport(0, 0, 1000, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

jawab = False
def mouseFunc(button, state, x, y):
    global jawab
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if ((170 <= x <= 300) and (430 >= y >= 350)):
            print("Benar")
        elif ((720 <= x <= 840) and (430 >= y >= 350)):
            print("Salah")

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(224,255,255,0)
    glLoadIdentity()
    iterate()
    glColor3f(255,0,0)
    if jawab == False:
        # drawTextBold(txt_soal,385,500)
        # drawTextBold(txt_benar[0],200,300)
        # drawTextBold(txt_salah[0],740,300)
        soal()
        jwb_benar()
        jwb_salah()
    #else:
        #Game Over3
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 700)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("Quiziz")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMouseFunc(mouseFunc)
glutMainLoop()