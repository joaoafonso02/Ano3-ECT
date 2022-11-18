from pickletools import optimize
from tree_search import *
from cidades import *
from blocksworld import *


def func_branching(connections,coordinates):
    sum = 0
    numberOfCities = len(coordinates)
    for neighbor in coordinates:
        sum += len(func_actions(connections,neighbor))-1 
    return sum/numberOfCities # average number of neighboor cities computed over all cities, sub 1 
    
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
            state = self.result(state,action) # state is a tuple
        return state

 
class MyNode(SearchNode):
    def __init__(self,state,parent,cost=0,heuristic=0, depth=0):
        super().__init__(state,parent)
        self.cost = cost
        self.heuristic = heuristic
        self.depth = depth
        #ADD HERE ANY CODE YOU NEED

class MyTree(SearchTree):
    def __init__(self,problem, strategy='breadth',optimize=0,keep=0.25): 
        self.optimize = optimize # initialize optimize variable
        self.keep = keep

        if self.optimize == 2 or self.optimize == 4:
            self.operations = problem[0]
            self.initial = problem[1]
            self.goal = problem[2]

            self.open_nodes = [0]
            #print(self.initial, self.goal) #--> Braga, Faro,, exaclty as we want
            self.strategy = strategy
            self.solution = None
            self.all_nodes = [self.initial]
            self.non_terminals = 0
            self.terminals = 0
            self.cities = []
        else:
            super().__init__(problem,strategy)
            

        #ADD HERE ANY CODE YOU NEED

    def astar_add_to_open(self,lnewnodes):
        self.open_nodes.extend(lnewnodes)
        return self.open_nodes.sort(key=lambda elem : self.all_nodes[elem].cost + self.all_nodes[elem].heuristic)  


    # remove a fraction of open (terminal) nodes
    # with lowest evaluation function
    # (used in Incrementally Bounded A*)
    def forget_worst_terminals(self):
        depth = 0
        if (self.optimize == 0):
            for nodeID in self.open_nodes:
                depth += self.all_nodes[nodeID].depth
            depth = depth/len(self.open_nodes) # average depth of open nodes  
            maximum_nodes = pow ( self.problem.domain.branching_estimate, depth ) # Tree's max number of nodes
            KeepNo = math.trunk( self.keep * maximum_nodes ) + 1 # +1 to avoid 0  -->  keep this  
            self.open_nodes = self.open_nodes[:KeepNo]

        elif (self.optimize == 1):
            for nodeID in self.open_nodes:
                depth += self.all_nodes[nodeID][4]
            depth = depth/len(self.open_nodes)
            maximum_nodes = pow( self.problem.domain.branching_estimate, depth )
            KeepNo = math.trunc ( self.keep * maximum_nodes ) + 1 
            self.open_nodes = self.open_nodes[:KeepNo]

        elif (self.optimize == 4 or self.optimize == 2):
            for nodeID in self.open_nodes:
                depth = self.all_nodes[nodeID][4]
            depth = depth/len( self.open_nodes )
            maximum_nodes = pow( self.problem[0][5], depth )
            KeepNo = math.trunc ( self.keep * maximum_nodes) + 1
            self.open_nodes = self.open_nodes[:KeepNo]

    # procurar a solucao
    def search2(self):
        if self.optimize == 0:
            self.all_nodes[0] = MyNode(self.all_nodes[0].state, None,0)
        elif self.optimize == 1:
            self.all_nodes[0] = (self.problem.initial, None,0,0,0)
        elif self.optimize == 2: 
            self.all_nodes[0] = (self.initial, None,0,0,0) # (self.problem.initial, None,0,0,0)
        elif self.optimize == 4:
            self.all_nodes[0] = (self.initial, None,0,0,0)

        while self.open_nodes != []:  
            nodeID = self.open_nodes.pop(0)
            node = self.all_nodes[nodeID]
            
            if self.optimize == 0:
                if self.problem.goal_test(node.state):
                    self.solution = node
                    self.terminals = len(self.open_nodes) + 1
                    return self.get_path(node) 
            elif self.optimize == 1:
                if self.problem.goal_test(node[0]):
                    self.solution = node
                    self.terminals = len(self.open_nodes) + 1
                    return self.get_path2(node)
            elif self.optimize == 2:
                if self.operations[4](node[0], self.goal):
                    self.solution = node
                    self.terminals = len(self.open_nodes) + 1
                    return self.get_path2(node)
            elif self.optimize == 4:
                if self.operations[4](node[0], self.goal):
                    self.solution = node
                    self.terminals = len(self.open_nodes) + 1
                    return self.get_path2(node)

            lnewnodes = []
            self.non_terminals += 1
  
            if self.optimize == 0 :
                for a in self.problem.domain.actions(node.state if not self.optimize else node[0]):
                    newstate = self.problem.domain.result(node.state if not self.optimize else node[0],a)
                    #print(node)
                    condition = self.get_path(node) if self.optimize == 0 else self.get_path2(node)

                    if newstate not in condition:
                        add_cost =  self.problem.domain.cost(node.state if not self.optimize else node[0],a)   
                        newnode = MyNode(newstate,
                                            nodeID, 
                                            cost = node.cost + add_cost,
                                            heuristic = self.problem.domain.heuristic(newstate, self.problem.goal), 
                                            depth = node.depth + 1
                                )
                        
                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)
            ##############################################
            elif self.optimize == 1:
                #print(self.operations[0](node[0]))
                for a in self.problem.domain.actions(node.state if not self.optimize else node[0]):
                    newstate = self.problem.domain.result(node.state if not self.optimize else node[0],a)
                    #print(node)
    
                    if newstate not in self.get_path2(node):
                        add_cost =  self.problem.domain.cost(node[0],a)   
                        newnode = (newstate,
                                            nodeID, 
                                            node[2] + add_cost,
                                            self.problem.domain.heuristic(newstate, self.problem.goal), 
                                            node[4] + 1
                                )
                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)    
            ##############################################
            elif self.optimize == 2:
                #print(self.operations[0](node[0]))
                for a in self.operations[0](node[0]):
                    newstate = self.operations[1](node[0],a)
                    #print(node)
                    condition = self.get_path(node) if self.optimize == 0 else self.get_path2(node)
                    if newstate not in condition:
                        newnode = (newstate,
                                        nodeID, 
                                        node[2] + self.operations[2](node[0], a),
                                        self.operations[3](newstate, self.goal), 
                                        node[4] + 1
                                )
                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)    
             ##############################################
            elif self.optimize == 4:
                #print(self.operations[0](node[0]))
                for a in self.operations[0](node[0]):
                    newstate = self.operations[1](node[0],a)
                    #print(node)
                    condition = self.get_path(node) if self.optimize == 0 else self.get_path2(node)
                    
                    if newstate not in condition:
                        newnode = (newstate,
                                        nodeID, 
                                        node[2] + self.operations[2](node[0], a),
                                        self.operations[3](newstate, self.goal), 
                                        node[4] + 1
                                )
                        #self.cities[newstate] = self.cities[node[0]]

                        lnewnodes.append(len(self.all_nodes))
                        self.all_nodes.append(newnode)
                self.add_to_open(lnewnodes)   

        print("No solution found")       
        return None
        
# If needed, auxiliary functions can be added
    def get_path2(self,node):
        if not self.optimize:
            return self.get_path(node)
        else:
            if node[1] == None:
                return [node[0]]
            path = self.get_path2(self.all_nodes[node[1]])
            path += [node[0]]
            return(path)    

    def add_to_open2(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy in [ 'A*', 'IBA*' ]:
            self.astar_add_to_open(lnewnodes)

