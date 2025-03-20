import turtle
from abc import abstractmethod, ABCMeta

import screen

#------------------------------------------------------------------ constants
#constants for the screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1050

HORIZONTAL_BORDER_DISTANCE = 100
VERTICAL_BORDER_DISTANCE = 100

BORDER_LEFT = -SCREEN_WIDTH / 2 + HORIZONTAL_BORDER_DISTANCE
BORDER_RIGHT = SCREEN_WIDTH / 2 - HORIZONTAL_BORDER_DISTANCE
BORDER_TOP = SCREEN_HEIGHT / 2 - VERTICAL_BORDER_DISTANCE
BORDER_BOTTOM = -SCREEN_HEIGHT / 2 + VERTICAL_BORDER_DISTANCE
PLAYFIELD_BOTTOM = BORDER_BOTTOM + 150

BOX_LENGTH = 200

DISTANCE = BOX_LENGTH + 30
PLAYFIELD_LEFT = BORDER_LEFT + 20
PLAYFIELD_TOP = BORDER_TOP - 20

#constants for the nine fields
LIST_X = [PLAYFIELD_LEFT, PLAYFIELD_LEFT + DISTANCE, PLAYFIELD_LEFT + DISTANCE * 2]
LIST_Y = [PLAYFIELD_TOP, PLAYFIELD_TOP - DISTANCE, PLAYFIELD_TOP - DISTANCE * 2]
OL = [PLAYFIELD_LEFT, PLAYFIELD_TOP, 0]
OM = [PLAYFIELD_LEFT + DISTANCE, PLAYFIELD_TOP, 1]
OR = [PLAYFIELD_LEFT + DISTANCE * 2, PLAYFIELD_TOP, 2]
ML = [PLAYFIELD_LEFT, PLAYFIELD_TOP - DISTANCE, 3]
MM = [PLAYFIELD_LEFT + DISTANCE, PLAYFIELD_TOP - DISTANCE, 4]
MR = [PLAYFIELD_LEFT + DISTANCE * 2, PLAYFIELD_TOP - DISTANCE, 5]
UL = [PLAYFIELD_LEFT, PLAYFIELD_TOP - DISTANCE * 2, 6]
UM = [PLAYFIELD_LEFT + DISTANCE, PLAYFIELD_TOP - DISTANCE * 2, 7]
UR = [PLAYFIELD_LEFT + DISTANCE * 2, PLAYFIELD_TOP - DISTANCE * 2, 8]

#constants for on turn logic
PLAYER = 1
COMPUTER = 0
COLORS = ['red', 'blue']
PLAYERS = ['Computer', 'Player']

#constants for winner logic
IN_GAME = 2
COMPUTER_WINS = 0
PLAYER_WINS = 1
NO_WINNER = 3

#constants for case spliting 
MIDDLE = 0
CORNER = 1
EDGE = 2
ND = 4




#--------------------------------------------------------------- global variables
#shows who is on turn
on_turn = PLAYER

#game is stopped while new box appeares
pause = 0

#computer or player can win or there is a draw. while there is no winner or draw one is in game
winner = IN_GAME

#after someone wins a field cannot be clicked. the game has to restart
game_stopped = 0

#counts how many fields are clicked
cross_count = 0

#after first field is clicked case is either middle, corner or edge. at start case is not defined
case = ND


#lists for the nine fields
#item in blocked_boxes is set to 1 if player or computer clicks field
blocked_boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#item in computer is set to 1 if computer clicks field
computer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#item in player is set to 1 if player clicks field
player = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#turtle variables for the graphics
on_turn_turtle = turtle.Turtle()
reset_button_turtle = turtle.Turtle()
writing_turtle = turtle.Turtle()


