#blurred the image
%matplotlib notebook

import matplotlib.pyplot as plt

import numpy as np


def blurred(img):
    img_slice =(    img[1:-1 ,1:-1]  # center
                + img[ :-2 ,1:-1]  # top
                + img[2:   ,1:-1]  # bottom
                + img[1:-1 , :-2]  # left
                + img[1:-1 ,2:  ]  # right
                ) / 5.0
    return img_slice

img = plt.imread('dc_metro.png') i8
blur_img = blurred(img)

for i in range(30):
    blur_img = blurred(30)

plt.figure()
plt.gray()


plt.subplot(1,3,1)



plt.show()

