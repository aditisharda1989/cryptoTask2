import unittest
import os

path = "dummy.exe"  # path to the binary to be tested


class statuscodetest(unittest.TestCase):
    def tearDown(self):
        """clear modifications on hostfile"""
        os.system(" hostsman -r www.google.com")

    def updatehostfile(self, ip):
        """append an ip address for www.google.com to host file"""
        os.system(" hostsman -i www.google.com:%s" % ip)

    def test_200ok(self):
        """check the binary output when url returns 200ok"""
        out = os.system(path)
        self.assertEqual(out, "It works!!!", "Incorrect message on ststus code 200")

    def test_errorcode409(self):
        """check the binary output when url error code 409"""
        self.updatehostfile("1.1.1.1")
        out = os.system("path")
        self.assertEqual(out, "409", "Incorrect error code!")

    def test_errorcode301(self):
        """check the binary output when url error code 301"""
        self.updatehostfile("99999.99.99.0")
        out = os.system("path")
        self.assertEqual(out, "301", "Incorrect error code!")


if __name__ == '__main__':
    print("Please enter path to the binary file to be tested:")
    path = input()
    unittest.main()
