from codefiles.classes.car import Car
from codefiles.classes.board import Board
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from colorhash import ColorHash


def grid_visual(game: Board) -> None:
    fig, ax = plt.subplots()
    plt.axis('off')
    plt.xlim([0, game.get_dim()])
    plt.ylim([0, game.get_dim()])

    for i in range(0, game.get_dim() + 1):
        plt.axvline(x = i, color = "0.55")
        plt.axhline(y = i, color = "0.55")

    for car in game.get_cars():
        if car.get_orientation() == "H":
            vehicle = Rectangle((car.get_col() - 1, game.get_dim() - car.get_row()), width = car.get_length(), height = 1, color = game.get_color_dict()[car.get_name()], zorder = 2)
            x = vehicle.get_xy()[0] + vehicle.get_width()/2
            y = vehicle.get_xy()[1] + vehicle.get_height()/2
            ax.annotate(car.get_name(), (x, y), color = 'w', fontsize = 15, ha = 'center', va = 'center')
            ax.add_patch(vehicle)
        else:
            vehicle = Rectangle((car.get_col() - 1, game.get_dim() - car.get_row() + 1), width = 1, height = -car.get_length(), color = game.get_color_dict()[car.get_name()], zorder = 2)
            x = vehicle.get_xy()[0] + vehicle.get_width()/2
            y = vehicle.get_xy()[1] + vehicle.get_height()/2
            ax.annotate(car.get_name(), (x, y), color = 'w', fontsize = 15, ha = 'center', va = 'center')
            ax.add_patch(vehicle)

    plt.show()

# Voeg toe aan elk algoritme na runtime
def write_statistics(algorithm, iterations):
    with open("statistics.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(algorithm, iterations)

def load_statistics():
    with open("statistics.csv", 'r') as f:
        next(f)
        for line in f:
            f.readline().split()
        data = [line[0], line[1]]


def stat(algorithm):
    for stats in data:
        if data[stats][0] == algorithm:
            fig, ax = plt.subplot()
