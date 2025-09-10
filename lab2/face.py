from uib_inf100_graphics.simple import canvas, display


def draw_face(canvas, x, y, face_color, eye_color, mouth_color):
    canvas.create_oval(x, y, x + 100, y + 100, fill=face_color)  # Face
    canvas.create_oval(x + 20, y + 30, x + 40, y + 50, fill=eye_color)  # Left eye
    canvas.create_oval(x + 60, y + 30, x + 80, y + 50, fill=eye_color)  # Right eye
    canvas.create_arc(
        x + 20,
        y + 50,
        x + 80,
        y + 90,
        start=0,
        extent=-180,
        style="arc",
        outline=mouth_color,
        width=2,
    )  # Mouth


draw_face(canvas, 50, 30, "yellow", "black", "red")
display(canvas)
