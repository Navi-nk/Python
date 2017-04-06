import numpy as np 
import time 

n_hidden = 10
n_in = 10
n_out = 10

n_sample = 300

#hyper parameter
learning_rate = 0.01
momemtum = 0.9

#non deterministic seeding
np.random.seed(0)

#sigmoid activation
def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))

#tangent activation
def tanh(x):
	return 1-np.tanh(x)**2

#training
#x is input
#t is transpose for matrix multiplication
#V and W are layers(1 and 2)
#bv and bw are biases for each layer
def train(x, t, V, W, bv, bw):
	#forward propogation
	A = np.dot(x, V) + bv #matrix multiply + bias
	Z = np.tanh(A)

	B = np.dot(Z, W) + bw
	Y = sigmoid(B)

	#back propogation
	Ew = Y - t
	Ev = tanh(A) * np.dot(W, Ew)

	#predict loss
	dW = np.outer(Z, Ew)
	dV = np.outer(x, Ev)

	#cross entroy for classification(gives better than Mean square)
	loss = -np.mean(t * np.log(Y) + (1 - t) * np.log(1-Y))

	return loss, (dV, dW, Ev, Ew)

def predict(x, V, W, bv, bw):
	A = np.dot(x ,V) + bv
	B = np.dot(np.tanh(A), W) + bw
	return (sigmoid(B) > 0.5).astype(int)


#create layers
V = np.random.normal(scale=0.1, size=(n_in, n_hidden))
W = np.random.normal(scale=0.1, size=(n_hidden, n_out))


bv = np.zeros(n_hidden)
bw = np.zeros(n_out)

params = [V , W, bv, bw]

#generate data
X = np.random.binomial(1,0.5,(n_sample,n_in))
T = X ^ 1

#Training
for epoch in range(100):
	err = []
	upd = [0]*len(params)

	t0 = time.clock()

	#for each data point update weights
	for i in range(X.shape[0]):
		loss,grad = train(X[i], T[i], *params)
		#update loss
		for j in range(len(params)):
			params[j] -= upd[j]

		for j in range(len(params)):
			upd[j] = learning_rate * grad[j] + momemtum * upd[j]

		err.append(loss)

	print('Epoch:%d, Loss: %.8f, Time: %.4fs'%(epoch, np.mean(err), time.clock()-t0))


#try to predict some shit

x = np.random.binomial(1, 0.5, n_in)
print('XOR Prediction')
print(x)
print(predict(x,*params))

