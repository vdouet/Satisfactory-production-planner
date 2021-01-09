# Satisfactory production planner
import json
from pprint import pprint

products = []
buildings = []

class Tree:
    def __init__(self, buildings):
        self.children = []
        self.buildings = buildings

    def create_graph(self, depth = 0):
        layer = "layer {} ".format(depth) + "|"+ "_" * depth + "{}".format(self.buildings) + "\n"
        for child in self.children:
            layer += child.create_graph(depth+1)
        return layer

def production_tree(data, name, value, tree):

    """
    We use recursivity here because our item production is basically a tree with 
    the item we want being the root and the other items to make it being lower nodes 
    (the children) all the way to the raw ingredients (leaf nodes).
    Because we can use different buildings with a merger using one input it creates a child
    node with multiple parent nodes which is, in reality, not a tree (it's a graph). 
    But we can still use basic tree algorithm here.

    Args:
        data (dict): Dictionnary containing the JSON of the recipes.
        name (str): String of the item we want to produce
        value (int): Number of item we want to produce
    """

    # We look for the corresponding item
    for products in data['item']['normal']:
        if products['name'] == name:

            # We check if the ingredients list is not empty
            if products['ingredients']:

                # We calculate the building operation rate in pourcent
                # using the normal output of the building and the output needed.
                pourcent = (value / products['production']) * 100
                print(pourcent)

                # We add the building to the buildings list for the current node.
                buildings_node = [products['building']]

                # If a building needs to function at more than 100% we add more buildings
                # of the same type to get to an operation rate of 100% or less.
                # (We don't want to overclock a building as shards are more useful if used on miners.)
                if (pourcent > 100):
                    while pourcent > 100:
                        buildings_node.append(products['building'])
                        pourcent -= 100

                # We add the required building(s) to our global buildings list.
                buildings.append(buildings_node)

                node = Tree(buildings_node)
                tree.children.append(node)

                # We do the same recursively for each ingredients and ingredient value needed
                # in our current item's ingredients list.
                for key in products['ingredients']:
                    production_tree(data, key, products['ingredients'][key], node)

            # If the ingredients list is empty we have reached a leaf node.
            else:
                break

print("Welcome to Satisfactory production planner!\n")
print("Loading json...")

with open("recipes.json") as f:
    data = json.load(f)

name = "Reinforced iron plate"
value = 5
root = Tree("root")
production_tree(data, name, value, root)
print(buildings)
print(root.create_graph())
