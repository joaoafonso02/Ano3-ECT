from constraintsearch import *

region = ['A', 'B', 'C', 'D', 'E']
colors = ['red', 'blue', 'green', 'yellow', 'white']

domains = { # var: domain,...
            var: colors for var in region
        }
    
different_colors = lambda v1, x1, v2, x2: x1 != x2

edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
edges += [ (var, 'E') for var in region if var != 'E']
edges += [(var1, var2) for (var1, var2) in edges]

cg = { # aresta:restrição, ...
        e:different_colors for e in edges
    }

cs = ConstraintSearch(domains, cg)

print(cs.search())
N

# extra, determine automatically min numb of colors
min_colors = colors[:2]
while True:
    domains = {var:min_colors for var in region}
    cs = ConstraintSearch(domains, cg)
    solution = cs.search()
    if solution != None:
        break
    min_colors.append(colors[len(min_colors)])

    # -- completar


print (len(min_colors))