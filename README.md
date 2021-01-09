# Satisfactory-production-planner

WIP: A production planner made for the Satisfactory game.

Just a little project I'm working on while progressing through the game. The recipes are stored in a JSON file and are easy to add or delete using the following syntax:   

```json
{
  "name": "Reinforced iron plate",
  "ingredients": {"Iron plate": 6, "Screw": 60},
  "building": "Assembler",
  "production": 5
}
```

Two recipes types exist, `item` for recipes related to various in-game items. And `building` for recipes related to buildings (only used for resources cost calculation).  
There are also two different types of `item` recipes, `normal` for the normal items recipes and `alternate` for the alternate recipes.

Once a recipe is given, the script travels through the JSON file to find the given recipe and recursively calculates the components needed by searching for each individual component, the components' components, and so on, in a graph-like manner. Needed buildings are added to a tree as new nodes with the starter recipe as the root and the raw components as the leaves. The graph with the required buildings and links between them is generated using the Python module "Anytree" using the `main-Anytree` script or just as a console output using `main.py`. 

The script also calculates each building's operation rate. 100% for the normal operation rate or lower if the building needs to be downclock. If the operation rate is >100%, a new building of the same type is added.

To-do:
+ Add a GUI with PySide2.
+ Add all the recipes in `recipes.json`.
+ Replace Anytree by a better way to visualize graphs.
+ Add handling of the alternate recipes.
+ Calculate raw material cost and power for all the needed buildings.
+ Show each building's operation rate [0% - 100%].
+ Add a "power" field for each building in `recipes.json`.
