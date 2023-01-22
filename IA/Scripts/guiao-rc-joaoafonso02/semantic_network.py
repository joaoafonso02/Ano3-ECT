
from collections import Counter
# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

from functools import total_ordering


class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return str(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

    # SEMANTIC NETWORK - GUIDE 
    def list_associations(self): 
        associations = []
        for d in self.declarations:
            if d.relation.name not in associations and d.relation.name not in ["subtype", "member"]:
                associations.append(d.relation.name)
        return associations

    def list_objects(self):
        objects = []
        for d in self.declarations:
            if d.relation.entity1 not in objects and  d.relation.name == "member":
                objects.append(d.relation.entity1)
        return objects

    def list_users(self):
        users = []
        for d in self.declarations:
            if d.user not in users: # if user not in users list, add him
                users.append(d.user)
        return users

    def list_types(self):
        types = []
        for t in self.declarations:
            if t.relation.name == "subtype":
                if t.relation.entity1 not in types:
                    types.append(t.relation.entity1)
                if t.relation.entity2 not in types:
                    types.append(t.relation.entity2)
            if t.relation.name == "member" and t.relation.entity2 not in types:
                    types.append(t.relation.entity2)
        return types

    def list_local_associations(self, entity):
        # total_associations = []
        # for d in self.declarations:
        #     if d.relation.entity1 == entity and d.relation.name not in total_associations + ["subtype", "member"]:
        #         total_associations.append(d.relation.name)
        return {d.relation.name for d in self.declarations if d.relation.entity1 == entity and d.relation.name not in ["member", "subtype"]}

    def list_relations_by_user(self, user):
        return list(dict.fromkeys([d.relation.name for d in self.declarations if d.user == user]))

    def associations_by_user(self, user):
        return len({d.relation.name for d in self.declarations if d.user == user and d.relation.name not in ["member", "subtype"]})

    def list_local_associations_by_entity(self, user):
        pass

    def predecessor(self, pred, desc):
        ldecl = self.query_local(e2=pred, rel="subtype")
        ldecl += self.query_local(e2=pred, rel="member")
        lchild = [d.relation.entity1 for d in ldecl]

        for c in lchild:
            if c == desc or self.predecessor(c, desc):
                return True
        
        return False
        
    def predecessor_path(self, pred, desc):
        ldecl = self.query_local(e2=pred, rel="subtype")
        ldecl += self.query_local(e2=pred, rel="member")
        lchild = [d.relation.entity1 for d in ldecl]

        for c in lchild:
            if c == desc:
                return [pred, desc]
            path = self.predecessor_path(c, desc)
            if path != None:
                return [pred] + path 
        return None

    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result

    def query(self, entity, assoc = None):
        parents = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, (Member, Subtype)) and d.relation.entity1 == entity]
        
        ldecl = [d for d in self.query_local(e1 = entity, rel = assoc) if isinstance(d.relation, Association)]
        for p in parents:
            ldecl += self.query(p, assoc)
        return ldecl


    def query2(self, entity, rel = None):
        ldecl = [d for d in self.query_local(e1 = entity, rel = rel) ]
        return ldecl + self.query(entity, rel)

    def query_cancel(self, entity, assoc = None):
        ldecl = [d for d in self.query_local(e1 = entity, rel = assoc)]

        if ldecl == []:
            parents = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, (Member, Subtype)) and d.relation.entity1 == entity]
            for p in parents:
                ldecl += self.query_cancel(p, assoc)
        return ldecl

    def query_down(self, entity, assoc, first=True):
        
        desc = [self.query_down(d.relation.entity1, assoc, first=False) for d in self.declarations if isinstance(d.relation, (Member, Subtype)) and d.relation.entity2 == entity]

        # list of lists becomes a  lists with all elems   
        desc_query = [d for sublist in desc for d in sublist]

        local = []
        if not first:
            local = self.query_local(e1=entity, rel=assoc)

        return desc_query + local

    def query_induce(self, entity, assoc):
        desc = self.query_down(entity, assoc)

        values = [d.relation.entity2 for d in desc]

        c = Counter(values).most_common(1)

        for val, _ in c:    # o '_' quer dizer dont care, estamos a extrair o tuplo, mas só estamos interessados no 1o elemento, o val
            return val

        return None # não necessário, já retorna none anyways

