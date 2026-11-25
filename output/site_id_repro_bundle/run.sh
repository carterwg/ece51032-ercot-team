#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 /absolute/path/to/ece51032-ercot-team /absolute/path/to/new-output" >&2
  exit 2
fi

bundle_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd -- "$1" && pwd)"
output_dir="$2"
mkdir -p -- "$output_dir"
output_dir="$(cd -- "$output_dir" && pwd)"

if [[ ! -x "$repo_dir/.venv/bin/python" ]]; then
  echo "Expected a Python environment at $repo_dir/.venv/bin/python" >&2
  exit 2
fi

export PYTHONPATH="$repo_dir/ercot-connection-game:$repo_dir/ercot-connection-game/src${PYTHONPATH:+:$PYTHONPATH}"
"$repo_dir/.venv/bin/python" "$bundle_dir/reproduce.py" \
  --source-inputs "$bundle_dir/inputs" \
  --s1-output "$bundle_dir/s1-output" \
  --s2-base "$bundle_dir/s2-base" \
  --rules "$bundle_dir/rules.json" \
  --output "$output_dir"

echo "Comparison files: $output_dir/{original,reverse_rows_only,reverse_ids_only,reverse_both}/result.json"
