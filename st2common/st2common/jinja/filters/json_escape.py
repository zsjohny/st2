# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections

__all__ = [
    'json_escape'
]


def json_escape(value, indent=4, allow_unicode=True):
    """
    Backspace is replaced with \b
    Form feed is replaced with \f
    Newline is replaced with \n
    Carriage return is replaced with \r
    Tab is replaced with \t
    Double quote is replaced with \"
    Backslash is replaced with \\
    """

    replace_dict = collections.OrderedDict([
        ("\\", r"\\\\"),  # backslash (MUST go 1st so it doesn't escape \ inserted by another match)
        ('\"', r'\\"'),  # double quote
        ("\b", r"\\b"),  # backspace
        ("\t", r"\\t"),  # tab
        ("\n", r"\\n"),  # newline

        # These don't work yet, and I hate them because they are stupid.
        # ("\f", r"\\f"),  # form feed (this doesn't work and I hate it)
        # ("\r", r"\\r"),  # carriage return
    ])
    value = str(value)
    for old, new in replace_dict.items():
        value = value.replace(old, new)

    return value
