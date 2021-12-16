# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
            
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        
linkedList = NodeMgmt(0)

for i in range (1,10):
    linkedList.add(i)
    
linkedList.desc()
# -


