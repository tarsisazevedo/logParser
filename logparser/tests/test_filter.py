import unittest

from logparser.parsers import *
from logparser.utils import *
from logparser.filters import *

class TestFilters(unittest.TestCase):
    def test_filtro_com_um_atributo(self):
        log = open('log/teste_filtros', 'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        pacotes_filtrados = apply_filters(pacotes, 'src=100.100.0.1')
        self.assertTrue(pacotes_filtrados)
        for pacote in pacotes_filtrados:
            self.assertEquals(pacote.src, '100.100.0.1')

    def test_filtro_com_2_atributos(self):
        log = open("log/teste_filtros",'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        pacotes_filtrados = apply_filters(pacotes, 'src=100.100.0.1 dst=10.10.0.1')
        self.assertTrue(pacotes_filtrados)
        for pacote in pacotes_filtrados:
            self.assertEquals(pacote.src, '100.100.0.1')
            self.assertEquals(pacote.dst, '10.10.0.1')

    def test_filtro_com_3_atributos(self):
        log = open("log/teste_filtros",'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        pacotes_filtrados = apply_filters(pacotes, 'src=100.100.0.1 dst=10.10.0.1 proto=TCP')
        self.assertTrue(pacotes_filtrados)
        for pacote in pacotes_filtrados:
            self.assertEquals(pacote.src, '100.100.0.1')
            self.assertEquals(pacote.dst, '10.10.0.1')
            self.assertEquals(pacote.proto, 'TCP')

    def test_filtro_4_atributos(self):
        log = open("log/teste_filtros",'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        pacotes_filtrados = apply_filters(pacotes, 'ttl=128 proto=UDP spt=68 id=0')
        self.assertTrue(pacotes_filtrados)
        for pacote in pacotes_filtrados:
            self.assertEquals(pacote.ttl, '128')
            self.assertEquals(pacote.proto, 'UDP')
            self.assertEquals(pacote.spt, '68')
            self.assertEquals(pacote.id, '0')

    def test_filtro_da_mono(self):
        log = open('log/pequenaParteDoLog','r')
        pacotes = parser_log_to_objects(log)
        log.close()
        pacotes_filtrados = apply_filters(pacotes, 'src=10.10.3.170 dst=255.255.255.255 interface=eth1')
        self.assertTrue(pacotes_filtrados)

unittest.main()
