# pig_main.py
from uib_inf100_graphics.simple import canvas, display
from pig_head import draw_head
from pig_body import draw_body

# TODO: kall på funksjonene draw_body og draw_head
draw_body(canvas, 50, 150, 250, 300)
draw_head(canvas, 150, 100, 75)
...

display(canvas)
