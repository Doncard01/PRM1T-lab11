import numpy as np

def Funkcja(A, y):
    assert isinstance(A, np.ndarray), "Podany parametr nie jest tablicą ndarray !"
    assert isinstance(y, np.ndarray), "Podany parametr nie jest tablicą ndarray !"
    assert np.linalg.det(A) != 0, "Podaj w parametrze macierz nieosobliwą, z wyznacznikiem różnym od 0"

    odwr =  np.linalg.inv(A)
    x = np.dot(odwr, y)
    return x

if __name__ == '__main__':
    A = np.array([[1, 2], [1, -1]])
    y = np.array([3, -3])
    B = np.array([[1, 2], [2, 4]])
    y2 = np.array([9, 18])
    C = np.array([[1, 0, -1, 0, 1], [0, 2, -1, 1, 0], [-1, 1, -1, 1, 0], [1, 2, 0, 2, 1], [2, 0, 2, 0, -1]])
    y3 = np.array([1, 2, 0, 6, 3])

    try:
        print("Obliczanie wartości <x> dla równania macierzowego")
        print(f"Wektor <x> dla podanych parametrów: \n{Funkcja(A, y)}")
    except(AssertionError) as err:
        print("Błąd: ", err)
    try:
        print("Dla drugiego zestawu danych:")
        print(Funkcja(B, y2))
    except(AssertionError) as err:
        print("Błąd: ", err)
    try:
        print("Dla trzeciego zestawu danych:")
        print(Funkcja(C, y3))
    except(AssertionError) as err:
        print("Błąd: ", err)
