# Copyright (C) 2020 Linaro Limited
#
# Author: Antonio Terceiro <antonio.terceiro@linaro.org>
#
# SPDX-License-Identifier: GPL-2.0-or-later
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from lava_common.constants import DISPATCHER_DOWNLOAD_DIR
from lava_common.yaml import yaml_safe_dump, yaml_safe_load

if TYPE_CHECKING:
    from collections.abc import Iterator

DISPATCHER_DOWNLOAD_PATH = Path(DISPATCHER_DOWNLOAD_DIR)


def get_mapping_path(job_id) -> Path:
    return DISPATCHER_DOWNLOAD_PATH / str(job_id) / "usbmap.yaml"


def iter_mapping_paths() -> Iterator[Path]:
    yield from DISPATCHER_DOWNLOAD_PATH.glob("*/usbmap.yaml")


def add_device_container_mapping(job_id, device_info, container, container_type="lxc"):
    validate_device_info(device_info)
    item = {
        "device_info": device_info,
        "container": container,
        "container_type": container_type,
        "job_id": job_id,
    }
    mapping_path = get_mapping_path(job_id)
    data = load_mapping_data(mapping_path)

    # remove old mappings for the same device_info
    newdata = [old for old in data if old["device_info"] != item["device_info"]]
    newdata.append(item)

    mapping_path.parent.mkdir(exist_ok=True)
    with open(mapping_path, "w") as f:
        f.write(yaml_safe_dump(newdata))


def remove_device_container_mappings(job_id):
    get_mapping_path(job_id).unlink(missing_ok=True)


def validate_device_info(device_info):
    if not device_info:
        raise ValueError("Adding mapping for empty device info: %r" % device_info)
    if not any(device_info.values()):
        raise ValueError(
            "Adding mapping for device info with empty keys: %r" % device_info
        )


def load_mapping_data(filename):
    try:
        with open(filename) as f:
            data = yaml_safe_load(f) or []
        if isinstance(data, dict):
            data = [data]
        return data
    except FileNotFoundError:
        return []
