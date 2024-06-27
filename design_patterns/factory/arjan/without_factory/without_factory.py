""" This class shows several anti-patterns.
The ideas is to then refactor it to use the Factory design pattern in another package.
This coding is directly taken from a video from ArjanCodes: https://www.youtube.com/watch?v=s_4ZrtQs8Do&t=3s
"""

from pathlib import Path
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic represenation of video exporting codec"""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting"""

    @abstractmethod
    def do_export(self, path: Path):
        """Exports the video data to a folder"""


class AudioExporter(ABC):
    """Basic represenation of audio exporting codec"""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for export"""

    @abstractmethod
    def do_export(self, path: Path):
        """Exports audio data to a folder"""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec"""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, path: Path):
        print(f"Exporting video data in lossless format to {path}")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, path: Path):
        print(f"Exporting video data in H.264 (Baseline) format to {path}")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, path: Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {path}")


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, path: Path):
        print(f"Exporting audio data in AAC format to {path}")


class WAVAudioExporter(AudioExporter):
    """WAV audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, path: Path):
        print(f"Exporting audio data in WAV format to {path}")


def main() -> None:
    """Main function"""

    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input("Enter the desired export quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unknown output quality option: {export_quality}")

    # create video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        # defaults to best possible video and audio exporters
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    folder = Path("/usr/tmp/video")

    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