#---------------------------------------------------------------- not completed funcitons
#computer sets final cross to win
def computer_wins():
    if (computer[1] and computer[2] or computer[3] and computer[6] or computer[8] and computer[4]) and not blocked_boxes[0]:
        computer_clicks(OL)
    elif (computer[1] and computer[0] or computer[5] and computer[8] or computer[6] and computer[4]) and not blocked_boxes[2]:
        computer_clicks(OR)
    elif (computer[7] and computer[8] or computer[3] and computer[0] or computer[2] and computer[4]) and not blocked_boxes[6]:
        computer_clicks(UL)
    elif (computer[6] and computer[7] or computer[2] and computer[5] or computer[0] and computer[4]) and not blocked_boxes[8]:
        computer_clicks(UR)
    elif (computer[2] and computer[0] or computer[4] and computer[7]) and not blocked_boxes[1]:
        computer_clicks(OM)
    elif (computer[6] and computer[0] or computer[4] and computer[5]) and not blocked_boxes[3]:
        computer_clicks(ML)
    elif (computer[2] and computer[8] or computer[4] and computer[3]) and not blocked_boxes[5]:
        computer_clicks(MR)
    elif (computer[6] and computer[8] or computer[4] and computer[1]) and not blocked_boxes[7]:
        computer_clicks(UM)
    elif (computer[1] and computer[7] or computer[3] and computer[5] or computer[0] and computer[8] or computer[2] and computer[6]) and not blocked_boxes[4]:
        computer_clicks(MM)
    
#computer has to defend when player is one cross away to win
def computer_defends():
    if (player[2] and player[1] or player[3] and player[6] or player[4] and player[8]) and not blocked_boxes[0]:
        computer_clicks(OL)
    elif (player[0] and player[1] or player[5] and player[8] or player[4] and player[6]) and not blocked_boxes[2]:
        computer_clicks(OR)
    elif (player[2] and player[5] or player[6] and player[7] or player[4] and player[0]) and not blocked_boxes[8]:
        computer_clicks(UR)
    elif (player[0] and player[3] or player[7] and player[8] or player[4] and player[2]) and not blocked_boxes[6]:
        computer_clicks(UL)
    elif (player[2] and player[0] or player[4] and player[7]) and not blocked_boxes[1]:
        computer_clicks(OM)
    elif (player[6] and player[0] or player[4] and player[5]) and not blocked_boxes[3]:
        computer_clicks(ML)
    elif (player[2] and player[8] or player[4] and player[3]) and not blocked_boxes[5]:
        computer_clicks(MR)
    elif (player[6] and player[8] or player[4] and player[1]) and not blocked_boxes[7]:
        computer_clicks(UM)
    elif (player[2] and player[6] or player[0] and player[8] or player[3] and player[5] or player[1] and player[7]) and not blocked_boxes[4]:
        computer_clicks(MM)

#computer works out case middle
def case_middle():
    if cross_count == 1:
        computer_clicks(OR)
    else:
        computer_wins()
        if on_turn == COMPUTER:
            computer_defends()
        if on_turn == COMPUTER:
            computer_plays_to_win()

#computer works out case edge
def case_edge():
    if cross_count == 1:
        computer_clicks(MM)
    else:
        computer_wins()
        if on_turn == COMPUTER:
            computer_defends()
        if on_turn == COMPUTER:
            computer_plays_to_win()

#computer works out case corner
def case_corner():
    if cross_count == 1:
        computer_clicks(MM)
    else:
        if cross_count == 3:
            computer_puts_second_cross_on_edge()
        else:
            computer_wins()
            if on_turn == COMPUTER:
                computer_defends()
            if on_turn == COMPUTER:
                computer_plays_to_win()

#computer chooses the case
def computer_on_turn():
    if case == MIDDLE:
        case_middle()
    elif case == EDGE:
        case_edge()
    else:
        case_corner() 

#resets the whole game
def reset():
    global blocked_boxes, player, computer, winner, game_stopped, on_turn, cross_count, case

    blocked_boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    computer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    on_turn = PLAYER
    cross_count = 0
    case = ND
    winner = IN_GAME
    game_stopped = 0

    draw_boxes()
    draw_on_turn()

#checks if computer won
def check_computer_wins():
    global computer, winner

    if computer[0] and computer[1] and computer[2] or \
            computer[3] and computer[4] and computer[5] or \
            computer[6] and computer[7] and computer[8] or \
            computer[0] and computer[3] and computer[6] or \
            computer[1] and computer[4] and computer[7] or \
            computer[2] and computer[5] and computer[8] or \
            computer[0] and computer[4] and computer[8] or \
            computer[2] and computer[4] and computer[6]:
        winner = COMPUTER_WINS

