#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Tim Miller <timmil@cisco.com>"
__contributors__ = [
]
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

# Required attributes for each category of object being
# defined and managed by the sync process

cdp_attributes = ['name', 'adminSt']

lldp_attributes = ['name', 'adminRxSt', 'adminTxSt']

link_level_attributes = ['name', 'autoNeg', 'speed']

mcp_attributes = ['name', 'adminSt']

snmp_attributes = {
  'snmpPol': {
    'name': None,
    'adminSt': None,
    'contact': None,
    'loc': None,
    'snmpUserP': ['name', 'privType', 'privKey', 'authType', 'authKey'],
    'snmpTrapFwdServerP': ['addr', 'port'],
    'snmpCommunityP': ['name'],
    'snmpClientGrpP': {
      'name': None,
      'snmpClientP': ['name', 'addr']
    }
  }
}

snmp_group_attributes = {
  'snmpGroup': {
    'name': None,
    'snmpTrapDest': ['host', 'notifT', 'port', 'secName', 'v3SecLvl', 'ver']
  }
}

coop_attributes = ['name', 'type']

rogue_endpoint_attributes = [
  'name', 'adminSt', 'holdIntvl', 'rogueEpDetectIntvl', 'rogueEpDetectMult'
]

ip_aging_attributes = ['name', 'adminSt']

fabric_wide_attributes = ['name', 'domainValidation', 'enforceSubnetCheck']

bgp_attributes = {
  'bgpInstPol': {
    'name': None,
    'bgpAsP': ['asn'],
    'bgpRRP': ['podId', 'bgpRRNodePEp']
  },
}

dns_attributes = {
  'dnsProfile': {
    'name': None,
    'epgDn': None,
    'dnsProv': ['addr', 'preferred'],
    'dnsDomain': ['name', 'isDefault']
  },
}

ntp_provider_attributes = ['name', 'minPoll', 'maxPoll', 'preferred']
# ntp_auth_key_attributes = ['key', 'keyType', 'trusted']

ntp_attributes = {
  'datetimePol': {
    'name': None,
    'adminSt': None,
    'authSt': None,
    'serverState': None,
    'masterMode': None,
#    'datetimeNtpProv': ntp_provider_attributes + ntp_auth_key_attributes
    'datetimeNtpProv': ntp_provider_attributes
  }
}

syslog_attributes = {
  'syslogGroup': {
    'name': None,
    'format': None,
    'includeMilliSeconds': None,
    'syslogRemoteDest': [
      'name', 'host', 'port', 'adminState', 'format', 'severity', 'forwardingFacility'
    ],
    'syslogProf': ['name', 'adminState'],
    'syslogFile': ['adminState', 'format', 'severity'],
    'syslogConsole': ['adminState', 'format', 'severity']
  }
}
