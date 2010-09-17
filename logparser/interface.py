#encoding: utf-8

from monografia.filters import apply_filters
from monografia.utils import *
from monografia.parsers import parser_log_to_objects

x = ''
mensagem_sucesso_relatorio = """
                             ----------------------------------------
                             | Observe o relatorio gerado no browser|
                             ----------------------------------------
                             """
def macro_sucesso_acao(pacotes_filtrados):
    print mensagem_sucesso_relatorio
    return generate_report(pacotes_filtrados)


log = raw_input('Caminho do arquivo: ')
try:
    pacotes = parser_log_to_objects(open(log,'r'))
    print '''
          -------------------------
          | Log lido com sucesso! |
          -------------------------
          '''
except:
    print 'Digite o caminho do arquivo corretamente!!'


while x != 0:
    print '1 - Filtrar pacotes'
    print '2 - Regra porta alta'
    print '3 - Estatistica de protocolos usados'
    print '0 - Sair'

    x = int(raw_input('Digite a opção desejada: '))

    if x == 1:
        filtros = raw_input('Filtro(separe por espaço):')
        if pacotes and filtros:
            pacotes_filtrados = apply_filters(pacotes, filtros)
            macro_sucesso_acao(pacotes_filtrados)
   
    elif x == 2:
        pacotes_filtrados = create_list_pacotes_com_portas_altas(pacotes)
        macro_sucesso_acao(pacotes_filtrados)

    elif x == 3:
        protocolo = raw_input('Protocolo:')
        resultado = create_estatistica_protocolos_acessados(pacotes, protocolo)
        generate_report_statistcs(resultado, protocolo)

    elif x == 0:
        print 'Finalizando...'

    else:
        print 'Digite uma opção valida!'
