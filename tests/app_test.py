import sys
sys.path.append('../')

from pyRPGDiceRoller.application import diceRoller


def test_d100(capsys):
    diceRoller.d100()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 100))
    assert capture.out in myTestList


def test_d20(capsys):
    diceRoller.d20()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 20))
    assert capture.out in myTestList


def test_d12(capsys):
    diceRoller.d12()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 12))
    assert capture.out in myTestList


def test_d10(capsys):
    diceRoller.d10()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 10))
    assert capture.out in myTestList


def test_d8(capsys):
    diceRoller.d8()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 8))
    assert capture.out in myTestList


def test_d6(capsys):
    diceRoller.d6()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 6))
    assert capture.out in myTestList


def test_d4(capsys):
    diceRoller.d4()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 4))
    assert capture.out in myTestList
