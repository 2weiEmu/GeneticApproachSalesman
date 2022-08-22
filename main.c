#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char distance_table[][] = {{"0 94 76 141 91 60 120 145 91 74 90 55 145 108 41 49 33 151 69 111 24"}, 
 {"94 0 156 231 64 93 108 68 37 150 130 57 233 26 62 140 61 229 120 57 109"},
 {"76 156 0 80 167 133 124 216 137 114 154 100 141 161 116 37 100 169 49 185 84"}, 
 {"141 231 80 0 229 185 201 286 216 139 192 178 113 239 182 92 171 155 128 251 137"}, 
 {"91 64 167 229 0 49 163 65 96 114 76 93 200 91 51 139 72 185 148 26 92"}, 
 {"60 93 133 185 49 0 165 115 112 65 39 91 151 117 39 99 61 139 128 75 49"}, 
 {"120 108 124 201 163 165 0 173 71 194 203 74 254 90 127 136 104 269 75 163 144"}, 
 {"145 68 216 286 65 115 173 0 103 179 139 123 265 83 104 194 116 250 186 39 152"}, 
 {"91 37 137 216 96 112 71 103 0 160 151 39 236 25 75 130 61 239 95 93 112"},
 {"74 150 114 139 114 65 194 179 160 0 54 127 86 171 89 77 99 80 134 140 50"},
 {"90 130 154 192 76 39 203 139 151 54 0 129 133 155 78 117 99 111 159 101 71"},
 {"55 57 100 178 93 91 74 123 39 127 129 0 199 61 53 91 30 206 63 101 78"},
 {"145 233 141 113 200 151 254 265 236 86 133 199 0 251 171 118 176 46 182 226 125"},
 {"108 26 161 239 91 117 90 83 25 171 155 61 251 0 83 151 75 251 119 81 127"},
 {"41 62 116 182 51 39 127 104 75 89 78 53 171 83 0 90 24 168 99 69 49"},
 {"49 140 37 92 139 99 136 194 130 77 117 91 118 151 90 0 80 139 65 159 50"},
 {"33 61 100 171 72 61 104 116 61 99 99 30 176 75 24 80 0 179 76 86 52"},
 {"151 229 169 155 185 139 269 250 239 80 111 206 46 251 168 139 179 0 202 211 128"},
 {"69 120 49 128 148 128 75 186 95 134 159 63 182 119 99 65 76 202 0 161 90"},
 {"111 57 185 251 26 75 163 39 93 140 101 101 226 81 69 159 86 211 161 0 115"},
 {"24 109 84 137 92 49 144 152 112 50 71 78 125 127 49 50 52 128 90 115 0"}}

struct Tour {
    int tour_route[22] = {0};
    int route_length;
}

int[][] format_distance_table(char[][] distance_table) {
    int out_table[21][21];
    for (int x = 0; x < 21; x++) {
        int add[21];

        char number_list[82] = distance_table[x];

        int num_len = sizeof(distance_table[x])/sizeof(char);
        for (int j = 0; j < num_len; j++) {

        }
    }
}

int random_integer(int lower, int upper) {
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}
bool is_in_list(int value, int[] list, int length) {
    for (int i = 0; i < length; i++) {
        if (list[i] == value) {
            return true;
        }
    }
    return false;
}

struct Tour tour_create_new(int[][] distance_table) {
    struct Tour out_tour;
    int tour_counter = 1;

    while (tour_counter) < 21 {
        int number = random_integer(0, 20);
        
        if not(is_in_list(number, out_tour.tour_route, 22)) {
            out_tour.tour_route[tour_counter] = number;
            tour_counter++;
        }
    } 
    out_tour.tour_route[tour_counter] = 0;

    for (i = 0; i < tour_route - 1; i++) {
        out_tour.route_length += distance_table[out_tour.tour_route[i]][out_tour.tour_route[i+1]];
    }
}

