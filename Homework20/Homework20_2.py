import unittest
import Homework20
import logging

logging.basicConfig(filename='demo_log.log', filemode='w', format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

class TestHomework20(unittest.TestCase):

    def test_write(self):
        file_test = 'demo.txt'
        test_text = ('Valensia\n')
        Homework20.write('Valensia')
        with open('demo.txt', 'r+') as opened_file:
            f = opened_file.readline()
            self.assertEqual(test_text,f)
            logging.warning(f'Test program')

unittest.main()