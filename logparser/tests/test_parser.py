import unittest
from logparser.parsers import *

class TestParset(unittest.TestCase):
    def setUp(self):
        log = open("log/pequenaParteDoLog", 'r')
        self.line_to_parse = log.readline()

    def test_get_mac(self):
        mac = parse_mac_from_log(self.line_to_parse)
        self.assertTrue(mac)
        self.assertEquals(mac, '00:13:d4:ef:a3:80:00:00:a2:0d:20:a9:08:00')

    def test_get_interface(self):
        interface = parse_interface_from_log(self.line_to_parse)
        self.assertTrue(interface)
        self.assertEquals(interface, 'eth0')

    def test_get_dia_e_mes(self):
        dia_e_mes = parse_dia_e_mes_from_log(self.line_to_parse)
        self.assertTrue(dia_e_mes)
        self.assertEquals(dia_e_mes, 'Apr 25')
    
    def test_get_hora(self):
        hora = parse_hora_from_log(self.line_to_parse)
        self.assertTrue(hora)
        self.assertEquals(hora, '06:25:23')

    def test_get_src(self):
        src = parse_src_from_log(self.line_to_parse)
        self.assertTrue(src)
        self.assertEquals(src, '193.171.119.77')

    def test_get_dst(self):
        dst = parse_dst_from_log(self.line_to_parse)
        self.assertTrue(dst)
        self.assertEquals(dst, '200.167.212.131')

    def test_get_out(self):
        out = parse_out_from_log(self.line_to_parse)
        self.assertFalse(out)
        self.assertTrue(out=='')

    def test_get_len(self):
        len = parse_len_from_log(self.line_to_parse)
        self.assertTrue(len)
        self.assertEquals(len, '60')

    def test_get_prec(self):
        prec = parse_prec_from_log(self.line_to_parse)
        self.assertTrue(prec)
        self.assertEquals(prec, '0x00')

    def test_get_tos(self):
        tos = parse_tos_from_log(self.line_to_parse)
        self.assertTrue(tos)
        self.assertEquals(tos, '0x00')

    def test_get_ttl(self):
        ttl = parse_ttl_from_log(self.line_to_parse)
        self.assertTrue(ttl)
        self.assertEquals(ttl, '41')

    def test_get_id(self):
        id = parse_id_from_log(self.line_to_parse)
        self.assertTrue(id)
        self.assertEquals(id, '31266')

    def test_get_proto(self):
        proto = parse_proto_from_log(self.line_to_parse)
        self.assertTrue(proto)
        self.assertEquals(proto, 'TCP')

    def test_get_spt(self):
        spt = parse_spt_from_log(self.line_to_parse)
        self.assertTrue(spt)
        self.assertEquals(spt, '46039')

    def test_get_dpt(self):
        dpt = parse_dpt_from_log(self.line_to_parse)
        self.assertTrue(dpt)
        self.assertEquals(dpt, '25')
unittest.main()
