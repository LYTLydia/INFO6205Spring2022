#Q1-1
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return copy.deepcopy(node)

#Q1-2
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None;

        first_node = Node(node.val);
        new_nodes = {node.val: first_node};
        stack = [node];

        while stack:
            cur_node = stack[-1];
            for neighbor in cur_node.neighbors:
                if neighbor.val not in new_nodes.keys():
                    new_nodes[neighbor.val] = Node(neighbor.val);
                    stack.append(neighbor);
                    break;
                elif new_nodes[neighbor.val] not in new_nodes[cur_node.val].neighbors:
                    new_nodes[cur_node.val].neighbors.append(new_nodes[neighbor.val]);
            else:
                stack.pop();

        return first_node;


#Q2
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = collections.deque([])
        visited = set()
        n = len(graph)
        for i in range(n):
            q.append((i, 1 << i))
            visited.add((i, 1 << i))
        dis = 0
        while q:
            dis += 1
            for _ in range(len(q)):
                cur, cur_state = q.popleft()
                for nxt in graph[cur]:
                    nxt_state = cur_state | (1 << nxt)
                    if nxt_state == (1 << n) - 1: return dis
                    if (nxt, nxt_state) not in visited:
                        q.append((nxt, nxt_state))
                        visited.add((nxt, nxt_state))
        return 0


#Q3
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def dfs(u, node_set, value,  cost):
            nonlocal ans
            if cost > maxTime: return
            if u == 0:
                ans = max(ans, value)
            for v, c in g[u]:
                if v in node_set:
                    dfs(v, node_set, value, cost + c)
                else:
                    node_set.add(v)
                    dfs(v, node_set, value + values[v], cost + c)
                    node_set.remove(v)

        g = defaultdict(list)
        for u, v, c in edges:
            g[u].append((v, c))
            g[v].append((u, c))
        ans = 0
        dfs(0, {0}, values[0], 0)
        return ans