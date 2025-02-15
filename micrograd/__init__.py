from engine import Value
from drawing import draw_dot
from nn import Neuron, MLP
import random

#x = Value(1.0, label='x')
#b = Value(3.0, label='b')
#y = (2 * x + 1).relu()
#y.backward()
#draw_dot(y)

random.seed(1337)
n = Neuron(2, nonlin=False)
print("neuron weights:", n.w)
x = [Value(1.0, label='x0'), Value(2.0, label='x1')]
y = n(x); y.label = 'y'
y.backward()
print("y:", y)
draw_dot(y)


model = MLP(3, [1, 1, 1])
print("number of parameters", len(model.parameters()))
print(model)

