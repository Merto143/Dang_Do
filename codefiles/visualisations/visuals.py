from codefiles.classes.car import Car
from codefiles.classes.board import Board
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from colorhash import ColorHash
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


def write_random(time, visited_states, dim):
    with open("data/random.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time, visited_states, dim])

def write_breadth(time, visited_states, dim, path):
    with open("data/breadth.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time, visited_states, dim, path])

def write_randombreadth(time, visited_states, dim, path):
    with open("data/randombreadth.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time, visited_states, dim, path])

def write_depth(time, visited_states, dim, path):
    with open("data/depth.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time, visited_states, dim, path])

def write_beam(time, visited_states, dim, path):
    with open("data/beam.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([time, visited_states, dim, path])


def load_statistics(algorithm, dimension):

    data = []
    with open(f"data/{algorithm}.csv", 'r') as f:
        for line in f:
            list = line.strip().split(",")
            if list[2] == dimension:
                if not algorithm == "random":
                    data.append([float(list[0]), int(list[1]), int(list[3])])
                else:
                    data.append([float(list[0]), int(list[1])])
    return data


def histograms(algorithm, data, dimension):

    visited_states = []
    for i in range(len(data)):
        visited_states.append(data[i][1])
    plt.hist(visited_states, bins = round(len(data) ** (1/2)))
    plt.title(f"Histogram: '{algorithm}' {dimension}x{dimension}")
    plt.ylabel("Relative Frequency")
    plt.xlabel("Visited States")
    plt.show()

    time = []
    for j in range(len(data)):
        time.append(data[j][0])
    plt.hist(time, bins = round(len(data) ** (1/2)))
    plt.title(f"Histogram: '{algorithm}' {dimension}x{dimension}")
    plt.ylabel("Relative Frequency")
    plt.xlabel("Time elapsed (s)")
    plt.show()

    if algorithm != "breadth" and algorithm != "random":
        path = []
        for k in range(len(data)):
            path.append(data[k][2])
        plt.hist(path, bins = round(len(data) ** (1/2)))
        plt.title(f"Histogram: '{algorithm}' {dimension}x{dimension}")
        plt.ylabel("Relative Frequency")
        plt.xlabel("Shortest Path")
        plt.show()

def scatterplot(algorithm, data, dimension):

    algorithms = ["randombreadth", "breadth", "depth"]
    datalist = []
    for i in range(len(algorithms)):
        if not algorithms[i] == algorithm:
            datalist.append(load_statistics(algorithms[i], dimension))
        else:
            datalist.append(data)
        xaxis = []
        yaxis = []
        if not algorithms[i] == "random":
            for j in range(len(datalist[i])):
                xaxis.append(datalist[i][j][1])
                yaxis.append(datalist[i][j][-1])
            plt.xlabel("Visited States")
            plt.ylabel("Shortest Path")
            plt.xlim([250,650])
            plt.yscale("log")
            plt.scatter(xaxis, yaxis, c=ColorHash(algorithms[i]).hex)
    plt.show()

    if not algorithm == "random":
        dimensions = [6, 9, 12]
        datalist = [data]
        for i in range(len(dimensions)):
            if not dimensions[i] == dimension:
                datalist.append(load_statistics(algorithm, dimensions[i]))
            else:
                datalist.append(data)
            xaxis = []
            yaxis = []
            for j in range(len(datalist[i])):
                xaxis.append(datalist[i][j][1])
                yaxis.append(datalist[i][j][-1])
                plt.scatter(xaxis, yaxis, c="k")
                plt.xlabel("Visited States")
                plt.ylabel("Shortest Path")
        plt.show()
