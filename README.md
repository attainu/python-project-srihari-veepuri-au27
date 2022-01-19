                                       MAZE SOLVER
AIM:

The aim of this project is to build a python program  that runs as a command line tool. It
should take the input and output file names as commaand-line arguements.
Using the square matrix present in the input file it should generate a path to reach the 
maze and put it in the output file.If there is no path it returns -1.
Where 0 means blocked path and 1 means the path we can go through.

                       source 1 1 1 0 0
                              0 0 1 0 0
                              0 0 1 1 0 
                              0 0 0 1 1 
                              0 0 0 0 1 destination

CONCEPTS USED:

* Graphs.
* BFS(Bredth First Search).
* Dijkstra Algorithm.
* File Handling.

FOLDER CONTAINS:(MAZESOLVER)

* main.py - It contains main block of code.
* Inputfile.txt - To give matrix in the form of binary matrix which contains only 1's and 0's.
* Outputfile.txt - To view the output after running the code.
* __init__.py - To make modules into package. 
 

PROGRAM PROCEDURE:
It takes the input matrix from the input file and convert that matrix into a graph.Graph contains
vertices or nodes and branches or edges.After that we check all the vertices in a graph are connected
or not by using BFS(Breadth first search).Then we find the shortest path between the source node
to destination node by using Dijkstra algorithm.

INPUT FORMAT:the input file looks like this.

1 1 1 1 1 
1 1 0 0 0
0 1 1 0 0 
0 1 1 1 0 
0 0 0 1 1

After run the command(python main.py inputfile.txt outputfile.txt --s=0,0 --d=4,4,) the output file 
looks like as below.

OUTPUT FORMAT:

1 1 0 0 0 
0 1 0 0 0
0 1 1 0 0
0 0 1 1 0
0 0 0 1 1



(THANK YOU)






