class SimpleTracker:
    def __init__(self):
        self.next_id = 1

    def update(self, detections):
        tracked = []
        for det in detections:
            det["id"] = self.next_id
            self.next_id += 1
            tracked.append(det)
        return tracked