import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 0, 0]
print(data)

data[0:5, 0:2] = [0, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')


