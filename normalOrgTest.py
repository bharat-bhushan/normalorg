import unittest

from normalOrg import normalize


class TestNormalize(unittest.TestCase):

    def setUp(self):
        print "Setting up test"

    def test_replace(self):
        self.assertEqual("macys and co", normalize("macy's & company"))

        self.assertEqual("williams sanoma sba", normalize("williams sanoma s.b.a."))

        self.assertEqual("ck life sciences intl", normalize("ck life sciences int'l"))
        
        self.assertEqual("flughafen hamburg gmbh", normalize("flughafen hamburg gesellschaft mit beschrankter haftung"))


if __name__ == '__main__':
    unittest.main()
