from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create the set of available supplies
        supply = set(supplies)
        # Initialize in-degree and adjacency list
        degree = {recipe: 0 for recipe in recipes}
        adj = defaultdict(list)
        
        # Build the graph
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in supply:
                    adj[ingredient].append(recipe)
                    degree[recipe] += 1
        
        # Initialize the queue with recipes that have 0 in-degree
        que = deque([recipe for recipe in recipes if degree[recipe] == 0])
        ans = []
        
        # Perform topological sorting
        while que:
            recipe = que.popleft()
            ans.append(recipe)
            for neighbor in adj[recipe]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    que.append(neighbor)
        
        return ans
