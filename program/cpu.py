import psutil

def freq():
    if psutil.cpu_freq() == None:
        return psutil.cpu_freq()
    else:
        return psutil.cpu_freq().current

def cores():
    return psutil.cpu_count()

def phy_cores():
    return psutil.cpu_count(logical=False)

def percentage():
    return psutil.cpu_times_percent(interval=1)

