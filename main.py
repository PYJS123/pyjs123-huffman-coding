def huffmantree(string):
    letters=[]
    freqs=[]
    for char in string:
        if char in letters:
            freqs[letters.index(char)]+=1
        else:
            letters.append(char)
            freqs.append(1)

    nodes=[]
    for i in range(len(letters)):
        char, freq=letters[i], freqs[i]
        nodes.append(Leaf(char, freq))

    while len(nodes)>1:
        nodes=mergesort(nodes, func=lambda node:node.freq)
        left=nodes.pop(0)
        right=nodes.pop(0)
        parent=Parent(left.freq+right.freq)
        parent.left=left
        parent.right=right
        nodes.append(parent)

    return nodes[0]

def treelog(tree):
    codes={}
    if tree.__class__.__name__=='Leaf':
        codes[tree.char]=''
    else:
        tleft=treelog(tree.left)
        tleft={x:'0'+tleft[x] for x in tleft}
        tright=treelog(tree.right)
        tright={x:'1'+tright[x] for x in tright}
        codes.update(tleft)
        codes.update(tright)

    return codes

def huffmancode(string):
    tree=huffmantree(string)
    codes=treelog(tree)

    code=""
    for char in string:
        code+=codes[char]

    return code, tree

def huffmandecode(code, tree):
    curr=tree
    decoded=""
    for bit in code:
        if bit=='0':
            curr=curr.left
        else:
            curr=curr.right
        if curr.__class__.__name__=='Leaf':
            decoded+=curr.char
            curr=tree

    return decoded

from nodeclasses import *
from mergesort import *