import mnist_loader
import network
import numpy as np
import os.path as path
import canvas

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

net = network.Network([784, 40, 10])
if path.exists("./miEntrenamiento.json"):
   pass
else:
    #net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    net.SGD(training_data, 30, 10, 4.5, test_data=test_data)
    net.SaveData()

drawNumber = canvas.AllCanvas()
drawNumber = [ [y] for y in drawNumber]
res = net.feedforward(drawNumber)
res = np.argmax(res)
drawNumber = canvas.finalWindow("El numero es " + str(res))

