import numpy as np

def Funkcja(N):
    assert isinstance(N, int), "Podany parametr nie jest intem !"
    tab = np.arange(1, N+1)
    wynik = (1+1/tab)**tab
    roznica = np.e-wynik
    return wynik, roznica


if __name__ == '__main__':
    try:
        print(Funkcja(15))
    except(AssertionError) as err:
        print("Blad: ", err)