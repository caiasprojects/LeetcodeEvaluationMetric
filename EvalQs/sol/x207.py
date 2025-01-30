



class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses  # Initialize in-degree of each course

        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1  # Increment in-degree of the dependent course

        queue = [course for course in range(numCourses) if in_degree[course] == 0]  # Courses with no dependencies
        visited = [0] * numCourses  # Initialize visited array

        while queue:
            node = queue.pop(0)
            visited[node] = 1  # Mark the node as visited
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1  # Decrement in-degree of the neighbor
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)  # Add neighbor to the queue if in-degree is 0

        return all(visited[i] == 1 for i in range(numCourses))  # Check if all courses are visited