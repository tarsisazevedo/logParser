#encoding: utf-8

import HTML
import webbrowser

def generate_report(dados):
    tableHTML = HTML.Table(header_row=["Pacotes", "IP origem", "IP destino", "Interface", "Protocolo",'MAC', 'Dia e Mes', "Hora", "Tamanho", 'Porta origem', "Porta destino" ])
    if dados:
        for dado in dados:
            tableHTML.rows.append([dado, dado.src, dado.dst, dado.interface, dado.proto, dado.mac, dado.dia_e_mes, dado.hora, dado.len, dado.spt, dado.dpt])
    else:
        tableHTML.rows.append(['NAO FORAM ENCONTRADOS RESULTADOS'])
    reportHTML = open('report/report.html','w')
    reportHTML.write(str(tableHTML))
    reportHTML.close()
    return webbrowser.open('report/report.html')

def generate_report_statistcs(estatistica, protocolo):
    tableHTML = HTML.Table(header_row=['Protocolo', 'Estatistica'])
    tableHTML.rows.append([protocolo, str(estatistica)+"%"])
    reportHTML = open('report/report.html','w')
    reportHTML.write(str(tableHTML))
    reportHTML.close()
    return webbrowser.open('report/report.html')

def create_list_pacotes_com_portas_altas(pacotes):
    lista_de_pacotes = []
    for pacote in pacotes:
        if pacote.esta_acessando_portas_altas():
            lista_de_pacotes.append(pacote)
    generate_report(lista_de_pacotes)
    return lista_de_pacotes

def create_estatistica_protocolos_acessados(pacotes, protocolo):
    estatistica = 0
    for pacote in pacotes:
        if pacote.proto == protocolo.upper():
           estatistica += 1 
    return (estatistica*100)/len(pacotes)
