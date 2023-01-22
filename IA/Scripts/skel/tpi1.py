from pickletools import optimize
from tree_search import *
from cidades import *
from blocksworld import *


def func_branching(connections,coordinates):
    sum = 0
    for neighbor in coordinates:
        sum += len(func_actions(connections,neighbor))-1 
    return sum/len(coordinates) # average number of neighboor cities computed over all cities, sub 1 
    
class MyCities(Cidades):
    def __init__(self,connections,coordinates):
        super().__init__(connections,coordinates)
        # ADD CODE HERE IF NEEDED

class MySTRIPS(STRIPS):
    def __init__(self,optimize=False):
        super().__init__(optimize)

    def simulate_plan(self,state,plan):
        #IMPLEMENT HERE
        for action in plan:
            state = self.result(state,action)
        return state

    # def satisfies(self,state,goal_state):
    #     return state == goal_state

    # def heuristic(self,state,goal_state):
    #     return len(goal_state)-len(state)

 
class MyNode(SearchNode):
    def __init__(self,state,parent,cost=0,heuristic=0, depth=0):
        super().__init__(state,parent)
        self.cost = cost
        self.heuristic = heuristic
        self.depth = depth
        #ADD HERE ANY CODE YOU NEED

class MyTree(SearchTree):
    def __init__(self,problem, strategy='breadth',optimize=0,keep=0.25): 
        super().__init__(problem,strategy)
        self.optimize = optimize # initialize optimize variable
        #ADD HERE ANY CODE YOU NEED

    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        pass

    # remove a fraction of open (terminal) nodes
    # with lowest evaluation function
    # (used in Incrementally Bounded A*)
    def forget_worst_terminals(self):
        #IMPLEMENT HERE
        pass

    # procurar a solucao
    def search2(self):
        if self.optimize == 0:
            self.all_nodes[0] = MyNode(self.all_nodes[0].state, None,0)
        elif self.optimize == 1:
            self.all_nodes[0] = self.problem.initial, None,0,0,0

        while self.open_nodes != []:  
            nodeID = self.open_nodes.pop(0)
            node = self.all_nodes[nodeID]
            
            if self.optimize == 0:
                if self.problem.goal_test(node.state):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path(node) 
            elif self.optimize == 1:
                if self.problem.goal_test(node[0]):
                    self.solution = node
                    self.terminals = len(self.open_nodes)+1
                    return self.get_path2(node)

            lnewnodes = []
            self.non_terminals += 1
  
            for a in self.problem.domain.actions(node.state if not self.optimize else node[0]):
                newstate = self.problem.domain.result(node.state if not self.optimize else node[0],a)
                #print(node)
                condition = self.get_path(node) if self.optimize == 0 else self.get_path2(node)

                if newstate not in condition:
                    add_cost =  self.problem.domain.cost(node.state if not self.optimize else node[0],a)   
                    if self.optimize == 0:
                        newnode = MyNode(newstate,
                                        nodeID, 
                                        cost = node.cost + add_cost,
                                        heuristic = self.problem.domain.heuristic(newstate, self.problem.goal), 
                                        depth = node.depth + 1
                            )
                    elif self.optimize == 1:
                        newnode = (newstate,
                                        nodeID, 
                                        node[2] + add_cost,
                                        self.problem.domain.heuristic(newstate, self.problem.goal), 
                                        node[4] + 1
                            )
                        #print(newnode)
                    elif self.optimize == 2:
                        newnode = (newstate,
                                        nodeID, 
                                        node.cost + add_cost,
                                        self.problem.domain.heuristic(newstate, self.problem.goal), 
                                        node.depth + 1
                            )
                    lnewnodes.append(len(self.all_nodes))
                    self.all_nodes.append(newnode)
            self.add_to_open(lnewnodes)
        return None
        
# If needed, auxiliary functions can be added
    def get_path2(self,node):
        if not self.optimize:
            return self.get_path(node)
        elif self.optimize == 1:
            if node[1] == None:
                return [node[0]]
            path = self.get_path2(self.all_nodes[node[1]])
            path += [node[0]]
            return(path)    

    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy in [ 'A*', 'IBA*' ]:
            self.astar_add_to_open(lnewnodes)

