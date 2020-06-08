import sys
sys.path.append('../')

from pyRPGDiceRoller import diceRoller


def test_d10(capsys):
    diceRoller.d10()
    capture = capsys.readouterr()
    assert capture.out == "8\n"
