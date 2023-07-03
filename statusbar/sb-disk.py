#!/usr/bin/env python
import shutil

def main():
    # found on https://stackoverflow.com/a/39799743
    disk = shutil.disk_usage("C:/")

    # modified form https://stackoverflow.com/a/31631711
    def bytestoGB(B):
        B = float(B)
        KB = float(1024)
        GB = float(KB ** 3) # 1,073,741,824

        return '{0:.0f}GB'.format(B / GB)

    taken = bytestoGB(disk.used)
    space = bytestoGB(disk.total)

    print(f"{taken} / {space}")

if __name__ == "__main__":
    main()
