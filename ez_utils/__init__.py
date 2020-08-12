#!/usr/bin/env python
# coding:utf8
"""
@Time       :   2018/10/31
@Author     :   fls
@Contact    :   fls@darkripples.com
@Desc       :   fls易用性utils

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2018/10/31 11:41   fls        1.0.0         create
2020/08/01 11:43   fls        1.0.1         新增函数get_current_week
"""
version = "1.0.1"

from .fls_log import log_func

flog = log_func()
from .attrdict import AttrDict as fdic
from .date_utils import (fmt_date as fmt_date, get_day_n as after_date, get_seconds_n as after_seconds,
                         get_interval_day as interval_day, reformat_date_str as reformat_date_str,
                         str2date as str2date, get_current_week)
from .date_utils import FMT_DATETIME, FMT_DATE, FMT_TIME, FMT_DATETIME_SEPARATE
from .fmt_utils import allot_list
from .read_conf_utils import read_conf
from .err_utils import err_check
