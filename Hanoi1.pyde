add_library('minim')
minim=Minim(this)
from random import randint

disx=[]
ben=[]
click=[0,0,0]
highl=[0,0,0]
top=[0,50,50]
lg=[0,0,0]
kl=[]
menu=[1]
rod=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
disks=[0]
hght=[0,0,0]
right=[0]
L=[0]
intro=[0]
img = [None]
noclick=0
  
def Hanoi():
    Dor()
    Zones()
    fill(255,182,193)
    rect(0,0,255,30)
    textSize(17)
    fill(0)
    text("Disks placed on the correct rod - " + str(right[0]), 1, 20)
    textSize(25)
    Victory()

def setup():
    size(849,580)
    noStroke()
    rectMode(CORNERS)
    f=loadFont("Andalus-36.vlw")
    textFont(f)
    Intro()
    img[0]=loadImage("Hanoi.jpg")
    for i in range (0,16):
        kl.append(color((1423*i)%225+30, (324*i)%225+30, (216*i)%225+30))
    music=minim.loadFile('Audio'+str(randint(1,2))+'.mp3')
    music.play()

def mouseClicked():
    
    if menu[0]==1:
        if intro[0]==0:
            Start()
            intro[0]=1
        else:
            Menu()
    else:
        
        if(mouseX>=75 and mouseX <=275 and click[0]==0 and menu[0]==0):
            if (click[1]==0 and click[2]==0):
                rect (75,530, 275,560)
                click[0]=1
            else:
                if(click[1]==1):
                    if(top[0]>top[1]):
                        last=disx[L[0]-top[1]]
                        last.from2to1()
                        Hanoi()
                    else: 
                        Zones()
                if(click[2]==1):
                    if(top[0]>top[2]):
                        last=disx[L[0]-top[2]]
                        last.from3to1()
                        Hanoi()
                    else: 
                        fill(color(random(120,256), random(200,250),random(100,250)))
                        text("This move is not allowed.", 300, 125)
                        Zones()
                ResetAllClicks()
      
        if(mouseX>=325 and mouseX <=525 and click[1]==0 and menu[0]==0):
            if(click[0]==0 and click[2]==0):
                rect(325,530,525,560)
                click[1]=1
            else:
                if(click[0]==1):
                    if top[1]>top[0]:
                        last=disx[L[0]-top[0]]
                        last.from1to2()
                        Hanoi()
          
                    else: 
                        fill(color(random(120,256), random(200,250),random(100,250)))
                        text("This move is not allowed.", 300, 125)
                        Zones()
                if(click[2]==1):
                    if(top[1]>top[2]):
                        last=disx[L[0]-top[2]]
                        last.from3to2()
                        Hanoi()
                    else:
                        fill(color(random(120,256), random(200,250),random(100,250)))
                        text("This move is not allowed.", 300, 125)
                        Zones()
                ResetAllClicks()
      
    
    if(mouseX>=575 and mouseX <=775 and click[2]==0 and menu[0]==0):
        if(click[0]==0 and click[1]==0):
            rect(575,530,775,560)
            click[2]=1
        else:
            if(click[0]==1):
                if(top[2]>top[0]):
                    last=disx[L[0]-top[0]]
                    last.from1to3()
                    Hanoi()
          
                else:
                    fill(color(random(120,256), random(200,250),random(100,250)))
                    text("This move is not allowed.", 300, 125)
                    Zones()
        
            if(click[1]==1):
                if(top[2]>top[1]):
                    last=disx[L[0]-top[1]]
                    last.from2to3()
                    Hanoi()
                else: 
                    fill(color(random(120,256), random(200,250),random(100,250)))
                    text("This move is not allowed.", 300, 125)
                    Zones()
            ResetAllClicks()

                

def draw():

  if(noclick==0):
  
    PickZone()
    leaveZone()

