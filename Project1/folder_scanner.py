#!/usr/bin/env python3
"""Command-line tool that scans a folder and generates a summary report."""

import argparse
import os
import sys
from datetime import datetime
from collections import defaultdict


def format_size(size_bytes):
    """Convert bytes to a human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def scan_folder(folder_path, extensions=None):
    """Scan a folder and return statistics about its contents.

    Args:
        folder_path: Path to the directory to scan.
        extensions: Optional list of extensions to include (e.g. [".py", ".js"]).
                    If None, all files are included.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)

    # Normalise the filter set: ensure each extension starts with a dot
    ext_filter = None
    if extensions:
        ext_filter = set()
        for e in extensions:
            e = e.lower().strip()
            if not e.startswith("."):
                e = "." + e
            ext_filter.add(e)

    files = []
    dirs = []
    type_breakdown = defaultdict(lambda: {"count": 0, "size": 0})

    for entry in os.scandir(folder_path):
        if entry.is_dir(follow_symlinks=False):
            dirs.append(entry.name)
        elif entry.is_file(follow_symlinks=False):
            stat = entry.stat()
            ext = os.path.splitext(entry.name)[1].lower() or "(no extension)"

            # Skip files that don't match the filter
            if ext_filter and ext not in ext_filter:
                continue

            files.append({
                "name": entry.name,
                "size": stat.st_size,
                "extension": ext,
            })
            type_breakdown[ext]["count"] += 1
            type_breakdown[ext]["size"] += stat.st_size

    total_size = sum(f["size"] for f in files)
    largest = max(files, key=lambda f: f["size"]) if files else None

    return {
        "folder_path": os.path.abspath(folder_path),
        "total_files": len(files),
        "total_folders": len(dirs),
        "files": files,
        "folders": dirs,
        "total_size": total_size,
        "largest_file": largest,
        "type_breakdown": dict(type_breakdown),
    }


def build_report(stats):
    """Build a formatted report string from scan statistics."""
    lines = []
<<<<<<< HEAD
    sep = "-" * 60

    lines.append(sep)
    lines.append("  DIRECTORY SCAN SUMMARY (MAIN)")
    lines.append(sep)
    lines.append(f"  Path:     {stats['folder_path']}")
    lines.append(f"  Run at:   {datetime.now().strftime('%d %b %Y, %I:%M %p')}")
=======
    sep = "*" * 60

    lines.append(sep)
    lines.append("  FOLDER ANALYSIS REPORT (v2.0)")
    lines.append(sep)
    lines.append(f"  Directory:  {stats['folder_path']}")
    lines.append(f"  Generated:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
>>>>>>> feature/update-report-header
    if stats.get("filter"):
        lines.append(f"  Filter:   {', '.join(stats['filter'])}")
    lines.append(sep)

    # Overview
    lines.append("\n>> Overview")
    lines.append(f"   Total files:    {stats['total_files']}")
    lines.append(f"   Total folders:  {stats['total_folders']}")
    lines.append(f"   Total size:     {format_size(stats['total_size'])}")

    # Largest file
    lines.append(f"\n>> Largest File")
    if stats["largest_file"]:
        lf = stats["largest_file"]
        lines.append(f"   {lf['name']}  ({format_size(lf['size'])})")
    else:
        lines.append("   (no files found)")

    # File type breakdown
    lines.append(f"\n>> File Type Breakdown")
    breakdown = stats["type_breakdown"]
    if breakdown:
        # Sort by count descending
        for ext, info in sorted(breakdown.items(), key=lambda x: x[1]["count"], reverse=True):
            lines.append(f"   {ext:<20} {info['count']:>5} file(s)   {format_size(info['size']):>12}")
    else:
        lines.append("   (no files found)")

    # Individual file listing
    lines.append(f"\n>> All Files")
    if stats["files"]:
        for f in sorted(stats["files"], key=lambda x: x["size"], reverse=True):
            lines.append(f"   {f['name']:<40} {format_size(f['size']):>12}")
    else:
        lines.append("   (no files found)")

    # Subfolder listing
    if stats["folders"]:
        lines.append(f"\n>> Subfolders")
        for d in sorted(stats["folders"]):
            lines.append(f"   {d}/")

    lines.append("\n" + sep)
    lines.append("  END OF REPORT")
    lines.append(sep)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Scan a folder and generate a summary report."
    )
    parser.add_argument("folder", help="Path to the folder to scan")
    parser.add_argument(
        "-o", "--output",
        help="Output report file path (default: scan_report.txt in current directory)",
        default="scan_report.txt",
    )
    parser.add_argument(
        "-e", "--ext",
        nargs="+",
        metavar="EXT",
        help="Filter by file extension(s). Example: -e .py .js  or  -e py js",
    )
    args = parser.parse_args()

    stats = scan_folder(args.folder, extensions=args.ext)
    if args.ext:
        normalised = []
        for e in args.ext:
            e = e.lower().strip()
            if not e.startswith("."):
                e = "." + e
            normalised.append(e)
        stats["filter"] = sorted(set(normalised))
    report = build_report(stats)

    # Print to console
    print(report)

    # Save to file
    with open(args.output, "w") as f:
        f.write(report)

    print(f"\nReport saved to: {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
