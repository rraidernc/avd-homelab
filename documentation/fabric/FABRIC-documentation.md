# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | dc1-border-leaf1a | 192.168.4.140/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-border-leaf1b | 192.168.4.141/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf1a | 192.168.4.122/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf1b | 192.168.4.123/22 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc1-leaf1c | 192.168.4.124/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2a | 192.168.4.126/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2b | 192.168.4.127/22 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc1-leaf2c | 192.168.4.128/22 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc1-spine1 | 192.168.4.120/22 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc1-spine2 | 192.168.4.121/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-border-leaf1a | 192.168.4.142/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-border-leaf1b | 192.168.4.143/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf1a | 192.168.4.132/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf1b | 192.168.4.133/22 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc2-leaf1c | 192.168.4.134/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf2a | 192.168.4.136/22 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf2b | 192.168.4.137/22 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc2-leaf2c | 192.168.4.138/22 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc2-spine1 | 192.168.4.130/22 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc2-spine2 | 192.168.4.131/22 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l3leaf | dc1-border-leaf1a | Ethernet1 | spine | dc1-spine1 | Ethernet5 |
| l3leaf | dc1-border-leaf1a | Ethernet2 | spine | dc1-spine2 | Ethernet5 |
| l3leaf | dc1-border-leaf1a | Ethernet3 | mlag_peer | dc1-border-leaf1b | Ethernet3 |
| l3leaf | dc1-border-leaf1a | Ethernet4 | l3leaf | dc2-border-leaf1a | Ethernet4 |
| l3leaf | dc1-border-leaf1b | Ethernet1 | spine | dc1-spine1 | Ethernet6 |
| l3leaf | dc1-border-leaf1b | Ethernet2 | spine | dc1-spine2 | Ethernet6 |
| l3leaf | dc1-border-leaf1b | Ethernet4 | l3leaf | dc2-border-leaf1b | Ethernet4 |
| l3leaf | dc1-leaf1a | Ethernet1 | spine | dc1-spine1 | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet2 | spine | dc1-spine2 | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet3 | mlag_peer | dc1-leaf1b | Ethernet3 |
| l3leaf | dc1-leaf1a | Ethernet8 | l2leaf | dc1-leaf1c | Ethernet1 |
| l3leaf | dc1-leaf1b | Ethernet1 | spine | dc1-spine1 | Ethernet2 |
| l3leaf | dc1-leaf1b | Ethernet2 | spine | dc1-spine2 | Ethernet2 |
| l3leaf | dc1-leaf1b | Ethernet8 | l2leaf | dc1-leaf1c | Ethernet2 |
| l3leaf | dc1-leaf2a | Ethernet1 | spine | dc1-spine1 | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet2 | spine | dc1-spine2 | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet3 | mlag_peer | dc1-leaf2b | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet8 | l2leaf | dc1-leaf2c | Ethernet1 |
| l3leaf | dc1-leaf2b | Ethernet1 | spine | dc1-spine1 | Ethernet4 |
| l3leaf | dc1-leaf2b | Ethernet2 | spine | dc1-spine2 | Ethernet4 |
| l3leaf | dc1-leaf2b | Ethernet8 | l2leaf | dc1-leaf2c | Ethernet2 |
| l3leaf | dc2-border-leaf1a | Ethernet1 | spine | dc2-spine1 | Ethernet5 |
| l3leaf | dc2-border-leaf1a | Ethernet2 | spine | dc2-spine2 | Ethernet5 |
| l3leaf | dc2-border-leaf1a | Ethernet3 | mlag_peer | dc2-border-leaf1b | Ethernet3 |
| l3leaf | dc2-border-leaf1b | Ethernet1 | spine | dc2-spine1 | Ethernet6 |
| l3leaf | dc2-border-leaf1b | Ethernet2 | spine | dc2-spine2 | Ethernet6 |
| l3leaf | dc2-leaf1a | Ethernet1 | spine | dc2-spine1 | Ethernet1 |
| l3leaf | dc2-leaf1a | Ethernet2 | spine | dc2-spine2 | Ethernet1 |
| l3leaf | dc2-leaf1a | Ethernet3 | mlag_peer | dc2-leaf1b | Ethernet3 |
| l3leaf | dc2-leaf1a | Ethernet8 | l2leaf | dc2-leaf1c | Ethernet1 |
| l3leaf | dc2-leaf1b | Ethernet1 | spine | dc2-spine1 | Ethernet2 |
| l3leaf | dc2-leaf1b | Ethernet2 | spine | dc2-spine2 | Ethernet2 |
| l3leaf | dc2-leaf1b | Ethernet8 | l2leaf | dc2-leaf1c | Ethernet2 |
| l3leaf | dc2-leaf2a | Ethernet1 | spine | dc2-spine1 | Ethernet3 |
| l3leaf | dc2-leaf2a | Ethernet2 | spine | dc2-spine2 | Ethernet3 |
| l3leaf | dc2-leaf2a | Ethernet3 | mlag_peer | dc2-leaf2b | Ethernet3 |
| l3leaf | dc2-leaf2a | Ethernet8 | l2leaf | dc2-leaf2c | Ethernet1 |
| l3leaf | dc2-leaf2b | Ethernet1 | spine | dc2-spine1 | Ethernet4 |
| l3leaf | dc2-leaf2b | Ethernet2 | spine | dc2-spine2 | Ethernet4 |
| l3leaf | dc2-leaf2b | Ethernet8 | l2leaf | dc2-leaf2c | Ethernet2 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/26 | 64 | 24 | 37.5 % |
| 10.255.255.64/26 | 64 | 24 | 37.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dc1-border-leaf1a | Ethernet1 | 10.255.255.17/31 | dc1-spine1 | Ethernet5 | 10.255.255.16/31 |
| dc1-border-leaf1a | Ethernet2 | 10.255.255.19/31 | dc1-spine2 | Ethernet5 | 10.255.255.18/31 |
| dc1-border-leaf1a | Ethernet4 | 172.100.100.0/31 | dc2-border-leaf1a | Ethernet4 | 172.100.100.1/31 |
| dc1-border-leaf1b | Ethernet1 | 10.255.255.21/31 | dc1-spine1 | Ethernet6 | 10.255.255.20/31 |
| dc1-border-leaf1b | Ethernet2 | 10.255.255.23/31 | dc1-spine2 | Ethernet6 | 10.255.255.22/31 |
| dc1-border-leaf1b | Ethernet4 | 172.100.100.2/31 | dc2-border-leaf1b | Ethernet4 | 172.100.100.3/31 |
| dc1-leaf1a | Ethernet1 | 10.255.255.1/31 | dc1-spine1 | Ethernet1 | 10.255.255.0/31 |
| dc1-leaf1a | Ethernet2 | 10.255.255.3/31 | dc1-spine2 | Ethernet1 | 10.255.255.2/31 |
| dc1-leaf1b | Ethernet1 | 10.255.255.5/31 | dc1-spine1 | Ethernet2 | 10.255.255.4/31 |
| dc1-leaf1b | Ethernet2 | 10.255.255.7/31 | dc1-spine2 | Ethernet2 | 10.255.255.6/31 |
| dc1-leaf2a | Ethernet1 | 10.255.255.9/31 | dc1-spine1 | Ethernet3 | 10.255.255.8/31 |
| dc1-leaf2a | Ethernet2 | 10.255.255.11/31 | dc1-spine2 | Ethernet3 | 10.255.255.10/31 |
| dc1-leaf2b | Ethernet1 | 10.255.255.13/31 | dc1-spine1 | Ethernet4 | 10.255.255.12/31 |
| dc1-leaf2b | Ethernet2 | 10.255.255.15/31 | dc1-spine2 | Ethernet4 | 10.255.255.14/31 |
| dc2-border-leaf1a | Ethernet1 | 10.255.255.81/31 | dc2-spine1 | Ethernet5 | 10.255.255.80/31 |
| dc2-border-leaf1a | Ethernet2 | 10.255.255.83/31 | dc2-spine2 | Ethernet5 | 10.255.255.82/31 |
| dc2-border-leaf1b | Ethernet1 | 10.255.255.85/31 | dc2-spine1 | Ethernet6 | 10.255.255.84/31 |
| dc2-border-leaf1b | Ethernet2 | 10.255.255.87/31 | dc2-spine2 | Ethernet6 | 10.255.255.86/31 |
| dc2-leaf1a | Ethernet1 | 10.255.255.65/31 | dc2-spine1 | Ethernet1 | 10.255.255.64/31 |
| dc2-leaf1a | Ethernet2 | 10.255.255.67/31 | dc2-spine2 | Ethernet1 | 10.255.255.66/31 |
| dc2-leaf1b | Ethernet1 | 10.255.255.69/31 | dc2-spine1 | Ethernet2 | 10.255.255.68/31 |
| dc2-leaf1b | Ethernet2 | 10.255.255.71/31 | dc2-spine2 | Ethernet2 | 10.255.255.70/31 |
| dc2-leaf2a | Ethernet1 | 10.255.255.73/31 | dc2-spine1 | Ethernet3 | 10.255.255.72/31 |
| dc2-leaf2a | Ethernet2 | 10.255.255.75/31 | dc2-spine2 | Ethernet3 | 10.255.255.74/31 |
| dc2-leaf2b | Ethernet1 | 10.255.255.77/31 | dc2-spine1 | Ethernet4 | 10.255.255.76/31 |
| dc2-leaf2b | Ethernet2 | 10.255.255.79/31 | dc2-spine2 | Ethernet4 | 10.255.255.78/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 8 | 25.0 % |
| 10.255.128.0/27 | 32 | 8 | 25.0 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | dc1-border-leaf1a | 10.255.0.7/32 |
| FABRIC | dc1-border-leaf1b | 10.255.0.8/32 |
| FABRIC | dc1-leaf1a | 10.255.0.3/32 |
| FABRIC | dc1-leaf1b | 10.255.0.4/32 |
| FABRIC | dc1-leaf2a | 10.255.0.5/32 |
| FABRIC | dc1-leaf2b | 10.255.0.6/32 |
| FABRIC | dc1-spine1 | 10.255.0.1/32 |
| FABRIC | dc1-spine2 | 10.255.0.2/32 |
| FABRIC | dc2-border-leaf1a | 10.255.128.7/32 |
| FABRIC | dc2-border-leaf1b | 10.255.128.8/32 |
| FABRIC | dc2-leaf1a | 10.255.128.3/32 |
| FABRIC | dc2-leaf1b | 10.255.128.4/32 |
| FABRIC | dc2-leaf2a | 10.255.128.5/32 |
| FABRIC | dc2-leaf2b | 10.255.128.6/32 |
| FABRIC | dc2-spine1 | 10.255.128.11/32 |
| FABRIC | dc2-spine2 | 10.255.128.12/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 6 | 18.75 % |
| 10.255.129.0/27 | 32 | 6 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | dc1-border-leaf1a | 10.255.1.7/32 |
| FABRIC | dc1-border-leaf1b | 10.255.1.7/32 |
| FABRIC | dc1-leaf1a | 10.255.1.3/32 |
| FABRIC | dc1-leaf1b | 10.255.1.3/32 |
| FABRIC | dc1-leaf2a | 10.255.1.5/32 |
| FABRIC | dc1-leaf2b | 10.255.1.5/32 |
| FABRIC | dc2-border-leaf1a | 10.255.129.7/32 |
| FABRIC | dc2-border-leaf1b | 10.255.129.7/32 |
| FABRIC | dc2-leaf1a | 10.255.129.3/32 |
| FABRIC | dc2-leaf1b | 10.255.129.3/32 |
| FABRIC | dc2-leaf2a | 10.255.129.5/32 |
| FABRIC | dc2-leaf2b | 10.255.129.5/32 |
