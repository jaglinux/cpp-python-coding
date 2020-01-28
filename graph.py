class vertex:
    def __init__(self, val):
        self.val=val
        self.list=[]

class graph():
    def __init__(self):
        self.vertices=[]

    def add_vertex(self, val):
        a=vertex(val)
        self.vertices.append(a)

    def add_link(self, a, b):
        flag=0
        node_a=None
        node_b=None

        for i in self.vertices:
            if a==i.val:
                flag+=1
                node_a=i
            elif b==i.val:
                flag+=1
                node_b=i

        if flag==2:
            node_a.list.append(node_b)
        else:
            print('Nodes not present !')


    def print_vertex(self):
        print('The vertices are')
        for i in self.vertices:
            print(i.val)

    def print_edge(self):
        print('The links are')
        for i in self.vertices:
            print("For Node ", i.val)
            for j in i.list:
                print(j.val)

g=graph()
g.add_vertex(4)
g.add_vertex(5)
g.add_link(4,5)
g.add_link(5,4)
g.add_link(4,7)
g.print_vertex()
g.print_edge()
