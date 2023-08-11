#/usr/bin/python3
import dis

if __name__ == '__main__':
    module = open("hidden_4.pyc", "rb").read()
    ins = dis.get_instructions(module)
    names = set()

    for i in ins:
        if i.opname == "LOAD_NAME" and not i.argval.startswith("__"):
            names.add(i.argval)
    for name in sorted(names):
        print(name)
