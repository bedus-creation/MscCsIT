#app.py
import numpy as np
from Perceptron import Perceptron

training_inputs = []
training_inputs.append(np.array([1, 1]))
training_inputs.append(np.array([1, 0]))
training_inputs.append(np.array([0, 1]))
training_inputs.append(np.array([0, 0]))

labels = np.array([1, 0, 0, 0])

perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)

inputs = np.array([1, 1])
perceptron.predict(inputs) 
#=> 1

inputs = np.array([0, 0])
print("inputs "+str(inputs)+" Output "+str(perceptron.predict(inputs)))

inputs = np.array([0, 1])
print("inputs "+str(inputs)+" Output "+str(perceptron.predict(inputs)))

inputs = np.array([1, 1])
print("inputs "+str(inputs)+" Output "+str(perceptron.predict(inputs)))