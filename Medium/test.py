import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
t = q.get()
print(t)
print(q.qsize())

if root.right:
    self.adj[root.val].add(root.right.val)
    self.adj[root.right.val].add(root.val)
    travesal(root.right)
