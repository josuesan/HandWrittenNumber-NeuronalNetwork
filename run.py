# ----------------------
# - read the input data:

import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

# ---------------------
# - network.py example:
import network
# Third-party libraries
import numpy as np
import os.path as path
import canvas

test_data1 = list(test_data)
n_test = len(test_data1)
test1= test_data1[0][0]
testResult1 = test_data1[0][1]
#Primera coordenada es la imagen en matriz y la segunda es el valor de esa imagen
test2= test_data1[1][0]
testResult2 = test_data1[1][1]
net = network.Network([784, 30, 10])
if path.exists("./miEntrenamiento.json"):
   #net.ReadData()
   pass
else:
    print ("No existo")
    net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    net.SaveData()

drawNumber = canvas.AllCanvas()
print("El test:")
print(test1.tolist())
#print("El draw:")
#print(drawNumber)
#print("Test case")
#print(len (test1))
#print(type (test1))
#print("Interfaz dibujada")
#print(len(drawNumber))
#print(type (drawNumber))


drawNumber = [ [y] for y in drawNumber]
print(drawNumber)
#for x in drawNumber:
#	test.append([x])
#print(test)
#drawNumber = np.ndarray((784),buffer=np.array(drawNumber),dtype=int)
#print(drawNumber)

#print(len(drawNumber))
#print(type (drawNumber))

res = net.feedforward(drawNumber)
print(res)
res = np.argmax(res)
print("La respuesta caso 1 es:")
print(res)
drawNumber = canvas.finalWindow("El numero es " + str(res))

print("La respuesta caso 2 es:")
res = net.feedforward(test1.tolist())
print(res)
res = np.argmax(res)
print(res)
print(testResult1)


#Segundo caso
''' res = net.feedforward(test2)
print(res)
res = np.argmax(res)
print(res)
print(testResult2)'''

