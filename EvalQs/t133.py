
from sol.x133 import Solution

class UndirectedGraphNode:
    def __init__(self, x):
        self.val = x
        self.neighbors = []

def are_graphs_identical(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    
    stack = [(node1, node2)]
    visited = set()
    
    while stack:
        n1, n2 = stack.pop()
        
        if (n1, n2) in visited:
            continue
        visited.add((n1, n2))
        
        if n1.val != n2.val:
            return False
        
        if len(n1.neighbors) != len(n2.neighbors):
            return False
        
        for nbr1, nbr2 in zip(n1.neighbors, n2.neighbors):
            stack.append((nbr1, nbr2))
    
    return True


# Example usage and test case
solution = Solution()

node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(3)
node4 = UndirectedGraphNode(4)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3, node4]
node3.neighbors = [node1, node2]
node4.neighbors = [node2]



# Additional asserts
node5 = UndirectedGraphNode(5)
node6 = UndirectedGraphNode(6)
node1.neighbors.append(node5)
node5.neighbors.append(node6)
node6.neighbors.append(node5)
cloned_node = solution.cloneGraph(node1)
assert are_graphs_identical(node1, cloned_node)

node7 = UndirectedGraphNode(7)
node8 = UndirectedGraphNode(8)
node8.neighbors.append(node7)
node7.neighbors.append(node8)
node1.neighbors.append(node8)
cloned_node = solution.cloneGraph(node1)
assert are_graphs_identical(node1, cloned_node)
