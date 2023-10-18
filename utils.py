import numpy as np
import imageio 

def load_and_pad(image_path):
    img = np.array(imageio.imread(image_path))
    pad = max(img.shape[0], img.shape[1])
    img = np.pad(img, ((0, pad - img.shape[0]), (0, pad - img.shape[1]), (0, 0)))
    return img, pad