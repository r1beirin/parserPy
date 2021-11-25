#!/usr/bin/python3
import argparse, pereader

arg = argparse.ArgumentParser()
arg.add_argument("-f", dest="path", help="Complete path to archive")
args = arg.parse_args()

pe = pereader.PE(args.path)

def save_file():
  with open ("parser.txt", "w") as f:
    print(pe, file=f)

save_file()
