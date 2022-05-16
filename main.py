from random import randint
import os
import cProfile

distance_table = [["0 94 76 141 91 60 120 145 91 74 90 55 145 108 41 49 33 151 69 111 24"], 
 ["94 0 156 231 64 93 108 68 37 150 130 57 233 26 62 140 61 229 120 57 109"],
 ["76 156 0 80 167 133 124 216 137 114 154 100 141 161 116 37 100 169 49 185 84"], 
 ["141 231 80 0 229 185 201 286 216 139 192 178 113 239 182 92 171 155 128 251 137"], 
 ["91 64 167 229 0 49 163 65 96 114 76 93 200 91 51 139 72 185 148 26 92"], 
 ["60 93 133 185 49 0 165 115 112 65 39 91 151 117 39 99 61 139 128 75 49"], 
 ["120 108 124 201 163 165 0 173 71 194 203 74 254 90 127 136 104 269 75 163 144"], 
 ["145 68 216 286 65 115 173 0 103 179 139 123 265 83 104 194 116 250 186 39 152"], 
 ["91 37 137 216 96 112 71 103 0 160 151 39 236 25 75 130 61 239 95 93 112"],
 ["74 150 114 139 114 65 194 179 160 0 54 127 86 171 89 77 99 80 134 140 50"],
 ["90 130 154 192 76 39 203 139 151 54 0 129 133 155 78 117 99 111 159 101 71"],
 ["55 57 100 178 93 91 74 123 39 127 129 0 199 61 53 91 30 206 63 101 78"],
 ["145 233 141 113 200 151 254 265 236 86 133 199 0 251 171 118 176 46 182 226 125"],
 ["108 26 161 239 91 117 90 83 25 171 155 61 251 0 83 151 75 251 119 81 127"],
 ["41 62 116 182 51 39 127 104 75 89 78 53 171 83 0 90 24 168 99 69 49"],
 ["49 140 37 92 139 99 136 194 130 77 117 91 118 151 90 0 80 139 65 159 50"],
 ["33 61 100 171 72 61 104 116 61 99 99 30 176 75 24 80 0 179 76 86 52"],
 ["151 229 169 155 185 139 269 250 239 80 111 206 46 251 168 139 179 0 202 211 128"],
 ["69 120 49 128 148 128 75 186 95 134 159 63 182 119 99 65 76 202 0 161 90"],
 ["111 57 185 251 26 75 163 39 93 140 101 101 226 81 69 159 86 211 161 0 115"],
 ["24 109 84 137 92 49 144 152 112 50 71 78 125 127 49 50 52 128 90 115 0"]]


def format_distance_table(distance_table):
    out_table : list = []
    for c in distance_table:

        c = [int(k) for k in c[0].split(" ")]
        out_table.append(c)
    
    return out_table

class Tour:

    def __init__(self, distance_table):
        # Random Tour generated on creation

        self.tour_route : list = [0]
        while (len(self.tour_route)) < 21:
            number = randint(1, 20)
            if number in self.tour_route:
                continue
            else:
                self.tour_route.append(number)
        self.tour_route.append(0)
        
        self.route_length : int = 0
        for x in range(len(self.tour_route) - 1):
            self.route_length += distance_table[self.tour_route[x]][self.tour_route[x+1]]

    def __repr__(self):
        temp = [str(k) for k in self.tour_route]
        return " ".join(temp) + "+++" + str(self.route_length) + "\n"


    def update_route_length(self, distance_table):
        self.route_length = 0
        for x in range(len(self.tour_route) - 1):
            self.route_length += distance_table[self.tour_route[x]][self.tour_route[x+1]]

    def check_if_valid(self):
        count = 0
        for x in range(1, 21):
            temp_count = 0
            temp_count += self.tour_route.count(x)
            if temp_count > 1:
                print("Counted Too many of 1")
                exit()
            
            count += temp_count
        
        if self.tour_route[0] != 0 or self.tour_route[-1] != 0:
            print("Not valid endpoint(s)")
            exit()

def truncate_select(set, lose_percent):
    leng = len(set)
    drop = int(leng - (leng * lose_percent))
    return set[:drop]

