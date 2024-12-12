class Layer:
    def __init__(self, name='Layer'):
        self.next_layer = None
        self.name = name

    def __call__(self, obj, *args, **kwargs):
        self.next_layer = obj
        return obj


class Input(Layer):
    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'

class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        x = self.network
        while x:
            yield x
            x = x.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)