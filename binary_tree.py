class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class BinaryTree:
    root = None
    def to_list(self):
        list = []
        if self.root:
            self.visit_node(self.root, list)
        return list

    def visit_node(self, node, list):
        if node.prev:
            self.visit_node(node.prev, list)
        list.append(node.data)
        if node.next:
            self.visit_node(node.next, list)

    def find(self, name, node = None):
        if not node:
            node = self.root
        if name < node.data and node.prev:
            return self.find(name, node.prev)
        elif name > node.data and node.next:
            return self.find(name, node.next)
        else:
            return node

    def insert(self, name):
        if not self.root:
            self.root = Node(name)
        else:
            node = self.find(name)
            if name < node.data:
                node.prev = Node(name)
            else:
                node.next = Node(name)

people = BinaryTree()
people.insert("mark")
people.insert("charlie")
people.insert("alex")
people.insert("peter")
people.insert("bob")
people.insert("trek")
people.insert("donnie")
people.insert("barnie")
people.insert("butte")
people.insert("sam")

list = people.to_list()

print("the list of people in alphabetical order is {0}".format(list))
