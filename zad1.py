import numpy as np

def Funkcja(f, g):
    assert isinstance(f, np.ndarray), "Podany parametr nie jest tablicą ndarray !"
    assert isinstance(g, np.ndarray), "Podany parametr nie jest tablicą ndarray !"
    assert f.size == g.size, "Tablice nie sa jednakowej dlugosci !"

    MSE = np.array([])
    SNR = np.array([])
    MSE = (1/f.size)*sum((f-g)**2)
    SNR = 10*np.log10((sum(f**2)/sum((f-g)**2)))

    return (MSE, SNR)


if __name__ == '__main__':
    f = np.array([11, 12, 13, 14, 15, 3])
    g = np.array([1, 2, 3, 4, 5, 1])


    try:
        print(f"MSE: {Funkcja(f, g)[0]}, SNR: {Funkcja(f, g)[1]}")
    except(AssertionError) as err:
        print("Blad: ", err)