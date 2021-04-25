import unittest
import os

path = "dummy.exe"  # path to the binary to be tested


class statuscodetest(unittest.TestCase):
    def tearDown(self):
        os.system(" hostsman -r www.google.com")

    def updatehostfile(self, ip):
        os.system(" hostsman -i www.google.com:%s" % ip)

    def test_200ok(self):
        out = os.system(path)
        self.assertEqual(out, "It works!!!", "Incorrect message on ststus code 200")

    def test_errorcode409(self):
        self.updatehostfile("1.1.1.1")
        out = os.system("path")
        self.assertEqual(out, "409", "Incorrect error code!")

    def test_errorcode301(self):
        self.updatehostfile("99999.99.99.0")
        out = os.system("path")
        self.assertEqual(out, "301", "Incorrect error code!")


if __name__ == '__main__':
    print("Please enter path to the binary file to be tested:")
    path = input()
    unittest.main()
