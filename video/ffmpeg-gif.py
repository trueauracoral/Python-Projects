#!/usr/bin/env python
import sys
import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='ffmpeg gif making script.')
    parser.add_argument('-s', '--start', type=str, metavar='00:00:00', help='Start time of the clip')
    parser.add_argument('-e', '--end', type=str, metavar='00:00:05', help='End time of the clip')
    parser.add_argument('-i', '--input', type=str, metavar='FILE', help='Input file')
    parser.add_argument('-o', '--output', type=str, metavar='FILE', help='Output file')
    parser.add_argument('-t', '--text', type=str, metavar='TEXT', help='Output file')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if not os.path.isfile(args.output):
        print("File not found!")
        sys.exit(1)

    print("---------------")
    os.system(f'ffmpeg -ss {args.start} -t {args.end} -i "{args.input}" -filter_complex "[0:v] palettegen" palette.png')

    print("---------------")
    os.system(f'ffmpeg -ss {args.start} -t {args.end} -i "{args.input}" -i palette.png -filter_complex "[0:v] fps=10,scale=720:-1 [new];[new][1:v] paletteuse" ffmpeg-meme-gif-file.gif')

    print("---------------")
    if not args.text == "":
        os.system(f'ffmpeg -i ffmpeg-meme-gif-file.gif -vf "drawtext=fontsize=45:fontcolor=#ffffff:bordercolor=black:borderw=2:x=(w-text_w)/2:y=(h-text_h)/2:text=\'{args.text}\'" -codec:a copy {args.output}')

    os.remove("palette.png")
    os.remove("ffmpeg-meme-gif-file.gif")

if __name__ == "__main__":
    main()
