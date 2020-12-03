import sys
import cv2
import random
import os
import pathlib

def framenumGetter(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap.get(cv2.CAP_PROP_FRAME_COUNT)


def save_frame(video_path, frame_num):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('video capture can not open')
        sys.exit(1)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    return cap.read()


def randomFramePickup(frame_total_num):
    frame_num = random.choice(range(0, int(frame_total_num)))

    return frame_num


def randomPicker(video_path):
    save_path = "./pickedImages"

    frame_total_num = framenumGetter(video_path)

    frame_num = randomFramePickup(frame_total_num)

    ret, pickedFrame = save_frame(video_path, frame_num)
    p_video_path = pathlib.Path(video_path)

    video_file_name = p_video_path.name

    frame_save_path = save_path + '/' + video_file_name[:-4] + '_' + str(frame_num) + '.jpg'
    print(frame_save_path)
    if ret:
        if not os.path.isfile(frame_save_path):
            # ダブらなければ保存
            cv2.imwrite(frame_save_path, pickedFrame)
            return pickedFrame, frame_save_path
            print('save complete')
        else:
            # ダブったら再度関数を呼び出し
            print('file doubling')
            randomPicker(video_path)
    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("引数が足りません")
        sys.exit(1)

    video_path = sys.argv[1]
    randomPicker(video_path)
