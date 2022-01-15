import cv2
import os


def main() -> None:
    folder: str = "test"
    frames: list[str] = [file for file in os.listdir(folder) if file.find(".jpg") > 0]
    video_name: str = "test.avi"
    output_folder: str = "output"
    if not os.path.isdir(os.path.join(folder, output_folder)):
        os.makedirs(os.path.join(folder, output_folder))

    height, width, _ = cv2.imread(os.path.join(folder, frames[0])).shape
    fps: int = 30

    video = cv2.VideoWriter(os.path.join(folder, output_folder, video_name), 0, fps, (width, height))
    for frame in frames:
        if frame.find(".jpg"):
            video.write(cv2.imread(os.path.join(folder, frame)))
    cv2.destroyAllWindows()
    video.release()


if __name__ == "__main__":
    main()
