#!/usr/bin/env bash
set -euo pipefail

# Bootstrap helper for 93won/360_visual_inertial_odometry.
# - Optionally clones the repo (with submodules)
# - Injects PoseLogger + CMake snippet + VS Code settings
# - Leaves an idempotent marker inside CMakeLists.txt

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/templates"
DEFAULT_CLONE_DIR="$SCRIPT_DIR/360_visual_inertial_odometry"
MARKER="# === aviabox VIO sandbox ==="

usage() {
  cat <<USAGE
Usage: $0 [--clone <url>] [--patch-only <path>]

--clone <url>        Clone the upstream/fork (with submodules) into $DEFAULT_CLONE_DIR
--patch-only <path>  Skip cloning and only patch an existing checkout

Examples:
  $0 --clone https://github.com/AVIUS001/aviabox_2025/360_visual_inertial_odometry.git
  $0 --patch-only $DEFAULT_CLONE_DIR
USAGE
}

clone_url=""
patch_only=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --clone)
      clone_url="$2"; shift 2 ;;
    --patch-only)
      patch_only="$2"; shift 2 ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      echo "Unknown argument: $1" >&2
      usage; exit 1 ;;
  esac
done

target_dir="$DEFAULT_CLONE_DIR"

if [[ -n "$clone_url" ]]; then
  if [[ -d "$target_dir/.git" ]]; then
    echo "Target directory already contains a git repo: $target_dir"
  else
    echo "Cloning $clone_url -> $target_dir"
    git clone --recursive "$clone_url" "$target_dir"
  fi
fi

if [[ -n "$patch_only" ]]; then
  target_dir="$patch_only"
fi

if [[ ! -d "$target_dir" ]]; then
  echo "Target directory does not exist: $target_dir" >&2
  exit 1
fi

if [[ -d "$target_dir/.git" ]]; then
  echo "Updating submodules in $target_dir"
  (cd "$target_dir" && git submodule update --init --recursive || true)
fi

# Copy PoseLogger sources
mkdir -p "$target_dir/src/utils"
cp -f "$TEMPLATE_DIR/pose_logger.h" "$target_dir/src/utils/pose_logger.h"
cp -f "$TEMPLATE_DIR/pose_logger.cpp" "$target_dir/src/utils/pose_logger.cpp"

# Append CMake snippet once
cmake_file="$target_dir/CMakeLists.txt"
if [[ -f "$cmake_file" ]] && ! grep -q "$MARKER" "$cmake_file"; then
  {
    echo ""
    echo "$MARKER"
    cat "$TEMPLATE_DIR/cmake_pose_logger_append.cmake"
  } >> "$cmake_file"
  echo "Appended PoseLogger + ZeroMQ CMake block to $cmake_file"
else
  echo "CMakeLists.txt already patched or missing; skipped append"
fi

# Drop VS Code templates
mkdir -p "$target_dir/.vscode"
cp -f "$TEMPLATE_DIR/settings.json" "$target_dir/.vscode/settings.json"
cp -f "$TEMPLATE_DIR/launch.json" "$target_dir/.vscode/launch.json"
cp -f "$TEMPLATE_DIR/tasks.json" "$target_dir/.vscode/tasks.json"

echo "Sandbox ready at $target_dir"
echo "Set VIO_DATASET_PATH to your seq1_vio folder before launching from VS Code."
