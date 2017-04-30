import configparser
import os
import sys
import subprocess
import struct
import time
import win32gui
import win32process

IMAGE_FILE_MACHINE_I386 = 332
IMAGE_FILE_MACHINE_IA64 = 512
IMAGE_FILE_MACHINE_AMD64 = 34404


# Source:
# http://stackoverflow.com/a/1345697/261217
def read_pe_machine_type(file_path):
    with open(file_path, "rb") as f:
        s = f.read(2)
        if s.decode() != 'MZ':
            raise OSError("File not recognized as PE.")

        f.seek(60)
        s = f.read(4)
        header_offset = struct.unpack("<L", s)[0]
        f.seek(header_offset + 4)
        s = f.read(2)
        return struct.unpack("<H", s)[0]


def is_64bit_pe(file_path):
    machine = read_pe_machine_type(file_path)

    if machine == IMAGE_FILE_MACHINE_I386:
        return False
    elif machine in [IMAGE_FILE_MACHINE_IA64, IMAGE_FILE_MACHINE_AMD64]:
        return True
    else:
        print("Unknown file architecture. Defaulted to 64-bit application.")

    return True


# Source:
# http://timgolden.me.uk/python/win32_how_do_i/find-the-window-for-my-subprocess.html
def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


config = configparser.ConfigParser()
config.read(os.path.splitext(sys.argv[0])[0] + '.ini')

dll_path = sys.argv[1]
app = config['Common']['Win64App'] if is_64bit_pe(dll_path) else config['Common']['Win32App']

print("Starting {}...".format(app))
args = [app, dll_path]
proc = subprocess.Popen(args)

print("Started process {}, waiting for window to appear...".format(proc.pid))
while not get_hwnds_for_pid(proc.pid):
    time.sleep(float(config['Common']['WindowDetectionPeriodSeconds']))

print("See the window, my job is done!")
