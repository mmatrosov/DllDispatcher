import sys
import subprocess
import struct

win32_app = 'c:/Program Files (x86)/depends22_x86/depends.exe'
win64_app = 'c:/Program Files/depends22_x64/depends.exe'

IMAGE_FILE_MACHINE_I386 = 332
IMAGE_FILE_MACHINE_IA64 = 512
IMAGE_FILE_MACHINE_AMD64 = 34404


# Source: http://stackoverflow.com/a/1345697/261217
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


file_path = sys.argv[1]
app = win64_app if is_64bit_pe(file_path) else win32_app

print("Starting {}...".format(app))
args = [app, file_path]
subprocess.Popen(args)
