# Perceptron.py
import numpy as np

class TrollPerceptron(object):
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
        self.errors = [0]
        self.squareError= [0]
        
           
    def predict(self, inputs):
       return np.dot(inputs, self.weights[1:]) + self.weights[0]

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            error = 0
            squareError = 0 
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
                error = error + abs(label - prediction)
                squareError = error + (label - prediction)**2
            self.errors.append(str(error))
            self.squareError.append(str(error))

    def getWeights(self):
        return self.weights

    def getSquareError(self):
        return self.squareError

    def getErrors(self):
        return self.errors