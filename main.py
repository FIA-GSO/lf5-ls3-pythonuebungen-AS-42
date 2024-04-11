# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# ---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int, int, int]:
    """
        Computes the r2d2 population for the given step amount
    :param steps: amount of steps to compute the population (e.g.: 5)
    :return: tuple of childs adults and old r2d2
    """

    anzahl_jung = 10
    anzahl_erwachsen = 10
    anzahl_alt = 10

    for step in range(steps):
        anzahl_neu_jung = (anzahl_erwachsen * 4) + (anzahl_alt * 2)
        anzahl_alt = int(anzahl_erwachsen / 3)
        anzahl_erwachsen = int(anzahl_jung / 2)
        anzahl_jung = anzahl_neu_jung

    return anzahl_jung, anzahl_erwachsen, anzahl_alt


# ---------------------Aufgabe 2 Streichholz------------------------------
# IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE
def nimgame():
    nim_game_running = True

    streichholz = 29
    while nim_game_running:
        input(f"Es sind {streichholz} Streichhölzer übrig. Ziehen Sie 1-6!")
        streichholz = streichholz - 7
        if streichholz == 1:
            print("Es ist nur noch 1 Streichholz übrig, welches du ziehen musst. Du hast verloren")
            nim_game_running = False


# ---------------------Aufgabe 3 Heron ------------------------------------
def heron_verfahren(area: float, threshold: float) -> float:
    """
        computes the square root using the heron method
    :param area: size of the area e.g.25
    :param threshold: threshold for the heron method e.g. 0.01
    :return:the square root of the given area according to the heron method
    """

    laenge_a = area
    laenge_b = 1
    mittelwert = 13
    abweichung = 24

    while (abweichung >= threshold):
        laenge_a = mittelwert
        laenge_b = area / laenge_a
        abweichung = laenge_a - laenge_b
        mittelwert = (laenge_a + laenge_b) / 2

    return laenge_a


# ---------------------Aufgabe 4 Quersumme------------------------------
# IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


# ---------------MANAGEMENT----------------------
# -------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    print(f"""
        # R2D2 Population after 5 steps is: 
        # Young: {compute_r2d2_population(5)[0]}
        # Adults: {compute_r2d2_population(5)[1]}
        # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    # TO BE IMPLEMENTED

    # Aufgabe 3
    print(f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
