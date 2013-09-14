#! python
#! encoding=utf8

import unittest

from normalOrg import normalize


class TestNormalize(unittest.TestCase):

    def setUp(self):
        print "Setting up test"

    def test_replace(self):
        self.assertEqual("macys and co", normalize(u"macy's & company"))
        self.assertEqual("williams sanoma sba", normalize(u"williams sanoma s.b.a."))
        self.assertEqual("ck life sciences international", normalize(u"ck life sciences int'l"))
        self.assertEqual("queens moat houses uk ltd", normalize(u"queens moat houses uk limited"))

    def test_multipeToken(self):
        self.assertEqual("flughafen hamburg gmbh", normalize(u"flughafen hamburg gesellschaft mit beschrankter haftung"))

    def test_unicode(self):
        self.assertEqual("sana kliniken duesseldorf", normalize(u"Sana Kliniken Düsseldorf"))
        self.assertEqual("association liegeoise du gaz", normalize(u"Association Liégeoise du Gaz"))
        self.assertEqual("societe anonyme dinformations et de productions multimedia", normalize(u"Société, Anonyme d'Informations et de Productions Multimédia"))
        self.assertEqual("celg distribuicao", normalize(u"Celg Distribuição"))
        self.assertEqual("instituto geral de assistencia social evangelica igase", normalize(u"Instituto Geral de Assistência Social Evangélica-IGASE"))
        self.assertEqual("uniao brasileira de educacao e assistencia", normalize(u"União Brasileira de Educação e Assistência"))
        self.assertEqual("oulun b&n yhtioet", normalize(u"Oulun B&N Yhtiöt"))
        self.assertEqual("jaervisuomen portti", normalize(u"Järvisuomen Portti"))

if __name__ == '__main__':
    unittest.main()
