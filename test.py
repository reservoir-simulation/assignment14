#/usr/bin/env python

import unittest
import os


def cleanup(line):

    return line.strip().strip('\n').split()


class TestSolution(unittest.TestCase):


    def test_cmg_output(self):

        with open('assignment14.out') as f:

            raw_content = f.readlines()


        for line in raw_content:
            clean_line = cleanup(line) 

            if clean_line != []:
                if clean_line[0] == 'Current' and clean_line[1] == 'Fluids':
                    assert abs(float(clean_line[6]) - float(71256)) < 5


if __name__ == '__main__':
    unittest.main()









