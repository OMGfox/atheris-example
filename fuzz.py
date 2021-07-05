import atheris
import sys

def TestOneInput(data):
    bad_data_test(data)
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeInt(4) 
    bad_int_test(num)


def bad_data_test(data):
    if data == b"bad":
        raise RuntimeError("Bad data!")

def bad_int_test(num: int):
    if num == 13:
        raise RuntimeError("The num is equel 13!")


atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
atheris.Fuzz()

