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


#---------------------------------------------------------------- not completed functions
#resets the whole game
def reset():
    global blocked_boxes, player, computer, winner, game_stopped, on_turn, cross_count, case

    # TODO: Sieh dir an, wie die globalen Variablen vorweg definiert wurden. Nach einem Reset sollen sie genau die gleichen Werte besitzen.
    #       Resette die globalen Variablen blocked_boxes, player, computer, winner, game_stopped, on_turn, cross_count und case
    # blocked_boxes = 
    # computer = 
    # player = 
    # on_turn = 
    # cross_count = 
    # case = 
    # winner = 
    # game_stopped =  

    draw_boxes()
    draw_on_turn()


#computer chooses the case
def computer_on_turn():
    if case == MIDDLE:
        # TODO: Rufe die Funktion auf, die den Fall für die Mitte behandelt (case_middle)
        #       Lösche pass
        pass
    # TODO: Ergänze die weiteren Bedingungen (elif und else) für EDGE und andere Fälle
    #       Rufe jeweils die gewünschte Funktion bei den einzelnen Fällen auf
    #       Lösche pass
    #elif case ==   :
        
    else:
        pass
         

#computer sets final cross to win
def computer_wins():
    #Es gibt neun Möglichkeiten, dass der Computer ein Kreuz setzt. Im Folgenden werden alle Möglichkeiten abgefragt,
    #ob es möglich ist, dass der Computer das finale Kreuz setzt.
    #Siehe dir im examble.txt file an, wann die Items der globalen Listen den Wert 1 bzw. den Wert 0 besitzen
    
    #Erste if-Abfrage: Wenn Computer bereits OM und OR oder ML und UL oder UR und MM gesetzt hat 
    #und die Box OL noch nicht blockiert ist, setzt der Computer OL sein Kreuz und gewinnt.
    if (computer[1] and computer[2] or computer[3] and computer[6] or computer[8] and computer[4]) and not blocked_boxes[0]:
        computer_clicks(OL)
    elif (computer[1] and computer[0] or computer[5] and computer[8] or computer[6] and computer[4]) and not blocked_boxes[2]:
        # TODO: Rufe die Funktion auf, die ein Kreuz OR setzt
        #       Lösche pass
        pass
    elif (computer[6] and computer[7] or computer[2] and computer[5] or computer[0] and computer[4]) and not blocked_boxes[8]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    elif (computer[2] and computer[0] or computer[4] and computer[7]) and not blocked_boxes[1]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    elif (computer[6] and computer[0] or computer[4] and computer[5]) and not blocked_boxes[3]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    elif (computer[1] and computer[7] or computer[3] and computer[5] or computer[0] and computer[8] or computer[2] and computer[6]) and not blocked_boxes[4]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    # TODO: Es wurde auf drei Möglichkeiten vergessen. Ergänze die beiden elif-Abfragen. Achte auf alle Fälle


    

#computer has to defend when player is one cross away to win
def computer_defends():
    #Es gibt neun Möglichkeiten, dass der Computer ein Kreuz setzt. Im Folgenden werden alle Möglichkeiten abgefragt,
    #ob es nötig ist, dass der Computer den Gewinn des Gegners abwehrt.
    #Siehe dir im examble.txt file an, wann die Items der globalen Listen den Wert 1 bzw. den Wert 0 besitzen
    
    #Erste if-Abfrage: Wenn Spieler bereits OM und OR oder ML und UL oder UR und MM gesetzt hat 
    #und die Box OL noch nicht blockiert ist, setzt der Computer OL sein Kreuz und wehrt ab.
    if (player[2] and player[1] or player[3] and player[6] or player[4] and player[8]) and not blocked_boxes[0]:
        computer_clicks(OL)
    elif (player[0] and player[1] or player[5] and player[8] or player[4] and player[6]) and not blocked_boxes[2]:
        # TODO: Rufe die Funktion auf, die ein Kreuz OR setzt
        #       Lösche pass
        pass
    elif (player[2] and player[5] or player[6] and player[7] or player[4] and player[0]) and not blocked_boxes[8]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    elif (player[0] and player[3] or player[7] and player[8] or player[4] and player[2]) and not blocked_boxes[6]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    elif (player[2] and player[0] or player[4] and player[7]) and not blocked_boxes[1]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    elif (player[2] and player[6] or player[0] and player[8] or player[3] and player[5] or player[1] and player[7]) and not blocked_boxes[4]:
        # TODO: Rufe die passende Funktion auf
        #       Lösche pass
        pass
    # TODO: Es wurde auf drei Möglichkeiten vergessen. Ergänze die beiden elif-Abfragen. Achte auf alle Fälle


