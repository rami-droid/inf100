from snake_view import draw_board
import random


def app_started(app):
    app.direction = "east"
    app.info_mode = True
    app.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.snake_size = 3
    app.head_pos = (3, 4)
    app.state = "active"
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    ...


def is_legal_move(pos: tuple, board):
    rows = len(board)
    cols = len(board[0])
    r, c = pos
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False
    if board[r][c] != 0:
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
    print(event.key)
    if event.key == "i":
        app.info_mode = not app.info_mode

    if app.state != "active":
        return
    if event.key == "Up":
        app.direction = "north"
    if event.key == "Down":
        app.direction = "south"
    if event.key == "Left":
        app.direction = "west"
    if event.key == "Right":
        app.direction = "east"
    if event.key == "Space":
        move_snake(app.direction, app)
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    ...


def redraw_all(app, canvas):
    draw_board(
        canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.info_mode
    )
    if app.info_mode:
        canvas.create_text(app.width / 2, 12, text=f"{app.direction}")
        canvas.create_text(app.width / 2 + 50, 12, text=f"{app.state}")
    if app.state == "gameover":
        canvas.create_text(
            app.width / 2 + 50, app.height / 2, text="Game Over", font=("Arial", 24)
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
