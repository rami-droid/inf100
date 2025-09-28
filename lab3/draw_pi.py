from uib_inf100_graphics.simple import canvas, display
import random

def draw_dot(canvas, x, y, fill_color='orange'):
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=fill_color)

# Draw a circle in the window
canvas.create_oval(0, 0, 400, 400)

# Highlight a random point on 400x400 canvas
def draw_random(amount=1):
    total = 0
    count = 0
    for _ in range(amount):
        x = random.random() * 400
        y = random.random() * 400

        if abs((200-x))**2 + abs((200-y))**2 <= 200**2:
            draw_dot(canvas, x, y, 'orange')
            count += 1
            total += 1
        else:
            draw_dot(canvas, x, y, 'blue')
            total += 1
    ratio = count / total 
    message = f'{count}/{total} prikker traff sirkelen \n beregnet pi: {ratio*4:.3f}'
    canvas.create_rectangle(100, 180, 300, 220, fill='white')
    canvas.create_text(200, 200, text=message, fill='blue')
    return count

draw_random(1000)
display(canvas)
