
import sys
from fractions import gcd
from time import time
from random import random
import numpy as np
# from numpy import array, nonzero, hstack, vstack, eye, np.sign, argsort, sum, abs, np.zeros
from numpy.linalg import matrix_rank
from scipy.io import savemat


def sampler(smatrix, rev, K=None, debug=False):
    """ Implements an elementary mode sampler.
    Inputs: smatrix (stoichiometric matrix), rev (reversibility vector), K (tunable parameter to adjust output size).
    Note: if K is undefined it will compute all modes.
    For more information consult the respective paper (Machado et al; 2012) (submitted).
    """

    p = (lambda N: K / (K + float(N))) if K else (lambda N: 1)

    smatrix = np.array(smatrix)

    # sort matrix
    order = np.argsort(np.sum(np.abs(np.sign(smatrix)), 1))
    smatrix = smatrix[order, :]

    (m, n) = smatrix.shape
    T = np.hstack((smatrix.T, np.eye(n)))
    reversibility_vector = np.array(rev)
    assert isinstance(reversibility_vector, np.ndarray) and len(reversibility_vector.shape) == 1

    if debug:
        tstart = time()
        print 'starting computation...'

    for i in range(m):
        nonzero_columns = np.nonzero(T[ :, 0 ] == 0)[0 ]
        zero_columns = np.nonzero(T[ :, 0 ])[0 ]

        T2 = np.zeros((0, T.shape[1] - 1))
        revT2 = np.zeros((0,))

        nrev = len(np.nonzero(reversibility_vector[zero_columns])[0])  # will always be 0 because of my reversibility vector = 0
        irr = np.nonzero(reversibility_vector == 0)[0]  # shrinking on each iteration but an entire vector
        npos = len(np.nonzero(T[irr, 0] > 0)[0])
        nneg = len(np.nonzero(T[irr, 0] < 0)[0])
        npairs = nrev * (nrev - 1) / 2 + nrev * (npos + nneg) + npos * nneg
        assert isinstance(nrev, int)
        assert isinstance(irr, np.ndarray) and len(irr.shape) == 1
        assert isinstance(npos, int)
        assert isinstance(nneg, int)
        assert isinstance(npairs, int)

        if debug:
            keep = nonzero_columns.shape[0]
            print 'line {} of {} - keep: {} combinations: {}'.format(i + 1, m, keep, npairs),

        pairs = ((j, k) for j in zero_columns for k in zero_columns
                 if k > j and (reversibility_vector[j] or reversibility_vector[k] or T[j, 0] * T[k, 0] < 0))

        first_i_rows = smatrix[:i + 1, :]
        assert isinstance(smatrix, np.ndarray) and len(smatrix.shape) == 2

        for j, k in pairs:
            # because I only have a case where revesibility vector is all False
            # if reversibility_vector[j ] and reversibility_vector[k ]:
            #     cj, ck = -T[k, 0], T[j, 0]
            # elif reversibility_vector[j ] and not reversibility_vector[k ]:
            #     cj, ck = -np.sign(T[j, 0]) * T[k, 0], np.sign(T[j, 0]) * T[j, 0]
            # elif not reversibility_vector[j ] and reversibility_vector[k ]:
            #     cj, ck = np.sign(T[k, 0]) * T[k, 0], -np.sign(T[k, 0]) * T[j, 0]
            # else:
            #     cj, ck = abs(T[k, 0]), abs(T[j, 0])
            cj, ck = abs(T[k, 0]), abs(T[j, 0])

            Tj, Tk = cj * T[j, 1:], ck * T[k, 1:]
            assert isinstance(Tj, np.ndarray) and len(Tj.shape) == 1
            assert isinstance(Tk, np.ndarray) and len(Tk.shape) == 1
            Tjk = Tj + Tk
            revTjk = reversibility_vector[j] and reversibility_vector[k]  # will always be 0

            minimal = all(np.abs(Tj[(m - i - 1):]) + np.abs(Tk[(m - i - 1):]) == np.abs(Tjk[(m - i - 1):])) \
                          and _rank_test(first_i_rows, np.nonzero(Tjk[(m - i - 1):])[0])

            if minimal:
                T2 = np.vstack((T2, Tjk))
                revT2 = np.hstack((revT2, revTjk))

        t = p(T2.shape[0]) if T2.shape[0] else 0
        selection = [i for i in range(T2.shape[0]) if random() <= t]
        T = np.vstack((T[ nonzero_columns, 1: ], T2[ selection, : ])) if selection else T[ nonzero_columns, 1: ]
        reversibility_vector = np.hstack((reversibility_vector[nonzero_columns ], revT2[selection ])) \
                                           if selection else reversibility_vector[nonzero_columns ]

        if debug:
            total = T.shape[0]
            new = total - keep
            print 'new: {} total {}'.format(new, total)

    if debug:
        tend = time()
        print 'computation took:', (tend - tstart)
        print 'post-processing... ',

    E = map(_normalize, T)
    E = map(lambda e: e.tolist(), E)

    if debug:
        print 'done'
        print 'Found {} modes.'.format(len(E))

    return E


def _rank_test(S, Sjk):
    if len(Sjk) > S.shape[0] + 1:
        return False
    else:
        return len(Sjk) - matrix_rank(S[:, Sjk]) == 1


def _normalize(e):
    support = abs(e[np.nonzero(e)[0]])
    n1 = reduce(gcd, support)  # greatest common denominator
    n2 = (min(support) * max(support)) ** 0.5  # geometric mean
    n = n1 if (1e-6 < n1 < 1e6) and (1e-6 < n2 < 1e6) else n2
    return e / n

s = [[-1,-1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[0,0,-1,-1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
[0,0,0,0,-1,-1,0,0,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,-1,0,1,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0,-1,0,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,-1,-1,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,0,0,0,-1,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,-1,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,-1,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,-1]]

r = [0 for i in range(len(s[0]))]  # rev = [reaction.getReversible() for reaction in model.getListOfReactions()]


with open('test.txt', 'w+') as f:
    f.write(str(sampler(s, r, K=None, debug=True)))
