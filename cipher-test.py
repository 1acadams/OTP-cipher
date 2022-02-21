from cipher import *

def test_generatePad_length():
    assert len(generatePad(15)) == 15

def test_encipher_abc():
    assert encipher('hello', 'ABCDE') == 'hfnos'

def test_encipher_xyz():
    assert encipher('WORLD', 'VWXYZ') == 'RKOJC'

def test_decipher_abc():
    assert decipher('sbnxx', 'ABCDE') == 'salut'

def test_decipher_xyc():
    assert decipher('HKKBD', 'VWXYZ') == 'MONDE'