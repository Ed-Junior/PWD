import os
from . import computer

def shutdown():
    if computer.so() == "Windows":
        os.system("shutdown -s")

    elif computer.so() == "Linux":
        os.system("shutdown -h")
    else:
        print("Sistema operacional não detectado, imposivel executar a operaçãpp")


def reboot():
    if computer.so() == "Windows":
        os.system("shutdown -r")

    elif computer.so() == "Linux":
        os.system("shutdown -r")
    else:
        print("Sistema operacional não detectado, imposivel executar a operaçãpp")