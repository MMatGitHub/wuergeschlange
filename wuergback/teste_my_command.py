import protokolliere
from run_my_command import run_cmd

def teste_hallo_welt():
    output = run_cmd("echo Hello, World!")
    if output is not None:
        return("Output: ", str(output))
    else:
        protokolliere.err("e: Kein Output in teste_hallo_welt()")

def test_ping_inet():
    output = run_cmd("ping -n 2 8.8.8.8")
    if output is not None:
        return("Output: ", output)
    else:
        protokolliere.err("e: Kein Output in test_ping_inet()")


def test_dir_temp():
    output = run_cmd("dir C:\\Temp")
    if output is not None:
        return("Output: ", str(output))
    else:
        protokolliere.err("e: Kein Output in test_dir_temp()")