from collections import deque

def bfs_debug(graph, start):
    queue = deque([start])
    visited = {start}
    order = []
    
    step = 1
    print(f"=== BFS 搜尋開始，起點為 '{start}' ===\n")
    
    while queue:
        print(f"--- Step {step} ---")
        print(f"當前佇列 (Queue)     : {list(queue)}")
        
        # 取出佇列第一個元素
        node = queue.popleft()
        order.append(node)
        print(f"👉 取出處理節點 (Node) : '{node}'")
        
        # 尋找鄰居
        neighbors = graph.get(node, [])
        new_added = []
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                new_added.append(neighbor)
                
        print(f"   檢查鄰居          : {neighbors}")
        print(f"   新加入佇列的鄰居  : {new_added if new_added else '無'}")
        print(f"目前走訪結果 (Order)  : {order}")
        print(f"目前已標記 (Visited) : {visited}")
        print("-" * 35 + "\n")
        
        step += 1
        
    return order


# ==================== 測試參數與執行 ====================
if __name__ == "__main__":
    # 測試圖形結構 (鄰接表 Adjacency List)
    #      A
    #     / \
    #    B   C
    #   / \   \
    #  D   E   F
    test_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    test_start = 'A'
    
    final_order = bfs_debug(test_graph, test_start)
    print("🎉 最終結果：", " -> ".join(final_order))