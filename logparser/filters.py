def filter(pacotes, filtro):
    pacotes_filtrados = []
    for pacote in pacotes:
        if getattr(pacote, filtro.split('=')[0])==filtro.split('=')[1]:
            pacotes_filtrados.append(pacote)

    return pacotes_filtrados

def apply_filters(pacotes, filtros):
    filtros = filtros.split(' ')
    pacotes_filtrados = filter(pacotes, filtros[0])
    if len(filtros) > 1:
        pacotes1 = pacotes_filtrados
        for filtro in filtros[1:]:
            pacotes1 = filter(pacotes1, filtro)

        return pacotes1
    else:
        return pacotes_filtrados
