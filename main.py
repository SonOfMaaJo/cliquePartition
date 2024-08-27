import copy
from powerset import powerset
import csv

def k_partition_generattion(M, N, c):
    Q = ["s"]
    Q = Q + list(N - M)
    P = {y: {y} for y in M}
    k_partitions = []

    def element_compatible(vertex, M, c):
        return list(filter(lambda y: y in c[vertex] and vertex in c[y], M))
    # fonction de recherche basée sur le backtraccking
    def backTrackingSearch(vertex):
        if vertex == "s":
           Q.append(vertex)
           k_partitions.append(copy.deepcopy(P))
        else:
           for y in element_compatible(vertex, M, c):
               if all((x in c[vertex] and vertex in c[x]) for x in P[y]):
                  P[y].add(vertex)
                  backTrackingSearch(Q.pop())
                  P[y].remove(vertex)
           Q.append(vertex)
              
                
    backTrackingSearch(Q.pop())
    return k_partitions

def main():
    N = {1, 2, 3, 4, 5}
    # resolution de la situation 1
    clique1_partitions = []
    c1 = {}
    c1[1] = {1, 2, 3, 4}
    c1[2] = {1, 2, 4, 5}
    c1[3] = {2, 3, 4, 5}
    c1[4] = {1, 2, 4, 5}
    c1[5] = {1, 3, 5}
    M1_alpha = {2, 3}
    for S in powerset(list(N - M1_alpha)):
        clique1_partitions.append(k_partition_generattion(M1_alpha | S, N, c1))
    with(open("clique1_partitions.csv", "w", newline="")) as f:
        writer = csv.writer(f)
        for k_partitions in clique1_partitions:
            writer.writerow([x for x in k_partitions[0].keys()])
            writer.writerows([k_partition.values() for k_partition in k_partitions])

    # resolution de la situation 2
    clique2_partitions = []
    c2 = {}
    c2[1] = {1, 3, 4, 6}
    c2[2] = {2, 3, 5}
    c2[3] = {1, 2, 3, 5}
    c2[4] = {1, 4, 5}
    c2[5] = {2, 3, 4, 5, 6}
    c2[6] = {1, 5, 6}
    M2_alpha = {3, 4, 6}
    for S in powerset(list(N - M2_alpha)):
        clique2_partitions.append(k_partition_generattion(M2_alpha | S, N, c2))
    with(open("clique2_partitions.csv", "w", newline="")) as f:
        writer = csv.writer(f)
        for k_partitions in clique2_partitions:
            writer.writerow([x for x in k_partitions[0].keys()])
            writer.writerows([k_partition.values() for k_partition in k_partitions])
  
if __name__ == "__main__":
   main()