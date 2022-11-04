import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.negative_varasto = Varasto(-5, -5)
        self.saldo_varasto = Varasto(100,120)

    def test_str_funktio(self):
        self.assertAlmostEqual(self.saldo_varasto.__str__(),"saldo = 100, vielä tilaa 0")

    def test_lisaa_neg(self):
        self.assertIsNone(self.varasto.lisaa_varastoon(-5), None)
    
    def test_ota_neg(self):
        apu = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(apu, 0.0)
    
    def test_ota_yli_saldon(self):
        self.assertAlmostEqual(self.saldo_varasto.ota_varastosta(130), 100)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_neg_varasto_tilavuus_build(self):
        self.assertAlmostEqual(self.negative_varasto.tilavuus, 0)
    
    def test_neg_varasto_saldo_build(self):
        self.assertAlmostEqual(self.negative_varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_maxsaldo_maxtilavuus(self):
        self.assertAlmostEqual(self.saldo_varasto.saldo, 100)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(11)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_ottaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 10)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
