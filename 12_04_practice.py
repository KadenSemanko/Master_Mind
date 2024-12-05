#Kaden Semanko
# 12/04/24
#12_04_practice.py
import DrawingPanel  #importing DrawingPanel file
window = DrawingPanel.DrawingPanel(300,300) #made a panel to draw and set a name for DrawingPanel.DrawingPanel
#window_v2 = dp.DrawingPanel(500,500) 
window.set_color("red")
window.draw_oval(0,0,300,300) #overall shape
window.fill_oval(0,0,300,300,"sandybrown") #the color of face
window.draw_oval(60,40,70,120)
window.fill_oval(60,40,70,120,"white")
window.draw_oval(175,40,70,120)
window.fill_oval(175,40,70,120,"white")
window.fill_oval(90,40,10,120)
window.fill_oval(205,40,10,120)
window.draw_line(0,0,26,65) #ears
window.draw_line(0,0,65,27)
window.draw_line(300,0,274,65)
window.draw_line(300,0,235,27)
window.draw_line(135,145,150,165) #nose and mouth
window.draw_line(135,145,165,145)
window.draw_line(165,145,150,165)
window.draw_line(150,165,150,175)
window.draw_line(150,175,165,185)
window.draw_line(150,175,135,185)
window.set_color("black") 
window.draw_line(45,235,10,225) #left side whistkers
window.draw_line(45,245,8,245)
window.draw_line(47,255,12,265)
window.draw_line(255,235,290,225) #right side whiskers
window.draw_line(255,245,290,245) 
window.draw_line(253,255,288,265)