from scipy.misc import imsave, imread, imresize
import numpy as np
x = imread('test3.png',mode='L')
#compute a bit-wise inversion so black becomes white and vice versa
x = np.invert(x)
#make it the right size
x = imresize(x,(28,28))
#convert to a 4D tensor to feed into our model
x = x.reshape(1,28,28,1)
x = x.astype('float32')
x /= 255
#print(x)

#perform the prediction
from keras.models import load_model
model = load_model('dense.h5')
out = model.predict(x)
print(np.argmax(out))