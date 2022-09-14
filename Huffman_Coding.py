# Huffman Coding for binary data, Given Symbol Probabilities 
class nodes:
    def __init__(self,symbol='-',probability=0,left=None,right=None):
        self.symbol = symbol
        self.probability = probability
        self.left = left
        self.right = right
    
def huffman_tree(symbols,probability):
    ls = []
    for i in range(0,len(symbols)):
        node = nodes(symbols[i],probability[i])
        ls.append(node)
    ls.sort(key = lambda x:x.probability)
    prev = ls[0]
    summ=ls[0].probability
    for i in range(1,len(ls)):
        curr = None
        prob = ls[i].probability
        if summ > prob:
            curr = nodes('-',0,ls[i],prev)
        else:
            curr = nodes('-',0,prev,ls[i])
        summ = summ+prob
        prev = curr
    root = prev
    dictionary = {}
    encode(root,"",dictionary)
    return dictionary
    
def encode(root,string,dictionary):
    if root.left is None and root.right is None:
        dictionary[root.symbol] = string
        return
    encode(root.left,string+'1',dictionary)
    encode(root.right,string+'0',dictionary)
    
symbols = ['x1','x2','x3','x4','x5','x7','x6']
probability = [0.37,0.33,0.16,0.07,0.04,0.01,0.02]
print(huffman_tree(symbols,probability))
