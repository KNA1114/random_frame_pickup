import cv2
import sys

# python pickupper.py [filename.mp4]


def save_frame(video_path, frame_num):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        sys.exit(1)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    return cap.read()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("引数が足りません。")
        print("python pickupper.py [video_path] [frame_num]")
        sys.exit(1)

    video_path = sys.argv[1]
    frame_num = int(sys.argv[2])
    save_path = "./pickedImages"

    frame = save_frame(video_path, frame_num)
    cv2.imwrite(save_path + video_path[:-4] + ".jpg", frame)