# Je nachdem wohin der / die SpielerIn das erste Kreuz setzt, 
# hängt der zu betrachtende Fall ab. Im analogen Unterricht wurde herausgefunden, 
# dass der Computer bei Fall Mitte und Fall Rand bereits nach 
# seinem ersten Kreuz nicht mehr verlieren kann. Bei Fall Ecke 
# muss der Computer auch bei seinem zweiten Kreuz aufpassen.
# In jeder Runde, wenn der Computer an der Reihe ist, wird der 
# jeweilige Fall aufgerufen. Wurden bereits mehr als ein bzw. 
# drei Kreuze gesetzt wurde immer folgendem Schema nachgegangen:

# Computer siegt
# Wenn nicht -> Computer wehrt ab
# Wenn nicht -> Computer spielt weiter auf Sieg


#computer works out case middle
def case_middle():
    # TODO: Bringe folgende Funktionen in die richtige Reihenfolge und verschiebe sie an die Stellen,
    #       an denen pass steht.
    #       Lösche pass
    #
    #computer_clicks(OR)
    #computer_wins()
    #computer_defends()
    #computer_plays_to_win()
    if cross_count == 1:
        pass
    else:
        pass
        if on_turn == COMPUTER:
            pass
        if on_turn == COMPUTER:
            pass


#computer works out case edge
def case_edge():
    if cross_count == 1:
        # TODO: Rufe die Funktion auf, die ein Kreuz MM setzt
        #       Lösche pass
        pass
    else:
        # TODO: Gehe folgendem Schema nach:
        #       Computer Siegt 
        #       Wenn nicht -> Computer wehrt ab
        #       Wenn nicht -> Computer spielt  weiter auf Sieg
        #       Vergleiche mit der Funktion case_middle()
        #       Lösche pass
        pass


#computer works out case corner
def case_corner():
    # TODO: Bringe folgende Funktionen in die richtige Reihenfolge und verschiebe sie an die Stellen,
    #       an denen pass steht.
    #       Lösche pass
    #
    #computer_clicks(MM)
    #computer_puts_second_cross_on_edge()
    #computer_wins()
    #computer_defends()
    #computer_plays_to_win()

    if cross_count == 1:
        pass
    else:
        if cross_count == 3:
            pass
        else:
            pass
            if on_turn == COMPUTER:
                pass
            if on_turn == COMPUTER:
                pass


#checks if computer won
def check_computer_wins():
    global computer, winner
    #Es gibt acht Möglichkeiten, dass der Computer gewinnt. Im Folgenden werden alle Möglichkeiten abgefragt,
    #ob der Computer gewonnen hat.
    #Siehe dir im examble.txt file an, wann die Items der globalen Listen den Wert 1 bzw. den Wert 0 besitzen

    # TODO: Es werden erst sieben Fälle betrachtet. Erweitere die if-Abfrage mit den anderen sieben Fällen.
    if computer[0] and computer[1] and computer[2]:
        winner = COMPUTER_WINS


#checks if player won
def check_player_wins():
    global player, winner

    #Es gibt acht Möglichkeiten, dass der Spieler gewinnt. 
    #Siehe dir im examble.txt file an, wann die Items der globalen Listen den Wert 1 bzw. den Wert 0 besitzen

    # TODO: Frage alle Möglichkeiten ab, ob der Spieler gewonnen hat.
    #       Setzte winner = SPIELER_WINS
    #       Lösche pass
    #       Gleiche Funktion wie_check_computer_wins. Anstelle von computer wird nun die player Liste betrachtet.
    pass


#checks draw
def check_draw():
    global blocked_boxes, winner

    #Wurden alle Kreuze gesetzt und gibt es keinen Gewinner, so endet die Partie mit einem Unentschieden
    #Siehe dir im examble.txt file an, wann die Items der globalen Listen den Wert 1 bzw. den Wert 0 besitzen

    # TODO: Erstelle eine if-Abfrage, die überprüft, ob alle Boxen belegt sind.
    #       Ist dies der Fall, setzte winner auf NO_WINNER
    #       Lösche pass
    pass
    


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
