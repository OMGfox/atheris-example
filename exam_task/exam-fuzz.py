import atheris
import sys


def GetAccess(age, leng, mydate, token):
    if age == 478214 and leng == -7 and mydate == '20':
        raise RuntimeError("backdoor finded!")
        return True
    elif token == 'djcu3ld8fjsnxkfjdheb':
        return True
    else:
        return False

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    age = fdp.ConsumeInt(4)
    leng = fdp.ConsumeInt(1)
    mydate = fdp.ConsumeUnicode(2)
    token = fdp.ConsumeUnicode(20)

    GetAccess(age, leng, mydate, token)


if __name__ == "__main__":
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
