from codefiles.classes.car import Car
from codefiles.classes.board import Board
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from colorhash import ColorHash
import time
import csv


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

def write_random(time, iterations, dim):
    with open("data/random.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time, iterations, dim])

# def write_breath(time, path):
#
# def write_randombreadth(time, length):
#
# def write_depth(time, iterations, length):
#
# def write_beam(time, iterations, length):



def load_statistics(algorithm, dimension):
    data = []
    with open(f"data/{algorithm}.csv", 'r') as f:
        line = f.readline()
        for line in f:
            list = line.strip().split(",")
            if list[2] == dimension:
                data.append([float(list[0]), int(list[1])])
    return data


def stat(algorithm, data):
    iterations = []
    for i in range(len(data)):
        iterations.append(data[i][1])
    plt.hist(iterations)
    plt.show()

    time = []
    for j in range(len(data)):
        time.append(data[j][0])
    plt.hist(time)
    plt.show()

    plt.scatter(iterations, time)
    plt.show()
