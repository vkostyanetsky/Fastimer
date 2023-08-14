#!/usr/bin/env python3

"""Implementation of methods to generate detailed view of a fast."""

import datetime
import typing

from vkostyanetsky.cliutils import title_and_value  # type: ignore

from .utils import get_time_difference, is_fast_completed, is_fast_stopped
