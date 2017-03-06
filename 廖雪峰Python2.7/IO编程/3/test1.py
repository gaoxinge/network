try:
    import cPickle as pickle
except ImportError:
    import pickle

f = open('dump.txt', 'rb')
print pickle.load(f)
f.close()
