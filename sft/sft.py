from math import log
from math import pi
from numpy import abs
from numpy import arange
from numpy import asarray
from numpy import exp
from numpy import hstack
from numpy import vstack
from numpy import zeros

def triangular(N):
   """triangular weight"""

   nk = arange(N/2)
   W = 2 * abs( 2 * nk / N - 1) - 1 + 0j
   W -= (1 - abs(4 * nk / N - 1)) * 1j
#   W[nk >= N/2] -= (np.abs(4 * nk / N - 3) - 1)[nk >= N/2] * 1j

   return W

def exponential(N):
    """exponential weight"""

    nk = arange(N/2)
    return exp(-2j * pi * nk / N)

def fft(xcx, N=0, W=exponential):
    """perform fft"""

    Xcx = asarray(xcx[:N], dtype=complex)
    N = min(N, Xcx.shape[0])

    Wcx = W(N)

    Xcx = sort(Xcx)

    m = int(log(N, 2))
    l1 = 1
    l3 = N

    for l in range(m):

        l2 = l1
        l1 <<= 1
        l3 = l3/2
        k1 = 0

        for j in range(l2):
            Wt = Wcx[k1]
            k1 += l3
            for i in range(j, N, l1):
                i1 = i + l2
                Tcx = Xcx[i1] * Wt
                Xcx[i1] = Xcx[i] - Tcx
                Xcx[i] += Tcx

    return Xcx

def sort(Xcx):
    """sort fft"""

    N = Xcx.shape[0]
    N2 = int(N/2)
    N1 = N - 1
    j = 0

    for i in range(N1):
        if i<j:
            Tcx = Xcx[j]
            Xcx[j] = Xcx[i]
            Xcx[i] = Tcx
        k = N2
        while(k<=j):
            j -= k
            k >>= 1
        j += k

    return Xcx
