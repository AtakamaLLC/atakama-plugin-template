""" Atakama plugin: Simple Detector """

import logging
from atakama import DetectorPlugin


log = logging.getLogger(__name__)


class SimpleDetector(DetectorPlugin):
    """Atakama plugin: Simple Detector"""

    @staticmethod
    def name():
        return "simple-detector"

    def needs_encryption(self, full_path: str) -> bool:
        return "simple" in full_path
