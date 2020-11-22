import cv2
import sys


def framenumGetter(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap.get(cv2.CAP_PROP_FRAME_COUNT)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("引数がおかしいです。")
        print("python framenumGetter.py [video_path]")
        sys.exit(1)

    video_path = sys.argv[1]
    print(framenumGetter(video_path))

