# ============================================================
# Problem: Binary Search - Nearest Neighbors
# Technique: Binary Search variants (lower / upper bound)
# Language: Python
# ============================================================

def find_max_less_than_x(arr, x):
    """Devuelve el mayor elemento estrictamente menor que x (o -1)."""
    low = 0
    high = len(arr) - 1
    result = -1  # Valor que indica "no encontrado"

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            result = arr[mid]  # Candidato actual
            low = mid + 1      # Busca a la derecha (valor mayor)
        else:
            high = mid - 1     # Busca a la izquierda

    return result


def find_min_greater_than_x(arr, x):
    """Devuelve el menor elemento estrictamente mayor que x (o -1)."""
    low = 0
    high = len(arr) - 1
    result = -1  # Valor que indica "no encontrado"

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > x:
            result = arr[mid]  # Candidato actual
            high = mid - 1     # Busca a la izquierda (valor menor)
        else:
            low = mid + 1      # Busca a la derecha

    return result


if __name__ == '__main__':
    n_ladies = int(input())
    h_ladies = list(map(int, input().split()))
    n_luchu = int(input())
    h_luchu = list(map(int, input().split()))

    # Elimina duplicados y ordena para habilitar la búsqueda binaria
    h_ladies_clean = sorted(list(set(h_ladies)))

    for x in h_luchu:
        max_less = find_max_less_than_x(h_ladies_clean, x)
        min_greater = find_min_greater_than_x(h_ladies_clean, x)

        # Formatea la salida según el problema
        if max_less == -1:
            print("X", end=" ")
        else:
            print(max_less, end=" ")

        if min_greater == -1:
            print("X")
        else:
            print(min_greater)