#checks if player won
def check_player_wins():
    global player, winner

    if player[0] and player[1] and player[2] or \
            player[3] and player[4] and player[5] or \
            player[6] and player[7] and player[8] or \
            player[0] and player[3] and player[6] or \
            player[1] and player[4] and player[7] or \
            player[2] and player[5] and player[8] or \
            player[0] and player[4] and player[8] or \
            player[2] and player[4] and player[6]:
        winner = PLAYER_WINS

#checks draw
def check_draw():
    global blocked_boxes, winner

    if blocked_boxes[0] and blocked_boxes[1] and blocked_boxes[2] and \
            blocked_boxes[3] and blocked_boxes[4] and blocked_boxes[5] and \
            blocked_boxes[6] and blocked_boxes[7] and blocked_boxes[8]:
        winner = NO_WINNER
    


#---------------------------------------------------------------- completed functions
#logic for the second cross for case corner
def computer_puts_second_cross_on_edge():
    computer_defends()
    if on_turn == COMPUTER:
        if player[2] and player[6] or player[0] and player[8]:
            computer_clicks(MR)
        elif player[1] or player[7]:
            computer_clicks(MR)
        else:
            computer_clicks(UM)

#Computer can neither win nor defend - he keeps playing to win
def computer_plays_to_win():
    if case == MIDDLE:
        if not blocked_boxes[1]:
            computer_clicks(OM)
        elif not blocked_boxes[3]:
            computer_clicks(ML)
        elif not blocked_boxes[5]:
            computer_clicks(MR)
        else:
            computer_clicks(UM)
    elif case == EDGE:
        if player[3] and player[5] or player[1] and player[7]:
            computer_clicks(UL)
        elif player[3] and player[1] or player[5] and player[7]:
            computer_clicks(OR)
        else:
            computer_clicks(OL)
    elif case == CORNER:
        if not blocked_boxes[0]:
            computer_clicks(OL)
        elif not blocked_boxes[2]:
            computer_clicks(OR)
        else:
            computer_clicks(UR)

#draws the winner
def draw_winner():
    global winner, game_stopped, on_turn_turtle 

    game_stopped = 1
    on_turn_turtle.hideturtle()
    on_turn_turtle.clear()
    on_turn_turtle.penup()
    on_turn_turtle.goto(-320, -350)

    if winner != NO_WINNER:
        on_turn_turtle.color(COLORS[winner])
        if winner == COMPUTER_WINS:
            on_turn_turtle.write("Winner: Computer", font=("Arial", 35, "bold"))
        else:
            on_turn_turtle.write("Winner: Player", font=("Arial", 35, "bold"))
    else:
        on_turn_turtle.color("brown")
        on_turn_turtle.write("No Winner", font=("Arial", 35, "bold"))

#checks if somebody won
def check_winner():
    check_player_wins()
    check_computer_wins()
    check_draw()

    if winner != IN_GAME:
        draw_winner()

#draws field in computer color when computer clicked a field
def computer_clicks(field):
    global on_turn, blocked_boxes, pause, on_turn_turtle, cross_count, case
    
    turtle.register_shape("box", ((0, 0), (0, BOX_LENGTH), (BOX_LENGTH, BOX_LENGTH), (BOX_LENGTH, 0), (0, 0)))

    pause = 1
    box = turtle.Turtle()
    box.shape("box")
    box.color(COLORS[on_turn])
    box.penup()
    box.goto(field[0], field[1])
    computer[field[2]] = 1
    change_color()
    blocked_boxes[field[2]] = 1
    on_turn_turtle.clear()
    draw_on_turn()
    pause = 0
    check_winner()                         
    cross_count += 1 

#changes the color when box was clicked
def change_color():
    global on_turn
    if on_turn == COMPUTER:
        on_turn = PLAYER
    else:
        on_turn = COMPUTER

