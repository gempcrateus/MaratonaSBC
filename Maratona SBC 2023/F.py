def max_activities(D, C, R, activities_c, activities_r):
    # Inicializar contadores e índices
    count = 0
    c_index = 0
    r_index = 0
    
    # Laço enquanto houver atividades cansativas não realizadas
    while c_index < C:
        if D >= activities_c[c_index]:
            # Realiza a atividade cansativa
            D -= activities_c[c_index]
            c_index += 1
        else:
            if r_index < R:
                # Realiza a atividade revigorante
                D += activities_r[r_index]
                r_index += 1
            else:
                # Sem disposição suficiente e sem atividades revigorantes disponíveis
                break
        # Incrementa o contador de atividades realizadas
        count += 1
    
    # Adiciona as atividades revigorantes restantes, se houver
    count += (R - r_index)
    
    return count

# Leitura da entrada
D, C, R = map(int, input().split())
activities_c = [int(input()) for _ in range(C)]
activities_r = [int(input()) for _ in range(R)]

# Chamada da função e impressão do resultado
result = max_activities(D, C, R, activities_c, activities_r)
print(result)