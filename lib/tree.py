class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Depth-first traversal
        def dfs(node):
            if node is None:
                return None
            if node.get('id') == id:
                return node
            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result
            return None

        # Breadth-first traversal
        def bfs(node):
            queue = [node]
            while queue:
                current_node = queue.pop(0)
                if current_node.get('id') == id:
                    return current_node
                queue.extend(current_node.get('children', []))
            return None

        # Call the appropriate traversal method based on the requirement
        # Here, we use breadth-first traversal by default
        return bfs(self.root)