void update_tour_length(struct Tour in_tour, int[][] distance_table, int length) {
    in_tour.route_length = 0;
    for (int i = 0; i < length; i++) {
        in_tour.route_length += distance_table[out_tour.tour_route[i]][out_tour.tour_route[i+1]];
    }
}

// Does not do anything as of now
void check_if_valid(struct Tour in_tour) {
    exit(0);
}

struct Tour[] truncate_select(struct Tour[] set, float lose_percent) {
    int leng = sizeof(set) / sizeof(struct Tour);
    drop = (int) (leng - (leng * lose_percent));
    struct Tour[leng] outset;
    for (int j = 0; j < drop; j++) {
        outset[j] = set[j];
    }
    return outset
}

struct Tour[] order_crossover_set(struct Tour[] set, int meant_length, int[][] distance_table) {
    int set_length = sizeof(set) / sizeof(struct Tour);
    int needed = meant_length - set_length;

    for (int i = 0; i < needed; i++) {
        int order_cross_route[22];
        for (int x = 0; x < 22; x++) {order_cross_route[x] = -1;}
        order_cross_route[0] = 0;
        order_cross_route[21] = 0;

        int start = random_integer(1,10);
        int end = random_integer(11, 20);

        int r_tour_num = random_integer(0, set_length - 1);
        struct Tour random_tour_1 = set[r_tour_num];
        r_tour_num = random_integer(0, set_length - 1);
        struct Tour random_tour_2 = set[r_tour_num];

        for (x = start; x < end; x++) {
            order_cross_route[x] = random_tour_1.tour_route[x];
        }

        for (int j = end; j < end + 22; j++) {

            int counter = end;

            if order_cross_route[j%22] == -1 {

                while (true) {
                    insert = random_tour_2.tour_route[counter%22];

                    if (counter > 50) {
                        exit(-1);
                    }
                    if (is_in_list(insert, order_cross_route, 22)) {
                        counter++;
                        insert = random_tour_2.tour_route[counter%22];
                    }
                    else {
                        order_cross_route[j%22] = insert;
                        break;
                    }
                }
            }
        }

        int length_o_c_r = sizeof(order_cross_route) / sizeof(int);
        if (length_o_c_r < 22) {
            printf("Cross Array too small!");
            exit(-1);
        }
        if ((order_cross_route[0] != 0) || (order_cross_route[21] != 0)) {
            printf("Route does not finish valid");
            exit(-1);
        }
        struct Tour new_tour = tour_create_new(distance_table);
        new_tour.tour_route = order_cross_route;
        update_tour_length(new_tour, distance_table, 22);

        set[set_length + i] = new_tour;

    }
    return set;
}

struct Tour[] mutate_set(struct Tour[] set, int swap_amount, float mutate_percent) {
    int set_length = sizeof(set) / sizeof(struct Tour);
    int mutate_length = (int) (mutate_percent * set_length);

    for (int x = 0; x < mutate_length; x++) {

        int r_tour_i = random_integer(0, set_length - 1);
        struct Tour random_tour = set[r_tour_i];

        int swap_1 = random_integer(1, 20);
        int swap_2 = random_integer(1, 20);

        random_tour.tour_route[swap_1] = random_tour.tour_route[swap_2];
        random_tour.tour_route[swap_2] = random_tour.tour_route[swap_1];
    }
    return set;
}

struct Tour[] sort_route_list(struct Tour[] route_list) {
    
    int list_length = sizeof(route_list) / sizeof(struct Tour);

    for (int j = 0; j < list_length; j++) {
        for (int i = 0; i < list_length - 1; i++) {
            
            if (route_list[i].route_length > route_list[i+1].route_length) {
                struct Tour temp = route_list[i];
                route_list[i] = route_list[i+1];
                route_list[i+1] = temp;
            }

        }
    }
    return route_list;
}

#define ITERATIONS 200
#define ROUTE_SET 1024
#define TRUNCATE_AMOUNT 0.2
#define MUTATE_SWAP 1
#define MUTATE_PERCENTAGE 0.1

int main() {

    distance_table_new = format_distance_table(distance_table);
}