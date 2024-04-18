# splay tree
# from monopoly_main import *

class Node:
    def __init__(self, key, value, bpos):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.boardpos = int(bpos)

class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
            else:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    def insert(self, key, value, boardpos):
        node = Node(key, value, boardpos)
        y = None
        x = self.root
        while x:
            y = x
            if node.boardpos < x.boardpos:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.boardpos < y.boardpos:
            y.left = node
        else:
            y.right = node
        self.splay(node)

    def search(self, bpos):
        x = self.root
        y = int(x.boardpos)
        while x:
        
            if int(bpos) < int(x.boardpos):
                x = x.left
            elif bpos > int(x.boardpos):
                x = x.right
            else:
                self.splay(x)
                
                return x
        return None
    
    def update_value(self, key, new_value):
        node = self.search(key)
        if node:
            node.value = new_value
            return True
        return False
    
    def get_most_searched(self):
        most_searched = []
        if self.root and self.root.value not in ["cc", "no", "ch", None]:
            most_searched.append(self.root.boardpos)
            if self.root.left and self.root.left.value not in ["cc", "no", "ch", None]:
                most_searched.append(self.root.left.boardpos)
            if self.root.right and self.root.right.value not in ["cc", "no", "ch", None]:
                most_searched.append(self.root.right.boardpos)
        return most_searched
    
    def increase_visited(self):
        nodelst = tree.get_most_searched()
        for node in nodelst:
            x = self.search(node)
            x.value = int(x.value)*1.5
            print(x.key,":", x.value)

    def decrease_visited(self):
        nodelst = tree.get_least_searched()
        for node in nodelst:
            x = self.search(node)
            x.value = int(x.value)*0.85
            print(x.key,":", x.value)
            

    def in_order_traversal(self, node, leaf_nodes):
        if node:
            self.in_order_traversal(node.left, leaf_nodes)
            if node.left is None and node.right is None:
                leaf_nodes.append(node)
            self.in_order_traversal(node.right, leaf_nodes)

    def get_least_searched(self):
        leaf_nodes = []
        self.in_order_traversal(self.root, leaf_nodes)
        return [node.boardpos for node in leaf_nodes if node.value not in ["cc", "no", "ch", None]]
    
    
            

# Usage
monopoly_properties = [["GO","no"],["Shoreline Pass",60],["Community Chest","cc"],["Trailhawk Lane",60],["Income Tax","no"],["Queens Crown Station",200],["Creighton Plaza",100],["CHANCE","ch"],["Tuscan Road",100],["Dreamville Lane",120],["Just Visiting","no"],["Grand View Mall",140],["Electric Company",150],["Pismo Court",140],["Swanson Avenue",160],["Kanto Station",200],["Morales Street",180],["COMMUNITY CHEST","cc"],["Palace Vinyard",180],["Cynthia Street",200],["Free Parking","no"],["Strand",220],["CHANCE","ch"],["Trojan Road",220],["Tralfamadore Square",240],["Spain Street Station",200],["John London Square",260],["Curry Street",260],["Water Works",150],["Tilted Towers",280],["Go To Jail","no"],["Berkeley Lane",300],["Lombard Street",300],["Community Chest","cc"],["Telegraph Avenue Station",200],["CHANCE","ch"],["Rocky Reels",350],["Super Tax","no"],["Palm Springs",400]]

tree = SplayTree()
for x in range(len( monopoly_properties)):
    print(monopoly_properties[x][0])
    if monopoly_properties[x][0] != None:
        tree.insert(monopoly_properties[x][0], monopoly_properties[x][1], x)
    
    
# print(tree.decrease_visited())
# print(tree.search("Shoreline Pass").key) 
# z = tree.search("Creighton Plaza")
# tree.search("Kanto Station").key  # Kanto Station
# tree.search("CHANCE").key  # CHANCE
# print(tree.search("Creighton Plaza").key)  # Community Chest
# print(tree.increase_visited("Swanson Avenue"))  # Output: None
# print(tree.search("Swanson Avenue").value)  # Output: 90
# print(tree.get_least_searched())  # Output: ['Creighton Plaza', 'Dreamville Lane', 'Income Tax', 'Kanto Station', 'Morales Street', 'Queens Crown Station', 'Strand', 'Swanson Avenue', 'Trailhawk Lane', 'Trojan Road']

#! except chance and community chest, all other properties will splay to the root after being searched