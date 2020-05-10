import sys

info = 'OS info is \n{}\n\nPython version is {}'.format(
    sys.platform, sys.version)
print(info)

with open('os_info', 'w') as ff:
    ff.write(info)