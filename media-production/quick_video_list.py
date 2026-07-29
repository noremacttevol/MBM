#!/usr/bin/env python3
"""Quick MBM video listing and file property scanner"""

from pathlib import Path
from datetime import datetime

MEDIA_ROOT = Path.cwd()
QC_FILE = MEDIA_ROOT / "qc" / "defects.json"

def main():
    results = []
    
    # Find all video builds
    for build_dir in sorted(MEDIA_ROOT.glob("build-*")):
        if not build_dir.is_dir():
            continue
            
        for video_file in build_dir.glob("*.mp4"):
            props = {
                "video": str(video_file.absolute()),
                "name": str(video_file.relative_to(MEDIA_ROOT)),
                "size_bytes": video_file.stat().st_size,
                "modified": datetime.fromtimestamp(video_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            }
            results.append(props)
    
    # Create initial QC file
    qc_data = {
        "qc_date": datetime.now().strftime("%Y-%m-%d"),
        "total_videos": len(results),
        "videos": results,
        "defects": [],
        "note": "Video QC requires human review per DEFECT-CATALOG.md. Use vision_analyze() to inspect frames and audio waveform analysis for defects."
    }
    
    with open(QC_FILE, 'w') as f:
        json.dump(qc_data, f, indent=2, default=str)
    
    print(f"Found {len(results)} videos")
    print(f"Wrote to {QC_FILE}")
    
    # Show first few
    for v in results[:3]:
        print(f"  ✓ {v['name']} ({v['size_bytes']/1024/1024:.1f}MB)")

if __name__ == '__main__':
    import json
    main()
