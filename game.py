import pgzrun
WIDTH=800
HEIGHT=800
score=0
timeleft=10
gameover=False
questions=[]
questioncount=0
questionindex=0



abox1=Rect(0,0,300,150)
abox1.move_ip(20,300)
abox2=Rect(0,0,300,150)
abox2.move_ip(20,460)
abox3=Rect(0,0,300,150)
abox3.move_ip(330,460)
abox4=Rect(0,0,300,150)
abox4.move_ip(330,300)
questionbox=Rect(0,0,650,150 )
questionbox.move_ip(20,100)
timerbox=Rect(0,0,150,150)
timerbox.move_ip(680,100)


def draw():
    screen.fill('blue')
    screen.draw.filled_rect(questionbox,'black')
    for box in answerboxes:
         screen.draw.filled_rect(box,'gray')
    screen.draw.filled_rect(timerbox,'brown')