import os

dir = "C:\SGZ_Pro\Hobbys\Media\pokemon\series\xy\thumbnails"

# *1* line
command = 'mpv --lavfi-complex="[vid1][vid2][vid3][vid4][vid5]hstack=inputs=5[vo]" 1.png --external-file="2.png" --external-file="3.png" --external-file="4.png" --external-file="5.png"'

# *2* line
command = 'mpv --lavfi-complex="[vid1][vid2][vid3]hstack=inputs=3[t1];[vid4][vid5][vid6]hstack=inputs=3[t2];[t1] [t2] vstack [vo]" 1.png --external-file="2.png" --external-file="3.png" --external-file="4.png" --external-file="5.png" --external-file="6.png"
