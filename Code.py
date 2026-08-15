import re
import sys
from collections import defaultdict

sys.setrecursionlimit(3000)

def solve_puzzle(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return "File not found"

    fragments = re.findall(r'\d+', content)
    if not fragments:
        return "No data"

    max_chain = []
    
    def dfs(current_chain, current_adj):
        nonlocal max_chain
        
        if len(current_chain) > len(max_chain):
            max_chain = list(current_chain)
            
        tail = current_chain[-1][-2:]
        
        for i in range(len(current_adj[tail])):
            next_frag = current_adj[tail].pop(i)
            current_chain.append(next_frag)
            
            dfs(current_chain, current_adj)
            
            current_chain.pop()
            current_adj[tail].insert(i, next_frag)

    for start_frag in fragments:
        current_adj = defaultdict(list)
        for frag in fragments:
            current_adj[frag[:2]].append(frag)
            
        current_adj[start_frag[:2]].remove(start_frag)
        
        dfs([start_frag], current_adj)

    if not max_chain:
        return ""

    final_sequence = max_chain[0]
    for frag in max_chain[1:]:
        final_sequence += frag[2:]

    return final_sequence

if __name__ == "__main__":
    result = solve_puzzle("fragments.txt")
    print(f"Довжина результату: {len(result)}")
    
    with open("result.txt", "w", encoding='utf-8') as f:
        f.write(result)