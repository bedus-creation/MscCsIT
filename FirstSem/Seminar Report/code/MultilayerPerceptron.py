import numpy as np

class MultilayerPerceptron(object):

    def __init__(self, no_of_inputs,no_of_hidden,no_of_outout,learning_rate=0.01):
        self.hidden_weights = np.random.uniform(size=(no_of_inputs,no_of_hidden))
        self.hidden_bias =np.random.uniform(size=(1,no_of_hidden))
        self.output_weights = np.random.uniform(size=(no_of_hidden,no_of_outout))
        self.output_bias = np.random.uniform(size=(1, no_of_outout))
        self.errors = []

    def forward(self, inputs):
        hidden_layer_activation = np.dot(inputs,self.hidden_weights)
        hidden_layer_activation += self.hidden_bias
        hidden_layer_output = self.sigmoid(hidden_layer_activation)

        output_layer_activation = np.dot(hidden_layer_output,self.output_weights)
        output_layer_activation += self.output_bias
        prediction = self.sigmoid(output_layer_activation)
        return prediction, hidden_layer_output
        
    def predictTroll(self, inputs):
        prediction, hidden_layer_output = self.forward(inputs)
        return prediction

    def predict(self, inputs):
        prediction, hidden_layer_output = self.forward(inputs)
        if prediction > 0.5:
          activation = 1
        else:
          activation = 0            
        return activation
    def sigmoid (self,x):
        return 1/(1 + np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1 - x)

    def getErrors(self):
        return self.errors


    def train(self, training_inputs, expected_output,learning_rate=0.1):
        for _ in range(10000):
            predicted_output, hidden_layer_output = self.forward(training_inputs)
            #Backpropagation
            error = expected_output - predicted_output
            temp=0
            for i in error:
                temp = temp + i*i
            self.errors.append(temp[0])
            d_predicted_output = error * self.sigmoid_derivative(predicted_output)
            
            error_hidden_layer = d_predicted_output.dot(self.output_weights.T)
            d_hidden_layer = error_hidden_layer * self.sigmoid_derivative(hidden_layer_output)

            # Updating Weights and Biases
            self.output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
            self.output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * learning_rate
            self.hidden_weights += training_inputs.T.dot(d_hidden_layer) * learning_rate
            self.hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate
