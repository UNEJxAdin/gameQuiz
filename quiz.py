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
randomize = None # MENENTUKAN POSISI JAWABAN
jmlSoal = len(txt_soal)-1 #

count = 0 #MENGHITUNG SOAL TELAH DITAMPILKAN

score = 0 #SCORE AWAL
nyawa = 3 # NYAWA AWAL
nSoal = rd.randint(0, jmlSoal-1) #MENENTUKAN SOAL YANG AKAN DITAMPILKAN
randomize = rd.randint(0, 1) #POSISI JAWABAN

def soal():
    drawTextBold(txt_soal[nSoal][0],400,500)    #MENAMPILKAN SOAL SECARA RANDOM 
    if randomize == 0: 
        benar = pos_jwb[0]  #JWB BENAR 
        salah = pos_jwb[1]  #JWB SALAH

    else:
        benar = pos_jwb[1]  #JWB BENAR
        salah = pos_jwb[0]  #JWB SALAH
    jwb_benar(benar[0], benar[1]) # benar
    jwb_salah (salah[0], salah[1]) # salah

def jwb_salah(px, py):          #BENTUK PERSEGI PANJANG SEBAGAI BACKGROUND DARI JAWABAN
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(204,0,204)   #WARNA
    glVertex2f(px, 275)
    glVertex2f(px, 340)
    glVertex2f(px + 130, 340)
    glVertex2f(px + 130, 275)
    glEnd()

    drawTextBold(txt_soal[nSoal][2],px+25,py)       #TEKS JAWAB SALAH, DI CSV PADA INDEKS KE 2
    glPopMatrix()

def jwb_benar(px, py):  #BENTUK PERSEGI PANJANG SEBAGAI BACKGROUND DARI JAWABAN
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(204,0,204)   #WARNA
    glVertex2f(px, 275)
    glVertex2f(px, 340)
    glVertex2f(px + 130, 340)
    glVertex2f(px + 130, 275)
    glEnd()

    drawTextBold(txt_soal[nSoal][1],px+25,py)   #TEKS JAWAB BENAR, DI CSV INDEKS KE 1
    glPopMatrix()

def drawText(ch,xpos,ypos,r,b,g):               #MENULIS TEKS (TIDAK TEBAL) 
    color = (r, b, g)                       #WARNA
    font_style = glut.GLUT_BITMAP_8_BY_13       #GAYA PENULISAN/KARAKTER
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def drawTextBold(ch,xpos,ypos):                     #MENULIS TEKS TEBAL
    glPushMatrix()
    color = (0,0,0)             #WARNA
    font_style = glut.GLUT_BITMAP_HELVETICA_18      #GAYA TEKS
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

def background():
    glPushMatrix()
    glTranslated(500, 350, 0)
    # Background ============================================
    glBegin(GL_POLYGON)
    glColor3ub(153,204,255)
    glVertex2f(-500,-350)
    glVertex2f(-500,350)
    glVertex2f(500,350)
    glVertex2f(500,-350)
    glEnd()

    #BANGUN SEGITIGA DARI KIRI
    glBegin(GL_POLYGON)
    glColor3d(255,255,0)
    glVertex2f(-500, -350)
    glVertex2f(-400, -250)
    glVertex2f(-500, -150)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0,0,0)
    glVertex2f(-500, -350)
    glVertex2f(-400, -250)
    glVertex2f(-300, -350)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3d(255,255,0)
    glVertex2f(-400, -250)
    glVertex2f(-300, -350)
    glVertex2f(-200, -250)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0,0,0)
    glVertex2f(-300, -350)
    glVertex2f(-200, -250)
    glVertex2f(-100, -350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(255,255,0)
    glVertex2f(-200, -250)
    glVertex2f(-100, -350)
    glVertex2f(0, -250)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3d(0,0,0)
    glVertex2f(-100, -350)
    glVertex2f(0, -250)
    glVertex2f(100, -350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(255,255,0)
    glVertex2f(0, -250)
    glVertex2f(100, -350)
    glVertex2f(200, -250)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0,0,0)
    glVertex2f(100, -350)
    glVertex2f(200, -250)
    glVertex2f(300, -350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(255,255,0)
    glVertex2f(200, -250)
    glVertex2f(400, -250)
    glVertex2f(300, -350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0,0,0)
    glVertex2f(300, -350)
    glVertex2f(400, -250)
    glVertex2f(500, -350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(255,255,0)
    glVertex2f(400, -250)
    glVertex2f(500, -150)
    glVertex2f(500, -350)
    glEnd()
    
    #BINTANG==========================================
    glBegin(GL_POLYGON)
    glColor3d(255,0,0)
    glVertex2f(-400, 240)
    glVertex2f(-440, 260)
    glVertex2f(-400, 280)
    glVertex2f(-380, 320)
    glVertex2f(-360, 280)
    glVertex2f(-320, 260)
    glVertex2f(-360, 240)
    glVertex2f(-380, 200)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(255,255,255)
    glVertex2f(-380, 260)
    glVertex2f(-380, 320)
    glVertex2f(-360, 280)
    glVertex2f(-380, 260)
    glVertex2f(-320, 260)
    glVertex2f(-360, 240)
    glVertex2f(-380, 260)
    glVertex2f(-380, 200)
    glVertex2f(-400, 240)
    glVertex2f(-380, 260)
    glVertex2f(-440, 260)
    glVertex2f(-400, 280)
    glEnd()
    glPopMatrix()

def iterate():
    glViewport(0, 0, 1000, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def mouseFunc(button, state, x, y):
    global nSoal, randomize, nyawa, score, count, selected
    if nyawa > 0:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            print(f"{x}, {y}")
            if randomize == 0:
                if ((pos_jwb[0][0] <= x <= pos_jwb[0][0]+150) and (350 <= y <= 430)):
                    score += 1
                    count += 1

                if ((pos_jwb[1][0] <= x <= pos_jwb[1][0]+150) and (350 <= y <= 430)):
                    nyawa -= 1
                    count += 1

            elif randomize == 1:
                if ((pos_jwb[0][0] <= x <= pos_jwb[0][0]+150) and (350 <= y <= 430)):
                    nyawa -= 1
                    count += 1

                if ((pos_jwb[1][0] <= x <= pos_jwb[1][0]+150) and (350 <= y <= 430)):
                    score += 1
                    count += 1
            nSoal = rd.randint(0, jmlSoal-1)
            randomize = rd.randint(0, 1)
            

def Keyboard(key, x, y):
    global nyawa, score, nSoal, randomize, count
    if nyawa == 0 or score <= 10:
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
    background()
    # glColor3f(255,0,0)
    # glBegin(GL_POINTS)
    # glVertex2f(20, 20)
    # glEnd()

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