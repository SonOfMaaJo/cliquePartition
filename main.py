import copy
import csv

def powerset(N):
    """
    Returns the powerset of a set N.
    """
    if len(N) == 0:
        return [set()]
    else:
        P = powerset(N[1:])
        return P + [subset | {N[0]} for subset in P]

def k_partition_generattion(M, N, c):
    """
        display the partition generate by M.
        Attention : it is possible for the same partition to 
        appear when displayed.
    """
    Q =  ["s"] + list(N - M)
    P = {y: {y} for y in M}

    def element_compatible(vertex, M, c):
        return list(filter(lambda y: y in c[vertex] and vertex in c[y], M))
    
    #search
    def backTrackingSearch(vertex):
        if vertex == "s":
           Q.append(vertex)
           print([bloc for bloc in P.values()])
        else:
           for y in element_compatible(vertex, M, c):
               if all((x in c[vertex] and vertex in c[x]) for x in P[y]):
                  P[y].add(vertex)
                  backTrackingSearch(Q.pop())
                  P[y].remove(vertex)
           Q.append(vertex)
              
                
    backTrackingSearch(Q.pop())

def main():
    """
     generate the set of all compatibility partition of the example 1 and 2 
     of paper.
     
     A partition is a list of subsets of 
       N containing elements that are pairwise compatible.
    """
    N = {1, 2, 3, 4, 5}
    # Solution of example 1
    clique1_partitions = set()
    c1 = {}
    c1[1] = {1, 2, 3, 4}
    c1[2] = {1, 2, 4, 5}
    c1[3] = {2, 3, 4, 5}
    c1[4] = {1, 2, 4, 5}
    c1[5] = {1, 3, 5}
    M1_alpha = {2, 3}
    print("Solution of the example 1 :\n")
    for S in powerset(list(N - M1_alpha)):
        k_partition_generattion(M1_alpha | S, N, c1)
    

    # Solution of the example 2
    clique2_partitions = set()
    c2 = {}
    c2[1] = {1, 3, 4, 6}
    c2[2] = {2, 3, 5}
    c2[3] = {1, 2, 3, 5}
    c2[4] = {1, 4, 5}
    c2[5] = {2, 3, 4, 5, 6}
    c2[6] = {1, 5, 6}
    M2_alpha = {3, 4, 6}
    print("\n\nSolution of the example 2 :\n")
    for S in powerset(list(N - M2_alpha)):
        k_partition_generattion(M2_alpha | S, N, c2)
    
  
if __name__ == "__main__":
   main()