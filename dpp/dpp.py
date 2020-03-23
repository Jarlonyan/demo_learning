
import numpy as np
import math

def dpp(L, max_len, epsilon=1E-10):
    M = L.shape[0]
    cis = np.zeros((max_len, M))
    di2s = np.copy(np.diag(L))
    j = np.argmax(di2s)
    Yg = [j]
    while len(Yg) < max_len:
        k = len(Yg) -1
        cj = cis[:k, j]
        dj = math.sqrt(di2s[j])
        elements = L[j, :]
        eis = (elements - np.dot(cj, cis[:k, :])) / dj
        cis[k,:] = eis
        di2s -= np.square(eis)
        j = np.argmax(di2s)
        if di2s[j] < epsilon:
            break
        Yg.append(j)
    return Yg

def main():
    M = 1000
    D = 256
    max_len = 20

    scores = np.exp(0.01*np.random.rand(M) + 0.2)
    feature_vectors = np.random.randn(M, D)
    feature_vectors /= np.linalg.norm(feature_vectors, axis=1, keepdims=True)

    S = np.dot(feature_vectors, feature_vectors.T)
    L = scores.reshape((M,1)) * S * scores.reshape((1, M))

    res = dpp(L, max_len)
    print res 

if __name__ == '__main__':
    main()
