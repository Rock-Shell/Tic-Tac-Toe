import pygame
import time
#############
white=(255,255,255)
black=(0,0,0)

##############
mat=[[None for i in range(3)]for j in range(3)]
mat2=[[None for i in range(3)]for j in range(3)]

def matrix(m):
     i=0
     if m[0][0]==m[1][1]==m[2][2]!=None:
          return m[0][0]
     elif m[2][0]==m[1][1]==m[0][2]!=None:
          return m[2][0]
     
     for i in range(3):
          if m[i][0]==m[i][1]==m[i][2]!=None:
               return m[i][0]
          elif m[0][i]==m[1][i]==m[2][i]!=None:
               return m[0][i]
     
def text_objects(text,font):
     textSurface=font.render(text,True,white)
     return textSurface,textSurface.get_rect()

def message_display(text):
     Ltext=pygame.font.Font('freesansbold.ttf',100)
     text="              "+text
     textSurf,textRect=text_objects(text,Ltext)
     textRect=(0,600)
     gameDisplay.blit(textSurf,textRect)
     
     pygame.display.update()

#############
pygame.init()
display_width=1201
display_height=700

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("ZERO KATA")

#gameDisplay.fill(white)
pygame.draw.rect(gameDisplay,black,(0,600,1201,100))

#screen.unlock()
img=pygame.image.load("tic.jpeg")
gameDisplay.blit(img,(0,0))

X=pygame.image.load("cross.png")
X=pygame.transform.scale(X,(100,100))
#gameDisplay.blit(x,(0,0))

o=pygame.image.load("zero.jpg")
o=pygame.transform.scale(o,(100,100))
#gameDisplay.blit(o,(100,0))


#############
def game():
     intro=True
     flag=0
     matu=[[None for i in range(3)]for j in range(3)]
     
     while  flag<9:
          if matrix(mat2)!=None:
               pygame.draw.rect(gameDisplay,black,(0,600,1201,100))
               if matrix(mat2)==1:
                    message_display(" X WINS")
               else:
                    message_display(" O WINS")               
               return
          for event in pygame.event.get():
               #print(event)
               if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()


          mouse=pygame.mouse.get_pos()
          x,y=mouse[0],mouse[1]
          click=pygame.mouse.get_pressed()
          #print("mouse- %s   , mat-  %s"%(mouse,mat))

          a,b,c=mat[0],mat[1],mat[2]

          for i in range(3):
               for j in range(3):
                    if mat[i][j]!=None:
                         matu[i][j]=mat[i][j]

          if x>185 and x<1010 and y>90 and y<522 and click==(1,0,0) :
               #flag2=1
                                   
               #pygame.draw.rect(gameDisplay,black,(0,600,1201,100))
               a=0
               if flag%2==0:
                    text="O turn"
               else:
                    text="X turn"
                    
               if x<453:
                    if y<227:
                         ind=(0,0)
                         mat[0][0]=a
                         pos=(290,90)
                    
                    elif y>227 and y<366:
                         ind=(1,0)
                         mat[1][0]=a
                         pos=(290,245)
                    
                    else:
                         ind=(2,0)
                         mat[2][0]=a
                         pos=(290,385)
                         
                         

               elif x>453 and x<728:
                    if y<227:
                         ind=(0,1)
                         mat[0][1]=a
                         pos=(520,90)
                         
                    elif y>227 and y<366:
                         ind=(1,1)
                         mat[1][1]=a
                         pos=(520,245)
                         
                    else:
                         ind=(2,1)
                         mat[2][1]=a
                         pos=(520,385)
                         
               else:
                    if y<227:
                         ind=(0,2)
                         mat[0][2]=a
                         pos=(750,90)
                         
                    elif y>227 and y<366:
                         ind=(1,2)
                         mat[1][2]=a
                         pos=(750,245)
                         
                    else:
                         ind=(2,2)
                         mat[2][2]=a
                         pos=(750,385)
                         
          if mat != matu:
               flag+=1
               print("%s - %s "%(flag,text))
               #print("%s - %s "%(mat,matu))
               #print()
               i,j=ind[0],ind[1]
               
               if text=="O turn":
                    pygame.draw.rect(gameDisplay,black,(0,600,1201,100))
                    gameDisplay.blit(o,pos)
                    mat2[i][j]=0
                    message_display("X turn")
               else:
                    pygame.draw.rect(gameDisplay,black,(0,600,1201,100))
                    gameDisplay.blit(X,pos)
                    mat2[i][j]=1
                    message_display("O turn")

               
          pygame.display.update()
     for i in range(3):
          for j in range(3):
               if mat2[i][j]==None:
                    mat2[i][j]=0
     pygame.draw.rect(gameDisplay,black,(0,600,1201,100))
     message_display(" FUCK OFF")
          #pygame.display.flip()
          #time.sleep(2)
game()

