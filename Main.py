from Bipartite_Matching_Assignment import *

def TestMaximumBipartiteMatching():
    V1, V2, E = [], [], []
    
    m = int(input())
    for i in range(m):
        v1, v2 = input().split()
        V1.append(v1)
        V2.append(v2)
        E.append((v1, v2))

    B = BipartiteGraph(V1, V2, E)
    print(MaximumCardinalityMatching(B, []))

def TestAssignmentProblem():
    V1, V2, E, W = [], [], [], []

    m = int(input())
    for i in range(m):
        v1, v2, w = input().split()
        V1.append(v1)
        V2.append(v2)
        E.append((v1, v2))
        W.append(float(w))

    B = BipartiteGraph(V1, V2, E, W)
    print(AssignmentProblem(B))

if __name__ == '__main__':
    #TestMaximumBipartiteMatching()
    TestAssignmentProblem()

