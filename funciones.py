def validar_matrices(cargas, capacidades):
    if len(cargas) != len(capacidades):
        return False

    if len(cargas) < 2:
        return False

    for i in range(len(cargas)):

        if len(cargas[i]) != len(capacidades[i]):
            return False

        if len(cargas[i]) < 2:
            return False

        for j in range(len(cargas[i])):

            if cargas[i][j] < 0:
                return False

            if capacidades[i][j] <= 0:
                return False

    return True
