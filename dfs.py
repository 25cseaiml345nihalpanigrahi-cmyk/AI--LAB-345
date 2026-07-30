student_graph = {}

num_edges = int(input("Enter number of edges: "))

for _ in range(num_edges):
    edge_input = input("Enter node and connected nodes (example: 1:2,3): ")
    node, connected_nodes = edge_input.split(":")
    student_graph[int(node.strip())] = [int(n.strip()) for n in connected_nodes.split(",") if n.strip()]

start_node = int(input("Enter start node: "))
x = int(input("Enter element to search: "))

visited = []
stack=[start_node]
found=False
while stack:
    current_node = stack.pop()
    if current_node not in visited:
        visited.append(current_node)
        if current_node == x:
            found=True
            print(f"Element {x} found in the graph.")
            break
        stack.extend(student_graph.get(current_node, []))
