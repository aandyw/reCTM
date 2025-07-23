#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# This script sets up a Conda environment with Python 3.12 and installs the
# required packages from requirements.txt in a RunPod instance.
# ---------------------------------------------------------------------------

set -e
curl -sSfL https://gist.githubusercontent.com/aandyw/5fc1b9feb101b940d3ed089c2b735019/raw/setup_conda_runpod.sh \
    | bash -s -- --python 3.12 --env ctm --requirements requirements.txt
exec "$@"
