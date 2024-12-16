#Kaden Semanko
#24/12/06
#dec_06_practice.py
import DrawingPanel
dp = DrawingPanel.DrawingPanel(800,600)#4/3 drawing panel
def minicar(x):
    for i in range(x): #Sets it to be animated with a loop
        if i < 300:
            dp.fill_rect(0,0,800,400,"sky blue")
            dp.fill_oval(700,30,60,60,"yellow")
            dp.fill_rect(0,400,800,600,"dark green")
            dp.fill_rect(400,410,20,70)
            dp.set_color("red")
            dp.fill_rect(20+i,450,80,20,"dark red")
            dp.fill_rect(40+i,430,40,20,"red")
            dp.set_color("black")
            dp.fill_oval(30+i,470,15,15)
            dp.fill_oval(75+i,470,15,15)
            dp.sleep(5)
        if i == 300:
            dp.fill_rect(0,0,800,400,"sky blue")
            dp.fill_oval(700,30,60,60,"yellow")
            dp.fill_rect(0,400,800,600,"dark green")
            dp.fill_rect(400,410,20,70)
            dp.set_color("red")
            dp.fill_rect(320,450,80,20,"dark red")
            dp.fill_rect(340,430,40,20,"red")
            dp.set_color("black")
            dp.fill_oval(330,470,15,15)
            dp.fill_oval(375,470,15,15)
            dp.sleep(400)
        if i > 301:
            dp.fill_rect(0,0,800,400,"sky blue")
            dp.fill_oval(700,30,60,60,"yellow")
            dp.fill_rect(0,400,800,600,"dark green")
            dp.fill_rect(400,410,20,70)
            dp.set_color("red")
            dp.fill_rect(20+i,480,80,20,"dark red")
            dp.fill_rect(40+i,460,40,20,"red")
            dp.set_color("black")
            dp.fill_oval(30+i,500,15,15)
            dp.fill_oval(75+i,500,15,15)
            dp.sleep(5)
minicar(500)