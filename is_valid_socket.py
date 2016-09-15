import re

def is_valid_socket(str_addr):
    #takes care of cases where there are letters, there aren't 3 periods
    #and there isn't 1 colon
    if re.search('[a-zA-Z]+', str_addr):
        return False
    elif len(re.findall('\.', str_addr)) != 3:
        return False
    elif len(re.findall('\:', str_addr)) != 1:
        return False

    #splits into first four then last one
    splitUp = str_addr.split(":")
    last = splitUp[1].split(":")
    firstFour = splitUp[0].split(".")


    #takes care of empty cases
    for item in firstFour:
        if item == "":
            return False
    for item in last:
        if item == "":
            return False

    #checks if first 4 are within limits
    for i in range(0, 4):
        if int(firstFour[i]) in range(0, 256):
            pass
        else:
            return False
    #checks if last is within limits
    if int(last[0]) in range(1, 65536):
        pass
    else:
        return False

    return True