class Disk():
    def __init__ (self, tempA, tempB, tempC, tempD):
        self.a=tempA
        self.b=tempB
        self.c=tempC
        self.d=tempD
    def display(self):
        rect(self.a, self.b, self.c, self.d)
  
    def from1to2(self):
        if(rod[top[0]]==1):
            right[0]-=1
        if(rod[top[0]]==2):
            right[0]+=1
        loq=530-(20*(lg[1]+1)+5*(lg[1]+1))
        self.a=322+6*(L[0]-top[0]+1)
        self.b=loq
        self.c=528-6*(L[0]-top[0]+1)
        self.d=loq+20
        trf=top[0]
        top[0]=ben[top[0]]
        trl=top[1]
        top[1]=trf
        ben[top[1]]=trl
        lg[0]-=1
        lg[1]+=1
        
    def from1to3(self):
        if(rod[top[0]]==1):
            right[0]-=1
        if(rod[top[0]]==3):
            right[0]+=1
        loq=530-(20*(lg[2]+1)+5*(lg[2]+1))
        self.a=572+6*(L[0]-top[0]+1)
        self.b=loq
        self.c=778-6*(L[0]-top[0]+1)
        self.d=loq+20
        trf=top[0]
        top[0]=ben[top[0]]
        trl=top[2]
        top[2]=trf
        ben[top[2]]=trl
        lg[0]-=1
        lg[2]+=1
    
    def from2to1(self):
        if(rod[top[1]]==2):
            right[0]-=1
        if(rod[top[1]]==1):
            right[0]+=1
        loq=530-(20*(lg[0]+1)+5*(lg[0]+1))
        self.a=72+6*(L[0]-top[1]+1)
        self.b=loq
        self.c=278-6*(L[0]-top[1]+1)
        self.d=loq+20
        trf=top[1]
        top[1]=ben[top[1]]
        trl=top[0]
        top[0]=trf
        ben[top[0]]=trl
        lg[1]-=1
        lg[0]+=1
  
    def from2to3(self):
        if(rod[top[1]]==2):
            right[0]-=1
        if(rod[top[1]]==3):
            right[0]+=1
        loq=530-(20*(lg[2]+1)+5*(lg[2]+1))
        self.a=572+6*(L[0]-top[1]+1)
        self.b=loq
        self.c=778-6*(L[0]-top[1]+1)
        self.d=loq+20
        trf=top[1]
        top[1]=ben[top[1]]
        trl=top[2]
        top[2]=trf
        ben[top[2]]=trl
        lg[1]-=1
        lg[2]+=1
        
    def from3to1(self):
        if(rod[top[2]]==3):
            right[0]-=1
        if(rod[top[2]]==1):
            right[0]+=1
        loq=530-(20*(lg[0]+1)+5*(lg[0]+1))
        self.a=72+6*(L[0]-top[2]+1)
        self.b=loq
        self.c=278-6*(L[0]-top[2]+1)
        self.d=loq+20
        trf=top[2]
        top[2]=ben[top[2]]
        trl=top[0]
        top[0]=trf
        ben[top[0]]=trl
        lg[2]-=1
        lg[0]+=1
    
    def from3to2(self):
        if(rod[top[2]]==3):
            right[0]-=1
        if(rod[top[2]]==2):
            right[0]+=1
        loq=530-(20*(lg[1]+1)+5*(lg[1]+1))
        self.a=322+6*(L[0]-top[2]+1)
        self.b=loq
        self.c=528-6*(L[0]-top[2]+1)
        self.d=loq+20
        trf=top[2]
        top[2]=ben[top[2]]
        trl=top[1]
        top[1]=trf
        ben[top[1]]=trl
        lg[2]-=1
        lg[1]+=1
  



def FirstCheck():
    for i in range(0, disks[0]):
        if(rod[i]==1):
            right[0]+=1
    Hanoi()


def GetDisks():
    for i in range (1, disks[0]+2):
        loc=530-(20*i+5*i)
        d = Disk (72+6*i, loc, 278-6*i, loc+20)
        disx.append(d)
    for i in range (0,disks[0]-1):
        ben.append(i+1)
    ben.append(50)
    L[0]=disks[0]-1
    lg[0]=disks[0]
    top[0]=0


def ResetAllClicks():
    for i in range(0,3):
        click[i]=0
        highl[i]=0

def Zones():

    fill(200,30,10)
    rect(0,530,849,560)
    fill(255)
    textSize(25)
    text("1", 168, 555)
    text("2", 418, 555)
    text("3", 668, 555)



def PickZone():
    fill(0, 0,255, 160)
    if(mouseX>=75 and mouseX <=275 and highl[0]==0 and (click[1]==1 or click[2]==1)):
        rect (75,530, 275,560)
        highl[0]=1
    if(mouseX>=325 and mouseX <=525 and highl[1]==0 and (click[0]==1 or click[2]==1)):
        rect(325,530,525,560)
        highl[1]=1
    if(mouseX>=575 and mouseX <=775 and highl[2]==0 and (click[0]==1 or click[1]==1)):
        rect(575,530,775,560)
        highl[2]=1


