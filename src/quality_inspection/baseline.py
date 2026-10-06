"""Small aligned-image baseline, deliberately transparent and CPU-only."""

import io
import warnings
from dataclasses import dataclass

import numpy as np
from PIL import Image, ImageOps, UnidentifiedImageError

MAX_IMAGE_BYTES = 5 * 1024 * 1024
MAX_PIXELS = 16_000_000
IMAGE_SIZE = (64, 64)


def preprocess(raw: bytes) -> np.ndarray:
    """Decode PNG/JPEG, orient, resize and normalize grayscale to [0, 1]."""
    if not raw or len(raw) > MAX_IMAGE_BYTES:
        raise ValueError("Image must contain 1 byte to 5 MiB")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(io.BytesIO(raw)) as image:
                if image.format not in {"PNG", "JPEG"}:
                    raise ValueError("Only PNG and JPEG are supported")
                if image.width * image.height > MAX_PIXELS:
                    raise ValueError("Image exceeds 16 million pixels")
                image = ImageOps.exif_transpose(image).convert("L")
                return (
                    np.asarray(
                        image.resize(IMAGE_SIZE, Image.Resampling.BILINEAR), dtype=np.float32
                    )
                    / 255.0
                )
    except (
        UnidentifiedImageError,
        OSError,
        Image.DecompressionBombError,
        Image.DecompressionBombWarning,
    ) as exc:
        raise ValueError("Invalid or oversized image") from exc


@dataclass(frozen=True)
class Inspection:
    score: float
    threshold: float
    decision: str
    model_source: str


@dataclass(frozen=True)
class TemplateBaseline:
    template: np.ndarray
    threshold: float
    source: str

    @classmethod
    def fit(
        cls, training: list[bytes], calibration: list[bytes], source: str
    ) -> "TemplateBaseline":
        if len(training) < 2 or len(calibration) < 2:
            raise ValueError(
                "At least two independent training and calibration images are required"
            )
        template = np.mean(np.stack([preprocess(x) for x in training]), axis=0)
        scores = [float(np.mean(np.abs(preprocess(x) - template))) for x in calibration]
        threshold = max(float(np.quantile(scores, 0.95)), 1e-6)
        return cls(template=template, threshold=threshold, source=source)

    def inspect(self, raw: bytes) -> Inspection:
        score = float(np.mean(np.abs(preprocess(raw) - self.template)))
        return Inspection(
            score=score,
            threshold=self.threshold,
            decision="review" if score > self.threshold else "candidate-pass",
            model_source=self.source,
        )
