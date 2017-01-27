#!/usr/bin/python

#
# Copyright (c) 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

import ovirtsdk4 as sdk
import ovirtsdk4.types as types

logging.basicConfig(level=logging.DEBUG, filename='example.log')

# This example will connect to the server and remove a snapshot to an
# existing virtual machine:

# Create the connection to the server:
connection = sdk.Connection(
  url='https://acore.v100.abes.fr/ovirt-engine/api',
  username='admin@internal',
  password='',
#  ca_file='ca.pem',
  insecure=True,
  debug=True,
  log=logging.getLogger(),
)

# Locate the virtual machines service and use it to find the virtual
# machine:
vms_service = connection.system_service().vms_service()
vm = vms_service.list(search='name=test_cloud')[0]

# Locate the service that manages the snapshots of the virtual machine:
vm_service = vms_service.vm_service(vm.id)
snaps_service = vm_service.snapshots_service()
snaps = snaps_service.list()
snap = [s for s in snaps if s.description == 'My snapshot2'][0]

# Remove the snapshot:
snap_service = snaps_service.snapshot_service(snap.id)
snap_service.remove()

# Close the connection to the server:
connection.close()
