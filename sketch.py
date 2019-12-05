import urllib.request
import os 
import numpy as np

DATABASE_URL = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'

def download_and_load(test_split = 0.2, max_items_per_class = 10000):
  root = 'data'
  os.mkdir('data')
  print('Downloading ...')
  for img_class in class_names:
    path = DATABASE_URL + img_class +'.npy'
    urllib.request.urlretrieve(path, f'{root}/{img_class}.npy')
  print('Loading ...')
  
  x = np.empty([0, 784])
  y = np.empty([0])

  for idx, file in enumerate(class_names):
      data = np.load(f'{root}/{file}.npy')
      data = data[0: max_items_per_class, :]
      labels = np.full(data.shape[0], idx)

      x = np.concatenate((x, data), axis=0)
      y = np.append(y, labels)

  data = None
  labels = None

  # Randomização
  permutation = np.random.permutation(y.shape[0])
  x = x[permutation, :]
  y = y[permutation]

  # Reshape 
  x = 255 - np.reshape(x, (x.shape[0], 28, 28))

  # Data split 
  test_size  = int(x.shape[0]/100*(test_split*100))

  x_test = x[0:test_size, :]
  y_test = y[0:test_size]

  x_train = x[test_size:x.shape[0], :]
  y_train = y[test_size:y.shape[0]]
  
  print('Training Data : ', x_train.shape[0])
  print('Testing  Data : ', x_test.shape[0])
  return x_train, y_train, x_test, y_test, class_names