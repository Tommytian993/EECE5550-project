#!/usr/bin/env bash
set -euo pipefail

sim_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

export GZ_SIM_RESOURCE_PATH="${sim_dir}/models${GZ_SIM_RESOURCE_PATH:+:${GZ_SIM_RESOURCE_PATH}}"

exec gz sim "${sim_dir}/worlds/empty_orchard.sdf" "$@"
