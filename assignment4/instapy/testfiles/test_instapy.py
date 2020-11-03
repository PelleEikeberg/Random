from instapy import grayscale_image, sepia_image
import numpy as np
from numpy.random import randint


def test_grayscale_image_allthesame():
    """testing all the pixels are of same value RGB = [x,x,x]"""
    H = randint(1, 200)
    W = randint(1, 200)

    X = randint(256, size=(H, W, 3), dtype=np.uint8)

    A = grayscale_image(X, implementation="python")
    B = grayscale_image(X, implementation="numpy")
    C = grayscale_image(X, implementation="numba")

    def onearray(A):
        Ar = A[:, :, 0]
        Ag = A[:, :, 1]
        Ab = A[:, :, 2]

        Atest1 = (Ar == Ag).all() == True
        Atest2 = (Ar == Ab).all() == True

        Atest3 = False
        if Atest1 and Atest2:
            Atest3 = True

        return Atest3

    assert ((onearray(A) == True) == (onearray(B) == True)) == (onearray(C) == True)


def test_grayscale_image_rndexpected():
    H = randint(1, 200)
    W = randint(1, 200)

    X = randint(256, size=(H, W, 3), dtype=np.uint8)

    A = grayscale_image(X, implementation="python")
    B = grayscale_image(X, implementation="numpy")
    C = grayscale_image(X, implementation="numba")

    def randomtest(A):
        i, j = randint(0, H), randint(0, W)

        expected = X[i, j, 0] * 0.07 + X[i, j, 1] * 0.72 + X[i, j, 2] * 0.21

        Ar = A[i, j, 0] == expected
        Ag = A[i, j, 1] == expected
        Ab = A[i, j, 2] == expected

        if ((Ar == True) == (Ag == True)) == (Ab == True):
            return True
        else:
            return False

    assert ((randomtest(A) == True) == (randomtest(B) == True)) == (
        randomtest(C) == True
    )


def test_sepia_image_all():
    H1 = randint(1, 200)
    W1 = randint(1, 200)

    X = randint(256, size=(H1, W1, 3), dtype=np.uint8)

    A1 = sepia_image(X, implementation="python")
    A2 = sepia_image(X, implementation="numpy")
    A3 = sepia_image(X, implementation="numba")

    def arraytesting(A1):
        # the weights for sepia given
        W = np.array(
            [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
        )
        S0 = np.sum(W[0])
        S1 = np.sum(W[1])
        S2 = np.sum(W[2])
        Scale = max([S0, S1, S2])
        Scale = 1 / Scale

        R, G, B = X[:, :, 0], X[:, :, 1], X[:, :, 2]
        # sets the grayscale
        Rs = (W[2, -1] * R + W[2, -2] * G + W[2, -3] * B) * Scale
        Gs = (W[1, -1] * R + W[1, -2] * G + W[1, -3] * B) * Scale
        Bs = (W[0, -1] * R + W[0, -2] * G + W[0, -3] * B) * Scale
        # sets the new RGB values.
        X[:, :, 0] = Rs
        X[:, :, 1] = Gs
        X[:, :, 2] = Bs

        r = (A1[:, :, 0] == X[:, :, 0]).all() == True
        g = (A1[:, :, 0] == X[:, :, 0]).all() == True
        b = (A1[:, :, 0] == X[:, :, 0]).all() == True

        if ((r == True) == (g == True)) == (b == True):
            return True
        else:
            return False

    assert ((arraytesting(A1) == True) == (arraytesting(A2) == True)) == (
        arraytesting(A3) == True
    )


if __name__ == "__main__":
    test_grayscale_image_allthesame()
    test_grayscale_image_rndexpected()
    test_sepia_image_all()
