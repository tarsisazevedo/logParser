import unittest
from logparser.utils import generate_report, \
     create_list_pacotes_com_portas_altas, create_estatistica_protocolos_acessados
from logparser.package import Pacote
from logparser.parsers import parser_log_to_objects

class TestUtils(unittest.TestCase):
    def setUp(self):
        log = open('log/log_test_utils', 'r')
        self.lista_de_pacotes = parser_log_to_objects(log)

    def test_lista_de_pacotes_acessando_portas_altas(self):
        log = open('log/teste_acesso_a_portas_altas', 'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        lista = create_list_pacotes_com_portas_altas(pacotes)
        self.assertEquals(len(lista), 2)

    def test_estatisticas_de_protocolos_acessados(self):
        log = open('log/estatistica_de_protocolo', 'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        estatistica = create_estatistica_protocolos_acessados(pacotes, 'TCP')
        self.assertEquals(estatistica, 30)

    def test_estatistica_de_acesso_por_UDP(self):
        log = open('log/estatistica_de_protocolo', 'r')
        pacotes = parser_log_to_objects(log)
        log.close()
        estatistica = create_estatistica_protocolos_acessados(pacotes, 'udp')
        self.assertEquals(estatistica, 70)

    def test_estatistica_igual_0(self):
        log = open('log/estatistica_de_protocolo','r')
        pacotes = parser_log_to_objects(log)
        log.close()
        estatistica = create_estatistica_protocolos_acessados(pacotes, 'nada')
        self.assertEquals(estatistica, 0)
        
unittest.main()
