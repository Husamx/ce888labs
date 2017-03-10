
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Activation, Embedding, Flatten, Input,PReLU,Dropout,Convolution1D,GlobalMaxPooling1D,LSTM,merge
from keras.datasets import imdb

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

print (X_train[0])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')


inputs = Input(shape=(maxlen,))
x = inputs
x = Embedding(max_features, 128, dropout=0.2)(x)

y = LSTM(64)(x)

#x = Dense(64)(x)
#x = PReLU()(x)
#x = Dropout(0.5)(x)
x = Convolution1D(64, 3)(x)
x = GlobalMaxPooling1D()(x)

z = merge([x,y])

z = Dense(1)(z)



#x = LSTM(64)(x)

#model = Sequential()
#model.add(x)
#model.add(Dense(64,activation = 'relu'))
#model.add(Dropout(0.25))
#model.add(Convolution1D(64,filter_length=3))
#model.add(MaxPooling1D(pool_length=2))


predictions = Activation("sigmoid")(z)


model = Model(input=inputs, output=predictions)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)