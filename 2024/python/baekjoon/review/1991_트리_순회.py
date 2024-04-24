n = int(input())
graph = {}
for _ in range(n):
    a, b, c = input().split()
    graph[a] = [b, c]

def preorder(root):
    if not root or root == '.':
        return
    print(root, end = '')
    preorder(graph[root][0])
    preorder(graph[root][1])

def inorder(root):
    if not root or root == '.':
        return
    inorder(graph[root][0])
    print(root, end = '')
    inorder(graph[root][1])

def postorder(root):
    if not root or root == '.':
        return False
    postorder(graph[root][0])
    postorder(graph[root][1])
    print(root, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')
