from uib_inf100_graphics.simple import canvas, display

def draw_soup_can(canvas, x, y, bg_color, text_color):
    canvas.create_rectangle(x, y+10, x+100, y+130, fill=bg_color)
    canvas.create_oval(x, y, x+100, y+20, fill='gray')
    canvas.create_oval(x, y+120, x+100, y+140, fill='gray')
    canvas.create_text(x+50, y+50, text='SOUP',
                       fill=text_color, font=('Arial', 16, 'bold'))

draw_soup_can(canvas, 50, 30, 'red', 'yellow')
# TODO: make three more calls to draw_soup_can with different arguments

draw_soup_can(canvas, 250, 210, 'blue', 'pink')
draw_soup_can(canvas, 50, 210, 'green', 'purple')
draw_soup_can(canvas, 250, 30, 'cyan', 'orange')
display(canvas)
