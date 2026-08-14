import re
from collections import defaultdict

def solve_puzzle(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return "File not found"

    fragments = re.findall(r'\d+', content)
    if not fragments:
        return "No data"

    adj = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for frag in fragments:
        u = frag[:2]
        v = frag[-2:]
        adj[u].append(frag)
        out_degree[u] += 1
        in_degree[v] += 1

    start_node = None
    for node in set(list(out_degree.keys()) + list(in_degree.keys())):
        if out_degree[node] - in_degree[node] == 1:
            start_node = node
            break
            
    if start_node is None:
        start_node = next(iter(adj.keys()))

    stack = [(start_node, None)]
    result_edges = []

    while stack:
        curr, edge_in = stack[-1]
        if adj[curr]:
            nxt_edge = adj[curr].pop()
            nxt_node = nxt_edge[-2:]
            stack.append((nxt_node, nxt_edge))
        else:
            _, edge = stack.pop()
            if edge is not None:
                result_edges.append(edge)

    result_edges.reverse()

    final_sequence = result_edges[0]
    for frag in result_edges[1:]:
        final_sequence += frag[2:]

    return final_sequence

if __name__ == "__main__":
    result = solve_puzzle("fragments.txt")
    print(f"Довжина результату: {len(result)}")
    
    with open("result.txt", "w", encoding='utf-8') as f:
        f.write(result)