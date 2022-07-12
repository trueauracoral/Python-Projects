#!/usr/bin/env python
# ffmpeg -ss 00 -i <VID> -t 55 -c copy out.mp4
import os
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='ffmpeg clipper script.')
    parser.add_argument('-s', '--start', type=str, metavar='00:00:00', help='Start time of the clip')
    parser.add_argument('-e', '--end', type=str, metavar='00:00:05', help='End time of the clip')
    parser.add_argument('-i', '--input', type=str, metavar='FILE', help='Input file')
    parser.add_argument('-o', '--output', type=str, metavar='FILE', help='Output file')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if os.path.isfile(args.input):
        os.system(f"ffmpeg -ss {args.start} -i {args.input} -t {args.end} -c copy {args.output}")
if __name__ == "__main__":
    main()
