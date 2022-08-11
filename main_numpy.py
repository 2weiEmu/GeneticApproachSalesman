from turtle import distance
from main import MUTATE_PERCENTAGE, TRUNCATE_AMOUNT, distance_table
from random import randint
import cProfile, pstats

import numpy as np

def format_distance_table(distance_table):
    out_table : list = []
    for c in distance_table:

        c = [int(k) for k in c[0].split(" ")]
        out_table.append(c)
    
    return out_table

distance_table = distance_table


ITERATIONS = 200
ROUTE_SET = 1024
TRUNCATE_AMOUNT = 0.4
MUTATE_SWAP = 1
MUTATE_PERCENTAGE = 0.1

def main():
    new_distance_table = format_distance_table(distance_table)

    route_list = np.array([ROUTE_SET,2])


if __name__ == "__main__":

    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.dump_stats("out.prof")
    stats.print_stats()