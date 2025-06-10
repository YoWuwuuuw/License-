import os
import fnmatch


def check_and_add_license_header(filepath, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(filepath, pattern):
            print(f"Skipping {filepath} due to ignore pattern: {pattern}")
            return

    if filepath.endswith(".md"):
        license_header = """
<!--
    Licensed to the Apache Software Foundation (ASF) under one or more
    contributor license agreements.  See the NOTICE file distributed with
    this work for additional information regarding copyright ownership.
    The ASF licenses this file to You under the Apache License, Version 2.0
    (the "License"); you may not use this file except in compliance with
    the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
-->
"""
        header_check_string = "Licensed to the Apache Software Foundation (ASF) under one or more"

    elif filepath.endswith((".yml", ".yaml")):
        license_header = """
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""

        header_check_string = "Licensed to the Apache Software Foundation (ASF) under one"

        old_license_header_format1 = """
#
# Licensed to the Apache Software Foundation (ASF) under one or more
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
#
"""
        old_license_header_format2 = """
#
# Licensed to the Apache Software Foundation (ASF) under one or more
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
#

"""

    elif filepath.endswith(".ftl"):
        license_header = """
<#--
    Licensed to the Apache Software Foundation (ASF) under one or more
    contributor license agreements.  See the NOTICE file distributed with
    this work for additional information regarding copyright ownership.
    The ASF licenses this file to You under the Apache License, Version 2.0
    (the "License"); you may not use this file except in compliance with
    the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
-->"""
        header_check_string = "Licensed to the Apache Software Foundation (ASF) under one or more"

    elif filepath.endswith(".java"):
        license_header = """
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 """

        header_check_string = "Licensed to the Apache Software Foundation (ASF) under one or more"
    else:
        return

    try:
        with open(filepath, 'r+') as f:
            content = f.read()

            if filepath.endswith((".yml", ".yaml")):
                if old_license_header_format1 in content:
                    content = content.replace(old_license_header_format1, license_header)
                    f.seek(0, 0)
                    f.write(content)
                    f.truncate()
                    print(f"Replaced old license header format 1 in {filepath}")
                elif old_license_header_format2 in content:
                    content = content.replace(old_license_header_format2, license_header)
                    f.seek(0, 0)
                    f.write(content)
                    f.truncate()
                    print(f"Replaced old license header format 2 in {filepath}")
                elif header_check_string not in content:
                    f.seek(0, 0)
                    f.write(license_header.rstrip('\n') + '\n\n' + content)
                    print(f"License header added to {filepath}")
                else:
                    print(f"License header already exists in {filepath}")
            elif filepath.endswith(".ftl"):
                if header_check_string not in content:
                    f.seek(0, 0)
                    f.write(license_header.rstrip('\n') + '\n\n' + content)
                    print(f"License header added to {filepath}")
                else:
                    print(f"License header already exists in {filepath}")
            else:
                if header_check_string not in content:
                    f.seek(0, 0)
                    f.write(license_header.rstrip('\n') + '\n\n' + content)
                    print(f"License header added to {filepath}")
                else:
                    print(f"License header already exists in {filepath}")


    except Exception as e:
        print(f"Error processing {filepath}: {e}")


def process_directory(directory, ignore_patterns):
    for root, _, files in os.walk(directory):
        for ignore_pattern in ignore_patterns:
            abs_ignore_path = os.path.normpath(os.path.join(directory, ignore_pattern))
            abs_root_path = os.path.normpath(os.path.join(directory, root))

            if fnmatch.fnmatch(abs_root_path + os.sep, abs_ignore_path):
                print(f"Skipping directory {root} due to ignore pattern: {ignore_pattern}")
                break

        else:
            for file in files:
                filepath = os.path.join(root, file)
                check_and_add_license_header(filepath, ignore_patterns)


def normalize_ignore_patterns(ignore_patterns):
    normalized_patterns = []
    for pattern in ignore_patterns:
        normalized_patterns.append(pattern)
    return normalized_patterns


if __name__ == "__main__":
    target_directory = "..."
    ignore_patterns = [
        'LICENSE',
        'NOTICE',
        'DISCLAIMER',
        '*.json',
        '.github/**',
        '.git/**',
    ]

    ignore_patterns = normalize_ignore_patterns(ignore_patterns)
    process_directory(target_directory, ignore_patterns)