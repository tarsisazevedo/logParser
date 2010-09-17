import re

def parse_mac_from_log(line_to_parse):
    try:
        return re.search('[\w{2}:]{41}', line_to_parse).group()
    except:
        return ''

def parse_interface_from_log(line_to_parse):
    try:
        return re.search("[e-t]{3}\d", line_to_parse).group()
    except:
        return ''

def parse_dia_e_mes_from_log(line_to_parse):
    try:
        dia = re.search('\d{2}', line_to_parse).group()
        mes = re.search('\w{3}', line_to_parse).group()
        dia_e_mes = mes+' '+dia
        return dia_e_mes
    except:
        return ''

def parse_hora_from_log(line_to_parse):
    try:
        return re.search('[\w{2}:]{8}', line_to_parse).group()
    except:
        return ''

def parse_src_from_log(line_to_parse):
    try:
        return re.search("(?<=SRC=)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line_to_parse).group()
    except:
        return ''

def parse_dst_from_log(line_to_parse):
    try:
        return re.search('(?<=DST=)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line_to_parse).group() 
    except:
        return ''

def parse_out_from_log(line_to_parse):
    try:
        return re.search('(?<=OUT=)', line_to_parse).group()
    except:
        return ''

def parse_len_from_log(line_to_parse):
    try:
        return re.search('(?<=LEN=)\d{2}', line_to_parse).group()
    except:
        return ''

def parse_prec_from_log(line_to_parse):
    try:
        return re.search('(?<=PREC=)\d{1}\w{1}\d{2}', line_to_parse).group()
    except:
        return ''

def parse_tos_from_log(line_to_parse):
    try:
        return re.search('(?<=TOS=)\d{1}\w{1}\d{2}', line_to_parse).group()
    except:
        return ''

def parse_ttl_from_log(line_to_parse):
    try:
        return re.search('(?<=TTL=)\d{2,3}', line_to_parse).group()
    except:
        return ''

def parse_id_from_log(line_to_parse):
    try:
        return re.search('(?<=ID=)\d{0,9}', line_to_parse).group()
    except:
        return ''

def parse_proto_from_log(line_to_parse):
    try:
        return re.search('(?<=PROTO=)\w{3,5}', line_to_parse).group()
    except:
        return ''

def parse_spt_from_log(line_to_parse):
    try:
        return re.search('(?<=SPT=)\d{0,9}', line_to_parse).group()
    except:
        return ''

def parse_dpt_from_log(line_to_parse):
    try:
        return re.search('(?<=DPT=)\d{0,9}', line_to_parse).group()
    except:
        return ''

from package import Pacote

def parser_log_to_objects(log):
  
    lista_de_pacotes = []
    for line_to_parse in log.readlines():
        mac = parse_mac_from_log(line_to_parse)
        interface = parse_interface_from_log(line_to_parse)
        dia_e_mes = parse_dia_e_mes_from_log(line_to_parse)
        hora = parse_hora_from_log(line_to_parse)
        src = parse_src_from_log(line_to_parse)
        dst = parse_dst_from_log(line_to_parse)
        out = parse_out_from_log(line_to_parse)
        len = parse_len_from_log(line_to_parse)
        prec = parse_prec_from_log(line_to_parse)
        tos = parse_tos_from_log(line_to_parse)
        ttl = parse_ttl_from_log(line_to_parse)
        id = parse_id_from_log(line_to_parse)
        proto = parse_proto_from_log(line_to_parse) 
        spt = parse_spt_from_log(line_to_parse)
        dpt = parse_dpt_from_log(line_to_parse)

        pacote = Pacote(interface, mac, dia_e_mes, hora, src, dst, out, len, prec, tos, ttl, id, proto, spt, dpt)
        lista_de_pacotes.append(pacote)
    
    log.close()
    return lista_de_pacotes

