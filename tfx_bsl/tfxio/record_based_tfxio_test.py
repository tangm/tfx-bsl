# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tfx_bsl.tfxio.record_based_tfxio."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tfx_bsl.tfxio import record_based_tfxio
from absl.testing import absltest


class RecordBasedTfxioTest(absltest.TestCase):

  def testGetBatchElementsKwargs(self):
    kwargs = record_based_tfxio.GetBatchElementsKwargs(batch_size=None)
    self.assertDictEqual(
        kwargs, {"max_batch_size": 1000})
    kwargs = record_based_tfxio.GetBatchElementsKwargs(batch_size=5000)
    self.assertDictEqual(
        kwargs, {"max_batch_size": 5000, "min_batch_size": 5000})


if __name__ == "__main__":
  absltest.main()
