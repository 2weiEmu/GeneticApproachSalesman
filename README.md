# A Genetic Approach to the Traveling Salesman Problem

Basically we had this as a case study in IB Computer Science, and I thought that maybe I could implement it. The exam is already over, but I wanted to do it anyway.

Basically if you want the best in accuracy i.e. the shortest route that I can give you there are 2 approaches:
You enable the full sorting (though you could also do that with optimised bubble sort) and then run a 1024 set run at 200 iterations with 0.4 truncate amount and 1 mutate swap and 0.1 mutation.
Or you can get something mostly right, close to right, by running the new pseudo-random number thing random() * 21, the new truncate select, and just commenting out sorting, with like a truncate of 0.2 (though 0.4 may also work) and you can prob get more iterations in there.
The second method is SUBSTANTIALLY faster.