class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        step = root
        while step.value is None:
            step = step.left if x[step.indx] else step.right
        return step.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, 'программист'), v_11)
DecisionTree.add_obj(TreeObj(-1, 'кодер'), v_11, False)
DecisionTree.add_obj(TreeObj(-1, 'есть шанс'), v_12)
DecisionTree.add_obj(TreeObj(-1, 'безнадега'), v_12, False)

x = [1, 1, 0]

res = DecisionTree.predict(root, x)

print(res)
