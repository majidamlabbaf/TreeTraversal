class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert Node
    def insert(self, data):
        if not self:
            root = Node(data)
            return
        q = []
        q.append(self)

        while (len(q)):
            self = q[0]
            q.pop(0)

            if (not self.left):
                self.left = Node(data)
                break
            else:
                q.append(self.left)

            if (not self.right):
                self.right = Node(data)
                break
            else:
                q.append(self.right)

# Tree navigation
    def in_order(self, root):
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.data)
            res = res + self.in_order(root.right)
        return res

    def Pre_order(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.Pre_order(root.left)
            res = res + self.Pre_order(root.right)
        return res

    def Post_order(self, root):
        res = []
        if root:
            res = self.Post_order(root.left)
            res = res + self.Post_order(root.right)
            res.append(root.data)
        return res


root = Node(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(50)
root.insert(60)
root.insert(70)

print("==================================")

print("in_order:")
print(root.in_order(root))
print("pre_order:")
print(root.Pre_order(root))
print("post_order:")
print(root.Post_order(root))

print("==================================")
