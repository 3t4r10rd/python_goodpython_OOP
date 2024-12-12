class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.stack = []

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.stack[-1].next = obj
        self.stack.append(obj)

    def pop(self):
        self.stack.pop()
        if self.stack:
            self.stack[-1].next = None
        else:
            self.top = None

    def __getitem__(self, item):
        return self.stack[item]

    def __setitem__(self, key, value):
        self.stack[key] = value
        if key != 0:
            self.stack[key-1].next = value
        self.stack[key].next = self.stack[key+1] if key+1 < len(self.stack) else None


st = Stack()
st.push(StackObj('obj1'))
st.push(StackObj('obj2'))
st.push(StackObj('obj3'))

st[1] = StackObj('new obj')

print(st[2].data)
print(st[1].data)

print(st[0].next.data)