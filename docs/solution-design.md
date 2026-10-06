# Solution design

The first slice is **Assumed** decision support for a quality operator.

1. Decode bounded PNG/JPEG bytes, apply EXIF orientation, grayscale, resize to 64×64 and normalize.
2. Fit the mean healthy-image template using fit data.
3. Calibrate the 95th percentile absolute-error threshold using independent healthy calibration images.
4. Calculate an image-level anomaly score and recommend review above threshold.
5. Display score, threshold, data source and a required human-decision warning.

Reusable preprocessing, inference and evaluation are in `src/quality_inspection`. FastAPI/UI in `app/` and CLI are thin adapters. The API fits only synthetic images at startup. Public-data CLI uses independent MVTec splits and emits metrics plus hashes into ignored `artifacts/`.

Invalid/oversized bytes produce 422 or 413 without saving an image. No external network calls, databases or executable model files are needed at runtime. Service restart regenerates the same demo model.

The template baseline tests whether alignment-sensitive local logic is enough. Its weaknesses include pose/lighting changes and small localized defects diluted by global mean error. A rejected baseline is a valid learning result. Alternatives for the next experiment are robust region features or a compact local anomaly model; compare against this baseline before spending GPU/API resources.

