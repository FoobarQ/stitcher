import cv2
import os
import sys
import datetime
from pick import pick


def create_vid(name, out_dir, frames):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    height, width, _ = cv2.imread(frames[0]).shape
    fps: int = 15

    video = cv2.VideoWriter(os.path.join(out_dir, name), 0, fps, (width, height))
    for frame in frames:
        video.write(cv2.imread(frame))
    cv2.destroyAllWindows()
    video.release()
    print("video: " + name + " created.")


def main() -> None:
    folder: str = input("folder name?\n")
    frames: list[str] = [os.path.join(folder, file) for file in os.listdir(folder) if file.find(".jpg") > 0]
    interval: int = int(input("photo interval?\n")) + 1
    frame_lists = {}
    video_name = input("video name?\n") + ".avi"
    output_folder: str = "output"
    previous_time = os.stat(frames[0]).st_ctime
    video_key = str(datetime.datetime.fromtimestamp(previous_time))
    frame_lists[video_key] = []

    for i in range(len(frames)):
        current_time = os.stat(frames[i]).st_ctime

        if current_time - previous_time > interval:
            video_key = str(datetime.datetime.fromtimestamp(current_time))
            frame_lists[video_key] = []

        frame_lists[video_key].append(frames[i])
        previous_time = current_time
    title = "--------------------------------------------------------------\nstart\t\t\t\tduration\t\tframes\n--------------------------------------------------------------\n"
    options = []
    for key in frame_lists.keys():
        if len(frame_lists[key]) - 1:
            options.append(
                key
                + "\t"
                + str(
                    datetime.datetime.fromtimestamp(os.stat(frame_lists[key][-1]).st_ctime)
                    - datetime.datetime.fromtimestamp(os.stat(frame_lists[key][0]).st_ctime)
                )
                + "\t\t"
                + str(len(frame_lists[key]))
            )
    chosen_list = frame_lists[pick(options, title)[0].split("\t")[0]]
    create_vid(video_name, os.path.join(folder, output_folder), chosen_list)


if __name__ == "__main__":
    main()
