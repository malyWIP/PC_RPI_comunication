#!/usr/bin/python
import sys, os, time, shutil
x1=0
path = r'C:\maxymos123\\'
moveto = r'\\192.168.21.50\homepi\csv_memory\\'

class DataMove:

    state = True

    def __init__(self, state):
        self.state = state


    def move_to_directory(self, path, moveto):
        files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=False)
        k = 0
        try:
            while self.state !=False and files.__len__() != k:
                x = files[k]
                b = x.split('\\')
                src = path + b[3]
                dst = moveto + b[3]
                shutil.move(src, dst)
                k += 1
                time.sleep(0.8)

        except FileNotFoundError:
            print('blad')



    def setState(self, newstate):
        self.state = newstate

def File_Change1():
    global x1
    folder =r'C:\maxymos123\\'
    try:
        x1 = len([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')])
        return x1
    except FileNotFoundError:
        print('nie znaleziono pliku')
        return x1



if __name__ == '__main__':
    # Listener
    process_tester = DataMove(True)
    while True:
        z = File_Change1()
        try:
            if z>0:
                time.sleep(0.1)
                process_tester.setState(True)
                process_tester.move_to_directory(path,moveto)
                z =0
                process_tester.setState(False)
        except PermissionError:
            print('bład odczytu')
        except TypeError:
            print('bład odczytu')
