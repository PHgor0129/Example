def cut_value(S, G):
    V = set(G.keys())
    S_complement = V - S
    return sum(1 for u in S for v in G[u] if v in S_complement)

def greedy_max_cut(G):
    S = set() 
    V = set(G.keys())
    
    while True:
        current_val = cut_value(S, G)
        improved = False
        
        for v in list(S):
            S.remove(v)
            if cut_value(S, G) > current_val:
                current_val = cut_value(S, G)
                improved = True
                break
            S.add(v)
        
        if not improved:
            for v in list(V - S):
                S.add(v)
                if cut_value(S, G) > current_val:
                    current_val = cut_value(S, G)
                    improved = True
                    break
                S.remove(v)
        
        if not improved:
            return S

def test_greedy_max_cut():
    G1 = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    
    S1 = greedy_max_cut(G1)
    print("Cut set S:", S1)
    print("Cut value:", cut_value(S1, G1))

    G2 = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3, 4],
        3: [ 1, 2, 4],
        4: [2, 3]
    }
    
    S2 = greedy_max_cut(G2)
    print("Cut set S:", S2)
    print("Cut value:", cut_value(S2, G2))
    
test_greedy_max_cut()
