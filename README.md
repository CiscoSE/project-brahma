# Project Brahma

Cisco ACI deployment...SIMPLIFIED!

A proof of concept to showcase how the ACI API can be leveraged to drastically
simplify the setup of an ACI fabric following the network centric design model.

## Motivation

When initially deploying an ACI fabric, there are a great many design decisions that
have to be made given the enormous flexibility that the fabric provides. Because the
solution is meant to primarily focus on applications and abstract away the physical
device element configurations, the notion of common concepts from NX-OS such as the
standardized interface names (Ethernet1/1, e.g.) aren't necessary.

Most customers adopting ACI though are not ready to jump from a traditional 2-tier or
3-tier design directly into an application centric, white list only approach to network
design. To ease that transition, we can leverage the flexibility of the fabric to model
the fabric to operate similar to traditional network concepts:

- "bridge domains" that map directly to a VLAN name
- "IP subnet" that maps 1:1 to a VLAN/bridge domain
- "EPGs" for a VLAN constructed such that all devices in a VLAN can freely communicate

Additionally, the typical policies we all run across in our daily lives need a naming
convention and actually need to be defined. Rather than go through the extensive
checklist, Project Brahma builds all those policies using sane, best practice defaults - such as:

- "Eth1-1" for the first port on the switch
- "1G_Auto" for 1Gbps autonegotiate speed settings
- "CDP_Enabled" for policy to enable CDP

In summary, the workflow that Project Brahma provides only requires the typical information
a network engineer would discuss when talking about their network design: VLAN IDs, subnets,
SNMP information, NTP information, etc. and the underlying automation applies the policies
and necessary access control.

## Aspiration

A SaaS-like application that would securely connect to your ACI environment to fetch existing
configuration, provide a web interface for user consumption, and push configuration back to
the ACI environment.

The hope is that Project Brahma could be easily integrated into the ACI application framework as an
application from the marketplace or the concepts incorporated directly into the ACI APIC
code base.

## Project History

This project started as a PoC for a Cisco internal quarterly challenge to promote
innovation thinking. It was developed against the ACI Simulator available in dCloud
and every attempt was made to validate the policies we intended to create were actually
created.

Please refer to the Issues in this repository to understand what Project Brahma can do
for you as well as what it may not yet do for you.

### Cisco Products Technologies/ Services

Our solution leverages the following Cisco technologies:

- [Application Centric Infrastructure (ACI)](http://cisco.com/go/aci)
- [ACI Cobra SDK](https://github.com/datacenter/cobra)

## Project Developer Team Members

- Matt Garrett - DC TSA (Emeritus)
- Tim Miller - GVE DC TSA
- Tyson Scott - GES DC TSA
- Mike Finch - GES DC TSA

## License

Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE.md)

## Code of Conduct

Our code of conduct is available [here](./CODE_OF_CONDUCT.md)

## Contributing

See our contributing guidelines [here](./CONTRIBUTING.md)
