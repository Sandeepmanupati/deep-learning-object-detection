import cv2
import time


class FPSCounter:
    def __init__(self):
        self.prev_time = time.time()

    def update(self):
        current_time = time.time()
        fps = 1.0 / (current_time - self.prev_time + 1e-6)
        self.prev_time = current_time
        return int(fps)


def draw_detections(frame, detections, fps=None):
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        label = det["label"]
        conf = det["conf"]
        obj_id = det.get("id", None)

        text = f"{label} {conf:.2f}"
        if obj_id is not None:
            text = f"ID {obj_id} | {text}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            text,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    if fps is not None:
        cv2.putText(
            frame,
            f"FPS: {fps}",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    return frame