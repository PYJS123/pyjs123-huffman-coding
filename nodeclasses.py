# leaf node class
class Leaf:
    def __init__(self, char, freq):
        self.char=char
        self.freq=freq

    def __str__(self):
        # for printing node
        return f'char: \'{self.char}\' \tfrequency: {self.freq}'

# parent node class
class Parent:
    def __init__(self, freq):
        self.left, self.right={}, {}
        self.freq=freq

    def __str__(self):
        # for printing node
        #return f'left: {self.left if self.left!={} else "[empty]"} \tright: {self.right if self.right!={} else "[empty]"} \tfrequency: {self.freq}'
        a="'"
        return f'left: {"[empty]" if self.left=={} else (a+self.left.char+a) if self.left.__class__.__name__=="Leaf" else self.left.freq} \tright: {"[empty]" if self.right=={} else (a+self.right.char+a) if self.right.__class__.__name__=="Leaf" else self.right.freq} \tfrequency: {self.freq}'