def leaveZone():
    if (highl[0]==1):
        if(mouseY<530 or mouseY>560 or mouseX<75 or mouseX >275):
            highl[0]=0
            fill(200,30,10)
            rect(75,530,275,560)
            fill(255)
            text("1", 168, 555)
    if(highl[1]==1):
        if(mouseY<530 or mouseY>560 or mouseX<325 or mouseX >525):
            highl[1]=0
            fill(200,30,10)
            rect(325,530,525,560)
            fill(255)
            text("2", 418, 555)
    if(highl[2]==1):
        if(mouseY<530 or mouseY>560 or mouseX<575 or mouseX >775): 
            highl[2]=0
            fill(200,30,10)
            rect(575,530,775,560)
            fill(255)
            text("3", 668, 555)

def Assign():
    for i in range (0,disks[0]):
        rnd=random(0,1)
        if(rnd<0.3):
            rod[i]=1
            hght[0]+=1
        if(rnd>=0.3 and rnd<0.65): 
            rod[i]=2
            hght[1]+=1
        if(rnd>=0.65):
            rod[i]=3
            hght[2]+=1
    if(hght[1]==0 and hght[2]==0):
        NoNonsense()


def NoNonsense():
    rnd1=int(random(0,disks[0]-1))
    rnd2=random(0,1)
    if(rnd2<0.5):
        rod[rnd1]=2
        hght[1]=1
    else:
        rod[rnd1]=3
        hght[2]=1
    hght[0]=disks[0]-1
  
def Victory():
    if(right[0]==disks[0]):
        noclick=1
        Dor()
        fill(200,30,10)
        rect(0,530,849,560)
        textSize(100)
        fill(200,200,0)
        text("You won!!!", 220,120)
        
def Dor():
    image(img[0],0,0)
    fill(200,30,10)
    rect(170, 130, 180, 530)
    rect(420, 130, 430, 530)
    rect(670, 130, 680, 530)
    for i in range (0, len(disx)-1):
        fill(kl[i])
        disx[i].display()

def Intro():
    background(135,206,250)
    if intro[0]==0:
        textSize(36)
        fill(0,0,25)
        text("How to play:", 300, 110)
        textSize(25)
        text("You begin with 3 rods, with disks arranged on one of them from the smallest to  \n the largest. You can move them, placing only smaller disks on the top of \n larger disks.  In the regular Tower of Hanoi game, you would need to move all \n the disks to one of the other two rods.  But here we'll play a modification - \n you'll have to bring the disks \
to a certain position - you don't know which one, \n but you will receive hints. More specifically, after each move you will know \n how many of the disks are on the correct rod. \
Move a disk by clicking on the \n rod where it is placed and then click on the intended target rod. Enjoy!",20,210)
        text("Click anywhere to advance", 500, 500)

def Start():
    background(135,206,250)
    fill(0,170,225,140)
    rect(300,130,450,160)
    rect(300,180,450,210)
    rect(300,230,450,260)
    rect(300,280,450,310)
    rect(300,330,450,360)
    rect(300,380,450,410)
    rect(300,430,450,460) 
    textSize(36)
    fill(0,0,25)
    text("Choose the difficulty level:", 300, 100)
    textSize(20)
    text("Pointlessly easy", 300, 150)
    text("Easy", 300, 200)
    text ("Moderate",300, 250)
    text ("Tough", 300, 300)
    text ("Very tough", 300, 350)
    text ("Pointlessly tough", 300, 400)
    text ("Insane", 300, 450)
    

def Menu():
    if mouseX>=300 and mouseX<=480:
        if mouseY>=130 and mouseY<=160:
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=1
            else: 
                disks[0]=2
        if mouseY>=180 and mouseY<=210:       
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=3
            else: 
                disks[0]=4
        if mouseY>=230 and mouseY<=260:
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=5
            else: 
                disks[0]=6
        if mouseY>=280 and mouseY<=310:
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=7
            else: 
                disks[0]=8
        if mouseY>=330 and mouseY<=360 and menu[0]==1:
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=9
            else: 
                disks[0]=10
        if mouseY>=380 and mouseY<=410:
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=11
            else: 
                disks[0]=12
        if mouseY>=430 and mouseY<=460:
            rnd=randint(0,1)
            if rnd==0:
                disks[0]=13
            else: 
                disks[0]=14
        if disks[0]!=0:
            menu[0]=0
            GetDisks()
            Assign()
            FirstCheck()
    
  
