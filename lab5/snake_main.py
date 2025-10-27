from uib_inf100_graphics.helpers import text_in_box
from snake_view import draw_board
import getpass
import random
import json


def make_board(num_rows, num_cols):
    board = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    center: tuple = (num_rows // 2, num_cols // 2)
    x, y = center
    count = 3
    for i in range(3):
        board[x][y + i] = count
        count -= 1
    head_pos = (x, y)
    add_apple_at_random_location(board)
    return board, head_pos


def app_started(app, first_launch=True):
    app.direction = "west"
    app.info_mode = False
    app.board, app.head_pos = make_board(10, 10)
    app.snake_size = 3
    if first_launch:
        app.state = "menu"
    else:
        app.state = "active"
    app.start_menu_items = ["start", "highscore"]
    app.menu_index = 0
    app.difficulties = ["easy", "medium", "hard"]
    app.difficulty_index = 0


    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    ...

def highscore_menu(canvas, app):
    try:
        with open("highscore.json","r") as file:
            scores = json.load(file)
        for i, score in enumerate(scores[:10]):
            canvas.create_text(app.width /2, app.height/3 + i * 30, text=f"{score['username']}: {score['score']}")

    except FileNotFoundError:
        canvas.create_text(app.width /2, app.height/2, text="No high scores found")

    canvas.create_text(app.width /2, app.height/2, text="press ESC to go to main menu")


def start_menu(canvas, app):
    text_in_box(
        canvas,
        app.width / 2 - 50,
        app.height / 6 - 25,
        app.width / 2 + 50,
        app.height / 6 + 25,
        "SNAKE",
    )
    y_start = app.height / 3
    canvas.create_rectangle(
        app.width / 2 - app.width / 4,
        y_start,
        app.width / 2 + app.width / 4,
        len(app.start_menu_items) * 50 + 20 + y_start,
    )
    for i, text in enumerate(app.start_menu_items):
        item_y = y_start + i * 50 + 30
        color = "yellow" if i == app.menu_index else "white"
        canvas.create_text(
            app.width / 2, item_y, text=text, font=("Arial", 12), fill=color
        )
    # canvas.create_text(app.width / 2, app.height / 5, text="SNAKE", font=("Arial", 24))


def difficulty_menu(canvas, app):
    y_start = app.height / 2
    canvas.create_rectangle(
        app.width / 2 - app.width / 4,
        y_start,
        app.width / 2 + app.width / 4,
        len(app.difficulties) * 50 + 20 + y_start,
    )
    for i, text in enumerate(app.difficulties):
        item_y = y_start + i * 50 + 30
        color = "red" if i == app.difficulty_index else "white"
        canvas.create_text(
            app.width / 2, item_y, text=text, font=("Arial", 12), fill=color
        )
def save_highscore(score):
    username = getpass.getuser()
    data = {"username": username, "score": score}
    try:
        with open("highscore.json", 'r') as file:
            new_data = json.load(file)
            if not isinstance(new_data, list):
                new_data = []
            new_data.append(data)
    except FileNotFoundError:
        new_data = [data]

    with open("highscore.json", 'w') as file:
        json.dump(new_data, file, indent=2)

def is_legal_move(pos: tuple, board):
    rows = len(board)
    cols = len(board[0])
    r, c = pos
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False
    if board[r][c] > 0:
        return False
    return True


def subtract_one_from_all(board):
    return [[i - 1 if i > 0 else i for i in j] for j in board]


def add_apple_at_random_location(board):
    while True:
        rows = len(board)
        cols = len(board[0])

        rand_row = random.randint(0, rows - 1)
        rand_cols = random.randint(0, cols - 1)
        if board[rand_row][rand_cols] == 0:
            board[rand_row][rand_cols] = -1
            break
    return board

def find_apple(board):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == -1:
                return (r, c)
    return None


def move_snake(direction, app):
    move = app.head_pos
    match direction:
        case "north":
            move = (-1, 0)
        case "south":
            move = (1, 0)
        case "west":
            move = (0, -1)
        case "east":
            move = (0, 1)
    old_pos = app.head_pos
    new_pos = tuple(x + y for x, y in zip(old_pos, move))
    if not is_legal_move(new_pos, app.board):
        save_highscore(app.snake_size - 3)
        app.state = "gameover"
        return
    if app.board[new_pos[0]][new_pos[1]] >= 0:
        app.board = subtract_one_from_all(app.board)
    else:
        app.board = add_apple_at_random_location(app.board)
        app.snake_size += 1
    app.board[new_pos[0]][new_pos[1]] = app.snake_size
    app.head_pos = new_pos


def timer_fired(app):
    if not app.info_mode and app.state == "active":
        move_snake(app.direction, app)
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    #
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...


def key_pressed(app, event):
    # MENU
    if app.state == "menu":
        if event.key == "Up" or event.key == "k":
            app.menu_index -= 1
            app.menu_index = app.menu_index % len(app.start_menu_items)
        if event.key == "Down" or event.key == "j":
            app.menu_index += 1
            app.menu_index = app.menu_index % len(app.start_menu_items)
        if event.key == "Enter":
            selected = app.start_menu_items[app.menu_index]
            if selected == "start":
                app.state = "difficulty"
            if selected == 'highscore':
                app.state =  'highscore'
        return

    # DIFFICULTY
    if app.state == "difficulty":
        if event.key == "Up" or event.key == "k":
            app.difficulty_index -= 1
            app.difficulty_index = app.difficulty_index % len(app.difficulties)
        if event.key == "Down" or event.key == "j":
            app.difficulty_index += 1
            app.difficulty_index = app.difficulty_index % len(app.difficulties)
        if event.key == "Enter":
            selected = app.difficulties[app.difficulty_index]
            if selected == "medium":
                app.board, app.head_pos = make_board(10, 10)
                app.state = "active"
                app.timer_delay = 200
            elif selected == "easy":
                app.board, app.head_pos = make_board(7, 7)
                app.timer_delay = 300
                app.state = "active"
            elif selected == "hard":
                app.board, app.head_pos = make_board(15, 15)
                app.state = "active"
                app.timer_delay = 100
        return

    # GLOBAL KEYS
    if event.key == "i":
        app.info_mode = not app.info_mode

    if event.key == "Escape":
        app_started(app)
        return

    # ACTIVE GAME
    if app.state == "active":
        if event.key in ("Up", "k", "w"):
            app.direction = "north"
        elif event.key in ("Down", "j", "s"):
            app.direction = "south"
        elif event.key in ("Left", "h", "a"):
            app.direction = "west"
        elif event.key in ("Right", "l", "d"):
            app.direction = "east"
        elif event.key == "Space":
            move_snake(app.direction, app)

    # GAME OVER
    if app.state == "gameover":
        if event.key == "r":
            #app.board = 
            app.state = "difficulty"

def redraw_all(app, canvas):
    if app.state == "menu":
        start_menu(canvas, app)
    if app.state == 'highscore':
        highscore_menu(canvas, app)
    if app.state == "difficulty":
        difficulty_menu(canvas, app)
    if app.state == "active":
        draw_board(
            canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.info_mode, app.snake_size
        )
        canvas.create_text(50, 15, text=f"Score: {app.snake_size - 3}")
    if app.info_mode:
        canvas.create_text(app.width / 2, 12, text=f"{app.direction}")
        canvas.create_text(app.width / 2 + 50, 12, text=f"{app.state}")
    if app.state == "gameover":
        canvas.create_text(
            app.width / 2 + 50, app.height / 2, text="Game Over", font=("Arial", 24)
        )
        canvas.create_text(
            app.width / 2 + 50,
            app.height / 2 + 30,
            text="press r to restart.",
            font=("Arial", 12),
        )
        canvas.create_text(
            app.width / 2 + 50, app.height / 2 + 50, text=f"score: {app.snake_size - 3}", font=("Arial", 12)
        )
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    ...


if __name__ == "__main__":
    from uib_inf100_graphics.event_app import run_app

    run_app(width=500, height=400, title="Snake")
