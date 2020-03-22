
import numpy as np
import math

def dpp(L, max_len, epsilon=1E-10):
    M = L.shape[0]
    cis = np.zeros((max_len, M))
    di2s = np.copy(np.diag(L))
    select_items = list()
    select_item = np.argmax(di2s)
    select_items.append(select_item)
    while len(select_items) < max_len:
        k = len(select_items) -1
        ci_optimal = cis[:k, select_item]
        di_optimal = math.sqrt(di2s[select_item])
        elements = L[select_item, :]
        eis = (elements - np.dot(ci_optimal, cis[:k, :])) / di_optimal
        cis[k,:] = eis
        di2s -= np.square(eis)
        select_item = np.argmax(di2s)
        if di2s[select_item] < epsilon:
            break
        select_items.append(select_item)
    return select_items

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
