class Timer:
    def __init__(self, duration_seconds: int) -> None:
        """
        Init timer

        Args:
            duration_seconds: Total duration in seconds.
        """
        self.duration = duration_seconds
        self.remaining = duration_seconds
        self._running = False

    def start(self) -> None:
        self._running = True

    def stop(self) -> None:
        self._running = False

    def tick(self) -> bool:
        if self._running and self.remaining > 0:
            self.remaining -= 1
            return True
        return False

    def is_finished(self) -> bool:
        """
        Check if timer is finished
        """
        return self.remaining <= 0
