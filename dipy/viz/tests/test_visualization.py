import numpy as np
import matplotlib.pyplot as plt
from numpy import zeros

imga = zeros([128,128])


def intensity_adjustment(data,rate):
    r""" This function enables changing the MRI image contrast.

    It first read the data, must be a 2D image (a specific slice image in MRI),
    then calaulate the image intensity histogram, and based on the rate value to
    decide what is the upperbound value for intensity normalization, the lowerbound
    is 0.

    Parameters
    -----------
    data : a two dimensional array representing one MRI slice image
    rate : a float point value representing the threshold whether a spicific
           histogram bin should be count in the normalization range

    Returns
    -------
    high : the upper_bound value for normalization

    References
    ----------

    Notes
    -----

    See also
    --------
    dipy.viz.utils.upper_bound
    """

    g,h = np.histogram(data)
    m = np.zeros((10,3))
    low = data.min()
    high = data.max()
    for i in np.array(range(10)):
        m[i,0] = g[i]
        m[i,1] = h[i]
        m[i,2] = h[i+1]

    g = sorted(g,reverse = True)
    S = np.size(g)
#    Rate = 0.05
    Index = 0

    for i in np.array(range(S)):
        if g[i]/g[0] > rate:
            Index = Index + 1

    for i in np.array(range(10)):
        for j in np.array(range(Index)):
            if g[j] == m[i,0]:
                high = m[i,2]
    print(high)
    return high


for y in range(128):
    for x in range(128):
        if y > 39 and y < 88 and x > 39 and x <88:
            imga[x,y] = 100
        if y > 59 and y < 69 and x > 59 and x < 69:
            imga[x,y] = 255

rate = 0.1
high = intensity_adjustment(imga,rate)
vol = np.interp(imga, xp=[imga.min(), high], fp=[0, 255])

plt.imshow(imga,"gray")

figure()
plt.imshow(vol,"gray")
