student_graph = {}

num_edges = int(input("Enter number of edges: "))

for _ in range(num_edges):
    edge_input = input("Enter node and connected nodes (example: 1:2,3): ")
    node, connected_nodes = edge_input.split(":")
    student_graph[int(node.strip())] = [int(n.strip()) for n in connected_nodes.split(",") if n.strip()]

start_node = int(input("Enter start node: "))
x = int(input("Enter element to search: "))

visited = []
queue = [start_node]
found = False

while queue:
    node = queue.pop(0) 
    
    if node == x:
        print(f"Element '{x}' found!")
        found = True
        break
    
    if node not in visited:
        visited.append(node)
        for neighbor in student_graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

if not found:
    print(f"Element '{x}' not found in the graph.")

print("BFS Traversal Order:", visited)