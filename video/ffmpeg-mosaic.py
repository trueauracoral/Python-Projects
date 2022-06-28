#!/usr/bin/env python
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Fffmpeg wrapper script.')
#parser.add_argument('-a', '--audio', action="store_true", default=False, help='Record just audio')
parser.add_argument('-n', '--number', type=int, metavar='NUMBER', help='Number of times the video will be in the mosaic')
parser.add_argument('-f', '--file', type=str, metavar='FILE', help='Video for the mosaic')
parser.add_argument('-o', '--output', type=str, metavar='FILE', help='Output location')
args = parser.parse_args()

if not os.path.isfile(str(args.file)):
    print(f"{sys.argv[0]}: error: argument -f/--find: Can not find this file")

file_args = "-i "+((args.file+" -i ")*args.number)[:-4]
print(file_args)
os.system(f'ffmpeg {file_args} -filter_complex "[0:v]scale=320:180[v0];[1:v]scale=320:180[v1];[2:v]scale=320:180[v2];[3:v]scale=320:180[v3];[4:v]scale=320:180[v4];[5:v]scale=320:180[v5];[6:v]scale=320:180[v6];[7:v]scale=320:180[v7];[8:v]scale=320:180[v8];[v0][v1][v2]hstack=3[Row0];[v3][v4][v5]hstack=3[Row1];[v6][v7][v8]hstack=3[Row2];[Row0][Row1][Row2]vstack=3[v]" -map "[v]" -shortest {args.output}')
print(f'ffmpeg {file_args} -filter_complex "[0:v]scale=320:180[v0];[1:v]scale=320:180[v1];[2:v]scale=320:180[v2];[3:v]scale=320:180[v3];[4:v]scale=320:180[v4];[5:v]scale=320:180[v5];[6:v]scale=320:180[v6];[7:v]scale=320:180[v7];[8:v]scale=320:180[v8];[v0][v1][v2]hstack=3[Row0];[v3][v4][v5]hstack=3[Row1];[v6][v7][v8]hstack=3[Row2];[Row0][Row1][Row2]vstack=3[v]" -map "[v]" -shortest {args.output}')
