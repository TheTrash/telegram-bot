#Import
import numpy as np
from keras.preprocessing  import image
#from keras.preprocessing.image import img_to_array
from keras.models import load_model

from numpy.random import seed
seed(98765432)


# width height
w = 224
h = 224



model =  load_model('third_model.h5')


def recognition(filename):
    prediction = ""
    test_image = image.load_img(filename, target_size = (w,h))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image, verbose=1)
    #{'cats': 0, 'dogs': 1}
    if result == 1:
        cl = 'dog'
        res = result[0]*100
    else:
        cl = 'cat'
        res = (1-result[0])*100

    return cl, int(res)

