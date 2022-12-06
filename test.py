# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import OpenGL.GLUT as glut

# import random as rd

# pos_jwb = [(170, 300), (720, 840)]
# txt_soal = ["1. Dasar negara Indonesia adalah", "2. Mage apa yang terkuat"]
# jawaban = [["Pancasila", "UUD 1945"],["Magewati", "Kagura"]]
# randomize = None
# nyawa = 3 # nyawa
# finish = False
# inSoal = False # kondisi soal
# currIdx = None # var index soal
# selected = [] # nyimpan yg sudah ditampilkan

# def soal():
#     global randomize
#     if currIdx != None: # currIdx = 1
#         _soal = txt_soal[currIdx]
#         benar = jawaban[currIdx][0]
#         salah = jawaban[currIdx][1]
#     drawTextBold(_soal,410,500)
    
#     randomize = rd.randint(0,1)
#     if randomize == 0:
#         jwb_kiri(salah)
#         jwb_kanan(benar)
#     else:
#         jwb_kiri(benar)
#         jwb_kanan(salah)

# def jwb_kiri(pilihan): #kiri
#     glPushMatrix()
#     glBegin(GL_QUADS)
#     glColor3ub(0,105,255)
#     glVertex2f(170, 275)
#     glVertex2f(170, 340)
#     glVertex2f(300, 340)
#     glVertex2f(300, 275)
#     glEnd()

#     drawTextBold(pilihan,195,300)
#     glPopMatrix()

# def jwb_kanan(pilihan):
#     glPushMatrix()
#     glBegin(GL_QUADS)
#     glColor3ub(0,105,255)
#     glVertex2f(720, 275)
#     glVertex2f(720, 340)
#     glVertex2f(840, 340)
#     glVertex2f(840, 275)
#     glEnd()

#     drawTextBold(pilihan,750,300)
#     glPopMatrix()

# def drawText(ch,xpos,ypos,r,b,g):
#     color = (r, b, g)
#     font_style = glut.GLUT_BITMAP_8_BY_13
#     glColor3ub(color[0],color[1],color[2])
#     line=0
#     glRasterPos2f (xpos, ypos)
#     for i in ch:
#        if  i=='\n':
#           line=line+1
#           glRasterPos2f (xpos, ypos*line)
#        else:
#           glutBitmapCharacter(font_style, ord(i))

# def drawTextBold(ch,xpos,ypos):
#     glPushMatrix()
#     color = (0,0,0)
#     font_style = glut.GLUT_BITMAP_HELVETICA_18
#     glColor3ub(color[0],color[1],color[2])
#     line=0
#     glRasterPos2f (xpos, ypos)
#     for i in ch:
#        if  i=='\n':
#           line=line+1
#           glRasterPos2f (xpos, ypos*line)
#        else:
#           glutBitmapCharacter(font_style, ord(i))  
#     glPopMatrix()  

# def iterate():
#     glViewport(0, 0, 1000, 700)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 1000, 0.0, 700, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()

# jawab = False
# def mouseFunc(button, state, x, y):
#     global jawab
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         if ((170 <= x <= 300) and (430 >= y >= 350)):
#             #if randomize==0:
#                 # salah, nyawa -=1, insoal false
#             # else:
#                 # benar, insoal false
#             print("Benar")
#         elif ((720 <= x <= 840) and (430 >= y >= 350)):
#             print("Salah")

# def showScreen():
#     global currIdx
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glClearColor(224,255,255,0)
#     glLoadIdentity()
#     iterate()
#     glColor3f(255,0,0)
#     if jawab == False: # if nyawa != 0
#         soal()
#         jwb_kanan()
#     global inSoal
#     if currIdx != None:
#         temp = rd.randint(0, len(soal)) #--> 1
#         inSoal = True
#         if temp not in selected:
#             selected.append (temp)
#         else:
#             inSoal = True 
#             currIdx = temp
#         soal()
#     # elif finish:
#         # splash menang
#     #else:
#         # Splash game over
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(1000, 700)
# glutInitWindowPosition(0,0)
# wind = glutCreateWindow("Quiziz")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMouseFunc(mouseFunc)
# glutMainLoop()