def exercicio1(vetor: tuple) -> int | float:
    if not isinstance(vetor, tuple):
        raise TypeError('O argumento deve ser do tipo tupla')
    
    soma_norma = 0
    for coord in vetor:    
        if not isinstance(coord, (int, float)):
            raise ValueError('A tupla deve conter apenas números inteiros ou float')
        
        soma_norma += coord * coord
        
    return soma_norma ** 0.5  # Calcula a norma euclidiana


def exercicio2(ponto_1: tuple, ponto_2: tuple) -> tuple:

    if not isinstance(ponto_1, tuple) or not isinstance(ponto_2, tuple):
        raise TypeError('Você não deu algum ponto do tipo tupla') 
    
    if len(ponto_1) != 2 or len(ponto_2) != 2:
        raise ValueError('Tamanho da tupla errado. Tamanho esperado: 2')

    for i in range(len(ponto_1)):
        if not isinstance(ponto_1[i], (int, float)):
            raise ValueError('Você não deu um valor apenas com números no ponto 1')
        if not isinstance(ponto_2[i], (int, float)):
            raise ValueError('Você não deu um valor apenas com números no ponto 2')

    if ponto_2[0] == ponto_1[0]:
        raise ZeroDivisionError('Divisão por zero no cálculo do coeficiente angular')

    coef_ang = (ponto_2[1] - ponto_1[1]) / (ponto_2[0] - ponto_1[0])
    b = ponto_1[1] - coef_ang * ponto_1[0]
    
    return coef_ang, b
