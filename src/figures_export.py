from __future__ import annotations

from pathlib import Path
from typing import Mapping
import re

from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def _slugify_filename(name: str) -> str:
    """Convert a figure title into a safe file name."""
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9_-]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "figure"


def export_figure(
    fig: Figure,
    filename: str,
    output_dir: str | Path = "../reports/figures",
    dpi: int = 300,
    bbox_inches: str = "tight",
    facecolor: str = "white",
    close: bool = False,
) -> Path:
    """Save one matplotlib figure to disk and return the output path."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    safe_name = _slugify_filename(filename)
    if not safe_name.endswith(".png"):
        safe_name = f"{safe_name}.png"

    file_path = output_path / safe_name
    fig.savefig(file_path, dpi=dpi, bbox_inches=bbox_inches, facecolor=facecolor)

    if close:
        plt.close(fig)

    return file_path


def export_current_figure(
    filename: str,
    output_dir: str | Path = "../reports/figures",
    dpi: int = 300,
    bbox_inches: str = "tight",
    facecolor: str = "white",
    close: bool = False,
) -> Path:
    """Save the current active matplotlib figure."""
    fig = plt.gcf()
    return export_figure(
        fig=fig,
        filename=filename,
        output_dir=output_dir,
        dpi=dpi,
        bbox_inches=bbox_inches,
        facecolor=facecolor,
        close=close,
    )


def export_figures(
    figures: Mapping[str, Figure],
    output_dir: str | Path = "../reports/figures",
    dpi: int = 300,
    bbox_inches: str = "tight",
    facecolor: str = "white",
    close: bool = False,
) -> dict[str, Path]:
    """Save multiple matplotlib figures using a {name: figure} mapping."""
    exported: dict[str, Path] = {}

    for name, fig in figures.items():
        exported[name] = export_figure(
            fig=fig,
            filename=name,
            output_dir=output_dir,
            dpi=dpi,
            bbox_inches=bbox_inches,
            facecolor=facecolor,
            close=close,
        )

    return exported