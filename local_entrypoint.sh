#!/usr/bin/env bash

set -euo pipefail

wait-for-it local-db:3306
aerich init-db
aerich upgrade
uvicorn main:app --reload --host 0.0.0.0 --port 8005
