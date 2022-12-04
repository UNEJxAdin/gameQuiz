from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut

import random as rd
import csv

txt_soal = []

# IMPORT DARI CSV FILE
with open ('soal.csv', 'r') as sl:
    _soal = csv.reader(sl, delimiter=',')
    for i in _soal:
        txt_soal.append(i)

pos_jwb = [[170, 300], [740, 300]] # MENENTUKAN POSISI JAWABAN
selected = [] 
randomize = None
jmlSoal = len(txt_soal)-1 #

count = 0

score = 0
nyawa = 3
nSoal = rd.randint(0, jmlSoal-1)
randomize = rd.randint(0, 1)

def soal():
    drawTextBold(txt_soal[nSoal][0],400,500)
    if randomize == 0:
        benar = pos_jwb[0]
        salah = pos_jwb[1]

    else:
        benar = pos_jwb[1]
        salah = pos_jwb[0]
    jwb_benar(benar[0], benar[1]) # benar
    jwb_salah (salah[0], salah[1]) # salah

def jwb_salah(px, py):
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(0,105,255)
    glVertex2f(px, 275)
    glVertex2f(px, 340)
    glVertex2f(px + 130, 340)
    glVertex2f(px + 130, 275)
    glEnd()

    drawTextBold(txt_soal[nSoal][2],px+25,py)
    glPopMatrix()

def jwb_benar(px, py):
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(0,105,255)
    glVertex2f(px, 275)
    glVertex2f(px, 340)
    glVertex2f(px + 130, 340)
    glVertex2f(px + 130, 275)
    glEnd()

    drawTextBold(txt_soal[nSoal][1],px+25,py)
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

def mouseFunc(button, state, x, y):
    global jawab, nSoal, randomize, nyawa, score, count, selected
    if nyawa > 0:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if randomize == 0:
                if ((pos_jwb[0][0] <= x <= pos_jwb[0][0]+150) and (430 >= y >= 350)):
                    score += 1

                if ((pos_jwb[1][0] <= x <= pos_jwb[1][0]+150) and (430 >= y >= 350)):
                    nyawa -= 1

            elif randomize == 1:
                if ((pos_jwb[0][0] <= x <= pos_jwb[0][0]+150) and (430 >= y >= 350)):
                    nyawa -= 1

                if ((pos_jwb[1][0] <= x <= pos_jwb[1][0]+150) and (430 >= y >= 350)):
                    score += 1
            nSoal = rd.randint(0, jmlSoal-1)
            randomize = rd.randint(0, 1)
            count += 1

def Keyboard(key, x, y):
    global nyawa, score, nSoal, randomize, count
    if nyawa <= 0 or score == 10:
        if key == b'r':
            count = 0
            nyawa = 3
            score = 0
            nSoal = rd.randint(0, jmlSoal-1)
            randomize = rd.randint(0, 1)
        
        if key == b' ':
            glutDestroyWindow(wind)
            

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,204,204,0)
    glLoadIdentity()
    iterate()
    glColor3f(255,0,0)
    glBegin(GL_POINTS)
    glVertex2f(20, 20)
    glEnd()

    if nyawa > 0 and count < 10:
        drawText(f"LIFE : {nyawa}", 900, 650, 0,0,0)
        drawText(f"SCORE : {score}", 900, 625, 0,0,0)
        soal()
    else:
        drawTextBold("GAME SELESAI", 460, 350)
        drawText(f'SCORE KAMU : {score}', 470, 320, 0,0,0)
        drawText('tekan "r" untuk restart',435, 292, 0,0,0)
    

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 700)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("Quiziz")
glutDisplayFunc(showScreen)
glutKeyboardFunc(Keyboard)
glutIdleFunc(showScreen)
glutMouseFunc(mouseFunc)
glutMainLoop()