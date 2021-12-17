# -*- coding: utf-8 -*-
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
            
    def delete(self, data):
        if self.head == '':
            print("해당 값이 없습니다.")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else :
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
                    
    def find(self, data):
        node = self.head
        while node:
            if(node.data == data):
                return node
            else:
                node = node.next
        print("해당 값이 없습니다.")
            
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        
linkedList = NodeMgmt(0)

for i in range (1,10):
    linkedList.add(i)
    
linkedList.find(5)
# -

