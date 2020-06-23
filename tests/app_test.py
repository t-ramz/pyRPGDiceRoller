import sys
sys.path.append('../')

from pyRPGDiceRoller.application import diceRoller


def test_d100(capsys):
    diceRoller.d100()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 101))
    assert capture.out in myTestList


def test_d20(capsys):
    diceRoller.d20()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 21))
    assert capture.out in myTestList


def test_d12(capsys):
    diceRoller.d12()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 13))
    assert capture.out in myTestList


def test_d10(capsys):
    diceRoller.d10()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 11))
    assert capture.out in myTestList


def test_d8(capsys):
    diceRoller.d8()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 9))
    assert capture.out in myTestList


def test_d6(capsys):
    diceRoller.d6()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 7))
    assert capture.out in myTestList


def test_d4(capsys):
    diceRoller.d4()
    capture = capsys.readouterr()
    myTestList = (str(s) + "\n" for s in range(1, 5))
    assert capture.out in myTestList
