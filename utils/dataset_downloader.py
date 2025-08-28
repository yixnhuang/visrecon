import argparse
import os
from huggingface_hub import snapshot_download


def download_subset(repo_id: str, subset_folder: str, local_dir: str = "./data") -> None:
    """
    Download a specific subset (folder) from a Hugging Face dataset repository.

    Parameters
    ----------
    repo_id : str
        Hugging Face dataset repository ID, e.g., "username/my_dataset".
    subset_folder : str
        The target folder inside the repository to download, e.g., "human".
    local_dir : str, optional
        Local directory to save the downloaded files (default is "./data").

    Notes
    -----
    Only files inside the specified `subset_folder` will be downloaded.
    """
    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        local_dir=local_dir,
        allow_patterns=f"{subset_folder}/*"  # Restrict download to subset folder
    )

    subset_path = os.path.join(local_dir, subset_folder)
    print(f"✅ Subset '{subset_folder}' successfully downloaded to '{subset_path}'")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download a specific subset from a Hugging Face dataset repository."
    )
    parser.add_argument(
        "--repo_id", type=str, default="yixuan-huang/Obj3D",
        help="Hugging Face dataset repository ID (default: 'yixuan-huang/Obj3D')"
    )
    parser.add_argument(
        "--subset", type=str, required=True,
        help="Subset folder name to download, e.g., 'human'"
    )
    parser.add_argument(
        "--local_dir", type=str, default="./data",
        help="Local directory to save downloaded files (default: './data')"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    download_subset(args.repo_id, args.subset, args.local_dir)

    # Example usage:
    # python download_subset.py --subset human
    # python download_subset.py --subset human/human_000
    # python download_subset.py --repo_id yixuan-huang/Plant3D --subset Plant_000
