#Kaden Semanko
#25/12/05
#practice_dec_05.py
import DrawingPanel
#dp = DrawingPanel.DrawingPanel(300,300)
down = 10
other = 100
#dp.set_color("dark green")
for i in range(10): #looping for 10 rectanges
#    dp.draw_rect(10,down,other,10)
    down += 10 #increases parameters each time
    other -= 10
box = DrawingPanel.DrawingPanel(300,300)
fun = 240
dwn = 10
for i in range(25):
    box.fill_rect(0,0,300,300,"white")
    box.fill_oval(fun,dwn,50,50,"red")
    dwn += 10
    fun -= 10
    box.sleep(40)
