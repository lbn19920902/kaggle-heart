import glob
import matplotlib.pyplot as plt
import os
import numpy as np
import cPickle as pickle

file = '~/storage/metadata/kaggle-heart/train/*dense*.pkl'

filename = '~/storage/metadata/kaggle-heart/train/*dense*.pkl'
data = pickle.load(open(file, "r"))
train_losses = data['losses_train']
valid_losses = data['losses_eval_valid']

fig = plt.figure()

mngr = plt.get_current_fig_manager()
# to put it into the upper left corner for example:
mngr.window.setGeometry(50, 100, 640, 545)
plt.title(filename)
x_train = np.arange(len(train_losses))+1

plt.gca().set_yscale('log')
plt.plot(x_train, train_losses)
if len(valid_losses)>=1:
    x_valid = np.arange(0,len(train_losses),1.0*len(train_losses)/len(valid_losses))+1
    plt.plot(x_valid, valid_losses)
plt.show()

print "done"