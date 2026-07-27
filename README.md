# VisRecon

VisRecon is a research-oriented toolkit for capturing RGB-D imagery, preparing multi-view datasets, running COLMAP reconstruction workflows, and inspecting the resulting point clouds or meshes. It combines small command-line utilities with sample outputs from experiments using an Intel RealSense camera.

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-orange)](#project-status)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)
![Reconstruction](https://img.shields.io/badge/Reconstruction-COLMAP-4C8BF5)

## Overview

The repository supports a compact multi-view reconstruction workflow: capture or download image sets, prepare them for reconstruction, run a configurable COLMAP pipeline, and visualize the generated model. Samples and rendered demonstrations are included to make the expected inputs and outputs easier to understand.

## Features

- Capture RGB-D sequences from supported Intel RealSense cameras
- Prepare color and depth images for reconstruction experiments
- Download selected folders from a Hugging Face dataset repository
- Run a scripted COLMAP reconstruction pipeline
- Visualize sparse or dense point clouds and meshes with Open3D
- Review included sample images and reconstruction previews

## Structure

```text
.
├── demo/          # Rendered reconstruction examples
├── samples/       # Sample multi-view images
├── utils/         # Capture, download, preparation, and visualization tools
├── requirements.txt
└── LICENSE
```

## Requirements

- Python 3.10 or later
- [COLMAP](https://colmap.github.io/) available from the command line
- A supported Intel RealSense device for capture workflows

Install the Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Dataset Download

Download a folder from a Hugging Face dataset repository by supplying its repository ID:

```bash
python utils/dataset_downloader.py \
  --repo_id username/dataset \
  --subset path/to/subset \
  --local_dir ./data
```

## Usage

### Capture images

```bash
python utils/image_fetcher.py --help
```

### Prepare images

```bash
python utils/image_preparer.py --help
```

### Run reconstruction

Review the paths and options near the beginning of `utils/run_colmap_pipeline.sh`, then run:

```bash
bash utils/run_colmap_pipeline.sh
```

### Visualize a model

```bash
python utils/visualizer.py --help
```

## Samples

The `samples` directory contains a representative input sequence. The `demo` directory contains rendered mesh and point-cloud results for plant reconstructions.

## Project Status

Experimental. VisRecon is retained as a research toolkit and reference workflow.
Its utilities require local hardware, datasets, and COLMAP configuration and
should not be treated as a production reconstruction system.

## Contributing

Focused bug fixes, documentation improvements, and reusable reconstruction utilities are welcome. Open an issue before proposing a substantial workflow change.

## License

The source code in this repository is available under the [MIT License](LICENSE). Dataset and third-party tool licenses remain separate and should be reviewed at their respective sources.

## Contact

For questions or collaboration, use the contact details below or consult the
website for the latest information.

- Website: [yixuanhuang.com](https://yixuanhuang.com)
- Email: [yixnhuang@gmail.com](mailto:yixnhuang@gmail.com)
