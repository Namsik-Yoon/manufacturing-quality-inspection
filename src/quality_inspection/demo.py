"""Original procedural fixtures, unrelated to downloaded benchmark images."""

import io

import numpy as np
from PIL import Image

from quality_inspection.baseline import TemplateBaseline


def synthetic_image(seed: int, defective: bool = False) -> bytes:
    rng = np.random.default_rng(seed)
    pixels = np.full((64, 64), 225.0)
    pixels[12:56, 20:44] = 110.0
    pixels[7:12, 27:37] = 95.0
    pixels += rng.normal(0, 1.5, pixels.shape)
    if defective:
        pixels[29:41, 23:41] = 20.0
    image = Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def demo_model() -> TemplateBaseline:
    return TemplateBaseline.fit(
        [synthetic_image(i) for i in range(30)],
        [synthetic_image(i) for i in range(100, 120)],
        source="synthetic-demo",
    )


def demo_results() -> dict:
    model = demo_model()
    return {
        "evidence": "synthetic smoke only; not real defect performance",
        "runtime_llm_tokens": 0,
        "results": [
            {
                "sample": name,
                "decision": result.decision,
                "score": result.score,
                "threshold": result.threshold,
            }
            for name, result in (
                ("healthy", model.inspect(synthetic_image(900))),
                ("defect", model.inspect(synthetic_image(901, defective=True))),
            )
        ],
    }
