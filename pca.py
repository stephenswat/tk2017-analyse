import numpy
import matplotlib.pyplot
from sklearn.decomposition import PCA
import data

dims = 2

pca = PCA(n_components=dims)
pca.fit(data.votes)
fit = pca.transform(data.votes)

fig = matplotlib.pyplot.figure()
if dims == 3:
    ax = fig.add_subplot(projection='3d')
    ax.set_title('3D PCA Nederlandse Politiek')
    ax.scatter(fit[:,0], fit[:,1], fit[:,2])
    for i, txt in enumerate(data.names):
        ax.text(fit[i,0],fit[i,1], fit[i,2], txt)
elif dims == 2:
    ax = fig.add_subplot()
    ax.set_title('2D PCA Nederlandse Politiek')
    ax.scatter(fit[:,0], fit[:,1])
    for i, txt in enumerate(data.names):
        ax.text(fit[i,0],fit[i,1], txt)
else:
    raise ValueError("Must be 2D or 3D.")

matplotlib.pyplot.show()