#colors a box in the player's color
def box_is_clicked(x, y):
    global on_turn, blocked_boxes, pause, on_turn_turtle, cross_count, case, winner

    if on_turn == PLAYER:
        distance = BOX_LENGTH + 30
        border_left = BORDER_LEFT + 20
        border_top = BORDER_TOP - 20

        list_x = [border_left, border_left + distance, border_left + distance * 2]
        list_y = [border_top, border_top - distance, border_top - distance * 2]
        turtle.register_shape("box", ((0, 0), (0, BOX_LENGTH), (BOX_LENGTH, BOX_LENGTH), (BOX_LENGTH, 0), (0, 0)))

        number = 0
        for y_coordinate in list_y:
            for x_coordinate in list_x:
                if x_coordinate <= x <= x_coordinate + BOX_LENGTH and y_coordinate >= y >= y_coordinate - BOX_LENGTH:
                    if blocked_boxes[number] == 0 and pause == 0 and game_stopped == 0:
                        pause = 1
                        box = turtle.Turtle()
                        box.shape("box")
                        box.color(COLORS[on_turn])
                        box.penup()
                        box.goto(x_coordinate, y_coordinate)
                        
                        if cross_count == 0:
                            if number == 0 or number == 2 or number == 6 or number == 8:
                                case = CORNER
                            elif number == 4:
                                case = MIDDLE
                            else:
                                case = EDGE                           
                        cross_count += 1 

                        player[number] = 1
                        change_color()
                        blocked_boxes[number] = 1
                        on_turn_turtle.clear()
                        check_winner()
                        if winner == IN_GAME:
                            draw_on_turn()
                        pause = 0
                number += 1

#draws who is on the turn
def draw_on_turn():
    global on_turn, on_turn_turtle 

    on_turn_turtle.clear()
    on_turn_turtle.hideturtle()
    on_turn_turtle.penup()
    on_turn_turtle.goto(-320, -350)
    on_turn_turtle.color(COLORS[on_turn])
    on_turn_turtle.write("On Turn: " + str(PLAYERS[on_turn]), font=("Arial", 35, "bold"))

    if on_turn == COMPUTER:
        computer_on_turn()

#draws the boxes
def draw_boxes():
    global pause, computer, player

    turtle.register_shape("box", ((0, 0), (0, BOX_LENGTH), (BOX_LENGTH, BOX_LENGTH), (BOX_LENGTH, 0), (0, 0)))

    pause = 1

    number = 0
    for y_coordinate in LIST_Y:
        for x_coordinate in LIST_X:
            if computer[number] == 1:
                col = "red"
            elif player[number] == 1:
                col = "blue"
            else:
                col = "black"

            box = turtle.Turtle()
            box.shape("box")
            box.color(col)
            box.penup()
            box.goto(x_coordinate, y_coordinate)
            number += 1
    pause = 0

#draws the buttons
def draw_buttons():
    global reset_button_turtle, writing_turtle

    button_designs = [['turtle', 'brown', 280, -330, 4, 280, -390, "Reset", reset, reset_button_turtle]]

    for design in button_designs:
        design[9].shape(design[0])
        design[9].fillcolor(design[1])
        design[9].penup()
        design[9].goto(design[2], design[3])
        design[9].shapesize(design[4])
        design[9].showturtle()
        writing_turtle.penup()
        writing_turtle.goto(design[5], design[6])
        writing_turtle.write(design[7], align='center', font=('Arial', 12, 'bold'))
        design[9].onclick(design[8])

#draws the play area
def draw_screen(screen):
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)

    play_area = turtle.Turtle()
    play_area.hideturtle()
    play_area.speed(10)
    play_area.penup()
    play_area.goto(BORDER_LEFT, BORDER_BOTTOM)
    play_area.pendown()
    play_area.goto(BORDER_RIGHT, BORDER_BOTTOM)
    play_area.goto(BORDER_RIGHT, BORDER_TOP)
    play_area.goto(BORDER_LEFT, BORDER_TOP)
    play_area.goto(BORDER_LEFT, BORDER_BOTTOM)
    play_area.goto(BORDER_LEFT, PLAYFIELD_BOTTOM)
    play_area.goto(BORDER_RIGHT, PLAYFIELD_BOTTOM)

#hides all turtles
def hide_turtles():
    global on_turn_turtle, reset_button_turtle, writing_turtle

    on_turn_turtle.hideturtle()
    reset_button_turtle.hideturtle()
    writing_turtle.hideturtle()

#main function
def main():
    global player, red_player, blue_player

    hide_turtles()

    screen = turtle.Screen()

    draw_screen(screen)
    draw_boxes()
    draw_buttons()
    draw_on_turn()

    screen.onscreenclick(box_is_clicked, 1)
    screen.listen()

    while 1:
        screen.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
