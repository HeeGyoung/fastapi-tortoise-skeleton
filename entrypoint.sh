#!/usr/bin/env bash

set -euo pipefail

aerich upgrade
uvicorn main:app --reload --host 0.0.0.0 --port 8005
