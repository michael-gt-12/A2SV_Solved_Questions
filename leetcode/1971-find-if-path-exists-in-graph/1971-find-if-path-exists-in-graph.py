class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build the graph
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Stores the visited nodes
        visited = set()

        # DFS algorithm
        def dfs(node,visited):
            # Base Case
            if node == destination:
                return True

            visited.add(node)

            # Visit the neighbor nodes also
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor,visited):
                        return True

            return False

        return dfs(source, visited)

        