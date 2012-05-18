# -*- encoding: utf-8 -*-
#
# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Doug Hellmann <doug.hellmann@dreamhost.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""Converters for producing compute counter messages from notification events.
"""

from .. import signature


def c1(body):
    """Generate c1(instance) counters for a notice."""
    c = {'source': '?',
         'counter_type': 'instance',
         'counter_volume': 1,
         'user_id': body['payload']['user_id'],
         'project_id': body['payload']['tenant_id'],
         'resource_id': body['payload']['instance_id'],
         'counter_datetime': body['timestamp'],
         'counter_duration': 0,
         # FIXME(dhellmann): Add region and other details to metadata
         'resource_metadata': {'display_name':
                                   body['payload']['display_name'],
                               'instance_type':
                                   body['payload']['instance_type_id'],
                               'host': body['publisher_id'],
                               },
         }
    c['message_signature'] = signature.compute_signature(c)
    return [c]
