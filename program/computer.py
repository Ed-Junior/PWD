import platform


def so():
    return platform.uname().system


def osVersion():
    return platform.uname().version


def name():
    return platform.uname().node


def arc():
    return platform.uname().machine


def cpu():
    return platform.uname().processor


def distro():
    if os() == "Linux":
        return platform.dist()
    else:
        return os()
