class ConstraintSearch:

    def __init__(self,domains,constraints):
        self.domains = domains
        self.constraints = constraints
        self.calls = 0

    # def propagate(self,domains,var):
    #     for (v1,v2) in self.constraints:           
    #             if v1 == var: # if v1 is var
    #                 for val in domains[v2]:
    #                     if not self.constraints[v1,v2](v1,domains[v1][0],v2,val):
    #                         domains[v2].remove(val) # removes the value from v2's domain

    #             if v2 == var: # if v2 is var
    #                 for val in domains[v1]:
    #                     if not self.constraints[v1,v2](v1,val,v2,domains[v2][0]):
    #                         domains[v1].remove(val) # removes the value from v1's domain
                            
    def search(self,domains=None):

        self.calls += 1 

        if domains==None:
            domains = self.domains

        if any([lv==[] for lv in domains.values()]):
            return None

        if all([len(lv)==1 for lv in list(domains.values())]):
            solution = { v:domains[v][0] for v in domains }
            # this "if" is not needed after implementing propagation
            if all( self.constraints[v1,v2](v1,solution[v1],v2,solution[v2])
                    for (v1,v2) in self.constraints ): 
                return solution

        for var in domains.keys():
            if len(domains[var])>1:
                for val in domains[var]:
                    newdomains = dict(domains)
                    newdomains[var] = [val]
                    self.propagate(newdomains,var)
                    solution = self.search(newdomains)
                    if solution != None:
                        return solution
        return None
