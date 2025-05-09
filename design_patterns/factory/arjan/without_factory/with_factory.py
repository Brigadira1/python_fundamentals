""" This class shows the Abastract Factory pattern. It is a refactored version of the
antipattern class called without_factory.py.
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


class AbstractExporterFactory(ABC):
    """This is the Abstract factory. Its purpose is to have two methods that return concrete factories for
    audio and vidio exporter objects."""

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass


class FastExporter(AbstractExporterFactory):
    """A factory aimed at providing a high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self):
        return AACAudioExporter()


class HighQualityExporter(AbstractExporterFactory):
    """A factory ained at providing a high speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(AbstractExporterFactory):
    """A factory aimed at providing a low speed, super quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> AbstractExporterFactory:

    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }

    # read the desired export quality
    while True:
        export_quality = input("Enter the desired export quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}")


def main(fac: AbstractExporterFactory) -> None:
    """Main function"""

    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    folder = Path("/usr/tmp/video")

    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    fac = read_exporter()
    main(fac)