def order_crossover_set(set, meant_length, dist_table):
    needed: int = meant_length - len(set)

    for x in range(needed):
        new_tour = Tour(dist_table)
        
        order_cross_route = [" " for x in range(22)]
        order_cross_route[0] = 0
        order_cross_route[-1] = 0
        start = randint(1,10)
        end = randint(11,20) 

        random_tour_1 = set[randint(0, len(set)) - 1]
        random_tour_2 = set[randint(0, len(set)) - 1]

        order_cross_route[start:end] = random_tour_1.tour_route[start:end]
        for j in range(end, end+len(order_cross_route)):
            counter = end
            if order_cross_route[j%22] == " ":
                iter_route = iter(random_tour_2.tour_route)
                while True:
                    
                    insert = random_tour_2.tour_route[counter%22]
                    if counter > 50:
                        exit()
                    if insert in order_cross_route:
                        counter += 1
                        insert = random_tour_2.tour_route[counter%22]
                    else:
                        order_cross_route[j%22] = insert
                        break

        if len(order_cross_route) < 22:
            print("CROSS ARRAY TOO SMALL")
            exit()
        if order_cross_route[0] != 0 or order_cross_route[-1] != 0:
            print("ROUTE DOES NOT FINISH VALID")
            exit()
        new_tour.tour_route = order_cross_route
        new_tour.update_route_length(dist_table)
        set.append(new_tour)
    
    return set
                    
def mutate_set(set, swap_amount, mutate_percent):
    for x in range(int(mutate_percent * len(set))):

        random_tour = set[randint(0, len(set) - 1)]
        swap_1 = randint(1,20)
        swap_2 = randint(1,20)
        
        random_tour.tour_route[swap_1], random_tour.tour_route[swap_2] = random_tour.tour_route[swap_2], random_tour.tour_route[swap_1]
    
    return set



ITERATIONS = 250
ROUTE_SET = 2048 # 2^13

def main():
    
    # Initialise Set
    distance_table_new = format_distance_table(distance_table)
    os.system("cls")

    print("Generating and Initialising Routes...")

    route_list : list = [Tour(distance_table_new) for c in range(ROUTE_SET)]
    print("Finished Generating and Initialising Routes.")

    ultimate_smallest : int = route_list[0].route_length
    ultimate_smallest_tour = []
    print("Beginning Calculations...\n\n\n")
    for x in range(ITERATIONS):
        
        smallest = route_list[0].route_length

        smallest_idx = 0
        for count, tour in enumerate(route_list):
            if tour.route_length < smallest:
                smallest = tour.route_length
                smallest_idx = count

        if smallest < ultimate_smallest: 
            ultimate_smallest = smallest
            ultimate_smallest_tour = route_list[smallest_idx]

        sum_route_length = 0
        for tour in route_list:
            sum_route_length += tour.route_length
        
        average_set_length = sum_route_length/len(route_list)

        for tour in route_list:
            tour.check_if_valid()

        # Progress Bar
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        for j in range(3): print(LINE_UP, end=LINE_CLEAR)
        print("|" + ((1 + int((x/ITERATIONS) * 100)) * ("\u2588")) + ((100 - int((x/ITERATIONS)*100) - 1) * " ") + "|", str(100 * x/ITERATIONS).rjust(4)+"%")
        print("Smallest Length:", str(smallest).rjust(5), "Set Length:", str(len(route_list)).rjust(6))
        print("Ultimate Smallest Length:", str(ultimate_smallest).rjust(5), "Average Length of Set:", str(average_set_length).rjust(5))

        # === Evaluate ===
        for tour in route_list:
            tour.update_route_length(distance_table_new)
        # Sort Tour Set by fitness value

        for j in range(len(route_list)):
            for i in range(len(route_list) - 1):

                if route_list[i].route_length > route_list[i+1].route_length:
                    route_list[i], route_list[i+1] = route_list[i+1], route_list[i]

        # === Select ===
        # Select Tours
        route_list = truncate_select(route_list, 0.4)

        # === Crossover ===
        # Crossover Old Tours, and keep originals
        route_list = order_crossover_set(route_list, ROUTE_SET, distance_table_new)

        # === Mutation ===
        # Mutate Tours
        route_list = mutate_set(route_list, 1, 0.1)

        # Output Shortest Tour Found

    print("\nGenetic Calculations Complete.")
    # Sort Tour set by fitness value
    
    # Output Best Tour
    ultimate_smallest_tour.update_route_length(distance_table_new)
    print("Shortest Route:", ultimate_smallest_tour)

    f = open("saves.txt", 'w')
    f.writelines("Length: " + str(ultimate_smallest) +  "| Tour: " + str(ultimate_smallest_tour)) 
    f.close

if __name__ == "__main__":
    cProfile.run('main()')