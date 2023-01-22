#encoding: utf8

# YOUR NAME: João Afonso Pereira Ferreira
# YOUR NUMBER: 103037 

# COLLEAGUES WITH WHOM YOU DISCUSSED THIS ASSIGNMENT:
# - ...
# - ...

from semantic_network import *
from bayes_net import *
from constraintsearch import *



class MySN(SemanticNetwork):

    def __init__(self):
        SemanticNetwork.__init__(self)
        # ADD CODE HERE IF NEEDED
        self.declarations = []
        pass

    def is_object(self,user,obj):
        for u in self.declarations:
            if u.user == user and type(u.relation)==Member and u.relation.entity1 == obj:
                return True
            if u.user == user and type(u.relation)==Association and (u.relation.entity1 == obj or u.relation.entity2 == obj):
                return True
        return False
        
 
    def is_type(self,user,type):
        #return self.query_local(user, e2 = type) != []
        for u in self.declarations:
            if u.user == user and (u.relation.entity2 == type and isinstance(u.relation, Member)) or (isinstance(u.relation, Association) and u.relation.entity2 == type):
                return True
        return False


    def infer_type(self,user,obj,xpto=None):
        for u in self.declarations: 
            if u.user == user: 
                if isinstance(u.relation, Member) and u.relation.entity1 == obj:
                    return u.relation.entity2 # type

                elif isinstance(u.relation, Subtype) and (u.relation.entity1 == obj or u.relation.entity2 == obj):
                    return u.relation.entity1 # subtype
                
                elif isinstance(u.relation, Association) and (u.relation.card == "one" or u.relation.card == "many") and (u.relation.entity1 == obj or u.relation.entity2 == obj) : 
                    return u.relation.entity2  # type

            elif isinstance(obj, str) and (u.relation.entity1 == obj or u.relation.entity2 == obj) :
                return '__unknown__'

            elif isinstance(obj, int) or isinstance(obj, float): # checks if obj is a number
                return 'number'
        return None # no type

 
    def infer_signature(self,user,assoc,xpto=None):
        for u in self.declarations:
            if u.user == user and isinstance(u.relation,Association) and u.relation.name == assoc: # if  association exists
                s1 = self.infer_type(user, u.relation.entity1) # type of entity1
                s2 = self.infer_type(user, u.relation.entity2) # type of entity2
                return (s1,s2) # return signature
        return None # no assoc


class MyBN(BayesNet):

    def __init__(self):
        BayesNet.__init__(self)
        # ADD CODE HERE IF NEEDED
        pass

    def markov_blanket(self,var):
        # print(self.dependencies) # DEBUG tuples
        # print("-------------------------------------------")
        # print(self.dependencies[var]) # DEBUG tuples

        m_blanket = []
        copy_m_blanket = []

        # add children
        for c, d in self.dependencies.items():
            i = 0
            while i < len(d):
                p1, p2, pr = d[i] # p1 = parents & p2 = parents
                if p1 != [] and p2 != []:
                    if p1[0] == var or p2[0] == var:
                        m_blanket.append(c)
                i += 1

        # add parents of children
        for child in m_blanket:
            i = 0
            while i < len(self.dependencies[child]):
                x, p, pr = self.dependencies[child][i]
                if x!= [] and p != []:
                    copy_m_blanket.append(p[0])
                i += 1

        m_blanket += copy_m_blanket

        # add parent
        i = 0
        while i < len(self.dependencies[var]): 
            par, p, pr = self.dependencies[var][i] 
            if par != []: # if par is not empty
                m_blanket.append(par[0]) 
            i += 1

        m_blanket = set(m_blanket)
        m_blanket.remove(var)
        return list(m_blanket)


class MyCS(ConstraintSearch):

    def __init__(self,domains,constraints):
        ConstraintSearch.__init__(self,domains,constraints)
        pass

    def propagate(self,domains,var):
        # Find all edges that have var as the target
        listofEdges = [(x1, k) for (x1, k) in self.constraints if k == var]

        while listofEdges != []:
            # Get the next edge
            (i, j) = listofEdges.pop()
            lenofValues = len(domains[i]) 
            c = self.constraints[i, j] # Get the constraint for the edge (i, j)

            domains[i] = [value for value in domains[i] 
                        if any(c(i, value, j, value1) for value1 in domains[j])]
   
            if len(domains[i]) < lenofValues:
                listofEdges += [(x1, k) for (x1, k) in self.constraints if k == i]
        return domains

    def higherorder2binary(self,ho_c_vars,unary_c):
        aux = ''.join(ho_c_vars)

        self.domains[aux] = [a for a in self.produto_cartesiano(self.domains, ho_c_vars) if unary_c(a)]

        for (i, var) in enumerate(ho_c_vars):
            self.constraints[var, aux] = lambda v,vx,av,avx : vx == aux[i]
            self.constraints[aux, var] = lambda av,avx,v,vx  : vx == aux[i]

        return aux

    def produto_cartesiano(self,domains, lvars):
        if lvars==[]:
            return [()]

        rec = self.produto_cartesiano(domains, lvars[1:])
        v = lvars[0]
        return [ (x,)+ a for a in rec for x in domains[v] ]