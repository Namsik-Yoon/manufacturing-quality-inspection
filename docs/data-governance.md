# Dataset rights, acquisition and reproducibility

**Observed from official publisher; checked 2026-10-06:** [MVTec AD](https://www.mvtec.com/research-teaching/datasets/mvtec-ad) contains industrial inspection images and anomaly annotations. Data is CC BY-NC-SA 4.0; commercial use is not permitted by these terms. The project's MIT code license does not replace the data license.

Attribution: Paul Bergmann, Michael Fauser, David Sattlegger and Carsten Steger, *MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection*, CVPR 2019. See the [publisher paper](https://www.mvtec.com/fileadmin/Redaktion/mvtec.com/company/research/datasets/mvtec_ad.pdf). Preserve attribution and applicable share-alike conditions for distributed data adaptations; this repo distributes no benchmark images/weights.

## Minimal manual access

1. Open the official MVTec AD page and review current terms.
2. Complete its official download form yourself; use the publisher-provided download route. Do not scrape around the form or use an unverified mirror.
3. Download/extract the original archive locally. Keep raw inputs immutable.
4. Place the category so these paths exist: `data/raw/mvtec-ad/bottle/train/good/*.png`, `bottle/test/good/*.png`, `bottle/test/<defect>/*.png`. Ground-truth masks remain available but are not used by this image-level baseline.
5. Run `uv run python scripts/prepare_data.py --data-root data/raw/mvtec-ad`. It records SHA-256 per local image without altering raw data.
6. Run the documented evaluation command. Hashes, preprocessing and split roles are embedded in its report.

Raw images, archives, manifests, model weights and generated image outputs are ignored. Preserve archive source, acquisition date and checksum in your local experiment evidence. Share only small lawful summary metrics in committed docs.

## Preprocessing and leakage

PNG/JPEG → EXIF orientation → grayscale → 64×64 bilinear resize → float [0,1]. Fit mean template on healthy training images excluding every fifth sorted file; that reserved 20% calibrates the threshold. Official test labels only score the final baseline. No labels or masks from test are used to tune it.

Proxy gaps: real prevalence, operations/cost, lighting drift, camera calibration and commercial acceptability are **To Validate**. The baseline is alignment-sensitive.

## Data and cache cleanup

`uv run python scripts/clean_cache.py` previews generated lint/test caches; add `--confirm` to remove only those caches. It never removes raw data or experiment artifacts. Manage intentionally unwanted raw downloads through your own file manager after confirming what to remove. There is no automatic large-data deletion.

