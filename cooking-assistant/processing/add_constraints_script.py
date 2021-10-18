constraints = [
    "wok",
    "grill pan",
    "sauce pan",
    "saucier",
    "double boiler",
    "saute pan",
    "multi pot",
    "braiser",
    "frenc oven",
    "deep skillet",
    "roaster pan",
    "stock pot",
    "soup pot"
]

with open("recipeapp:constraint.txt", "a") as f:
    for constraint in constraints:
        f.write(f"with {constraint}\n")
        f.write(f"no {constraint}\n")