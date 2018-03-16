from collections import*
import collections
import math 
from read_char_info import read_char

class Node:
     def __init__(self, left = None, right = None, root = None, f = None):
        self.left = left
        self.right = right
        self.root = root
        self.f = f

     def get_data(self):
        return self.root

     def get_next(self):
        return self.next_node

     def set_next(self, new_next):
        self.next_node = new_next

def printfreq():
    H = []
    N = []
    ch = dict()
    new = []
    char = read_char()
    for i in range(len(char)):
        char[i] = list(char[i])
        l = len(char[i])
        if l > 120:
            del char[i]

    new = collections.Counter(char[0])

    for key, value in new.items():
        ch[key] = value
    return  ch

def printtree(ch):
    cha = dict((v,k) for k,v in ch.items())
    char = []
    val = sorted(ch.values())
    for i in range(len(val)):
        for k,v in cha.items():
            if val[i] == k:
                char.append((k,v))
##    print char
    nodes = []
    p = []

    for f,l in char:
        node = Node()
        node.root = l,f
        node.f = f
        nodes.append(node)


    while len(nodes) > 1:
        node = Node()
        e1 = nodes.pop(0)
        e2 = nodes.pop(0)
        node.root = e1.f + e2.f
        node.f = e1.f + e2.f
        node.f = e1.f + e2.f
        node.left = e1.root
        node.right = e2.root
        insrt(nodes,node)
        p.append(node.left)
        p.append(node.right)
        p.append(node.root)

    print '\n', '\n'
    p.reverse()
    u = list(OrderedDict.fromkeys(p))
    u[5],u[6] = u[6],  u[5]
    level = len(u)
    lvls = int(math.log(level,2)) *2
    lvl = 1
    while len(u) > 0:
         while lvl < lvls:
              if lvl < 3  and len(u) > 0:
                   for i in range(lvl):
                        if not isinstance(u[0],tuple) and len(u) > 0:
                             print '\t'*(lvls-lvl-1), u.pop(0),
                        else:
                             print '\t'*(lvls-lvl-1), u.pop(0)[0],
              if lvl == 3 and len(u) > 0:
                   for i in range(2):
                        if not isinstance(u[0],tuple) and len(u) > 0:
                             print '\t'*(lvls-lvl-1), u.pop(0),'\t',
                        else:
                             print '\t'*(lvls-lvl-1), u.pop(0)[0],'\t',

              if lvl > 3 and len(u) > 0:
                   for i in range(lvl):
                        if len(u) > 0 and not isinstance(u[0],tuple):
                             print '\t'*(lvls-lvl-1), u.pop(0),'\t',
                        else:
                             if len(u) == 0:
                                  break
                             print '\t'*(lvls-lvl-1), u.pop(0)[0],'\t',
              print '\n'
              lvl +=1


def insrt(h,n):
     temp = []
     tmp = []
     h.insert(0,n)
     for node in h:
          temp.append(node.f)
     tmp =  sorted(temp)
     for i in range(len(tmp)):
          for nd in h:
               if tmp[i] == nd.f:
                    newnd = nd
                    h.remove(nd)
                    h.insert(i,nd)
                    


