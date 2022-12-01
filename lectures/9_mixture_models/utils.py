import numpy as np

def create_mixture(pis, mus, Sigmas, N=5000, rseed=None):
    """
    pis (list of floats): mixing coefficients : cluster importance
    mus (list of arrays): mean: cluster centers
    Sigmas (list of arrays): covariance: cluster shape
    N (int): number of points to create
    """
    if rseed is not None:
        np.random.seed(rseed)
    points = list()
    labels = list()
    for k in range(len(pis)):
        Nc = int(pis[k]*N)
        if len(mus[k]) > 1:
            x = np.random.multivariate_normal(mus[k], Sigmas[k], Nc)
        else:
            x = mus[k] + np.sqrt(Sigmas[k])*np.random.randn(Nc)
        points.append(x)
        labels.append([k]*Nc)
    return np.concatenate(points), np.concatenate(labels)