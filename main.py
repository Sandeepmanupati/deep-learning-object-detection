import cv2
from video_source import VideoSource
from detector import ObjectDetector
from tracker import SimpleTracker
from utils import draw_detections, FPSCounter


def main():
    source = 0  # webcam
    video = VideoSource(source).start()
    detector = ObjectDetector(model_path="yolov8n.pt", conf=0.4)
    tracker = SimpleTracker()
    fps_counter = FPSCounter()

    print("Press 'q' to quit.")

    while True:
        frame = video.read()

        detections = detector.detect(frame)
        tracked_objects = tracker.update(detections)

        fps = fps_counter.update()
        output_frame = draw_detections(frame, tracked_objects, fps=fps)

        cv2.imshow("Live Object Detection", output_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.stop()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()