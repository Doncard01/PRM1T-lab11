import numpy as np

def Funkcja(N):
    assert isinstance(N, int), "Podany parametr nie jest intem !"
    assert N >= 1, "Parametr musi byc liczbą naturalną !"
    tab = np.arange(1, N+1)
    wynik = (1+1/tab)**tab
    roznica = np.e-wynik
    return wynik, roznica


if __name__ == '__main__':
    try:
        wynikiObliczen = Funkcja(15)[0]
        roznica = Funkcja(15)[1]
        print(f"Wyniki obliczeń: \n {wynikiObliczen} \n\n Różnica poszczególnych wyników z liczbą Eulera: \n {roznica}")

    except(AssertionError) as err:
        print("Blad: ", err)