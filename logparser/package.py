"""
>>> from parsers import parser_log_to_objects
>>> log = open("log/pequenaParteDoLog", 'r')
>>> parser_log = parser_log_to_objects(log)
>>> type(parser_log)
<type 'list'>
>>> len(parser_log)
33
>>> pacote = parser_log[0]
>>> pacote
Pacote
>>> pacote.interface
'eth0'
>>> pacote.mac
'00:13:d4:ef:a3:80:00:00:a2:0d:20:a9:08:00'
>>> pacote.dia_e_mes
'Apr 25'
>>> pacote.hora
'06:25:23'
>>> pacote.src
'193.171.119.77'
>>> pacote.dst
'200.167.212.131'
>>> pacote.len
'60'
>>> pacote.prec
'0x00'
>>> pacote.tos
'0x00'
>>> pacote.ttl
'41'
>>> pacote.id
'31266'
>>> pacote.proto
'TCP'
>>> pacote.spt
'46039'
>>> pacote.dpt
'25'
"""

class Pacote(object):
    def __init__(self, interface=None, mac=None, dia_e_mes=None, hora=None,\
                 src=None, dst=None, out=None, len=None, prec=None, tos=None,\
                 ttl=None, id=None, proto=None, spt=None, dpt=None):
        self.interface = interface
        self.mac = mac
        self.dia_e_mes = dia_e_mes
        self.hora = hora
        self.src = src
        self.dst = dst
        self.out = out
        self.len = len
        self.prec = prec
        self.tos = tos
        self.ttl = ttl
        self.id = id
        self.proto = proto
        self.spt = spt
        self.dpt = dpt

    def esta_acessando_portas_altas(self):
        """
        >>> pacote = Pacote(dpt=1025)
        >>> pacote.esta_acessando_portas_altas()
        True
        >>> pacote2 = Pacote(dpt=1024)
        >>> pacote2.esta_acessando_portas_altas()
        False
        """
        if self.dpt != '' and int(self.dpt) > 1024:
            return True
        else:
            return False

    def __repr__(self):
        return "Pacote"


if __name__=='__main__':
    import doctest
    doctest.testmod()
