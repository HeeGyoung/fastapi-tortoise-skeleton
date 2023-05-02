#!/usr/bin/env bash

set -euo pipefail

wait-for-it test-db:3306
aerich --app exchange upgrade
aerich --app exchange_rate upgrade
aerich --app admin upgrade
uvicorn main:app --reload --host 0.0.0.0 --port 8005
