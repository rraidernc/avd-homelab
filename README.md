# Arista AVD Dual DC Homelab

A fully automated dual data center L3LS EVPN/VXLAN fabric built with Arista Validated Designs (AVD), CloudVision Portal (CVP), and EVE-NG.

---

## Architecture Overview

```
                          DC1                                          DC2
┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│          dc1-spine1 / dc1-spine2         │    │          dc2-spine1 / dc2-spine2         │
│              AS 65100                    │    │              AS 65200                    │
└──────┬──────────┬──────────┬─────────────┘    └──────┬──────────┬──────────┬─────────────┘
       │          │          │                         │          │          │
  ┌────┴───┐ ┌────┴───┐ ┌────┴──────────┐        ┌────┴───┐ ┌────┴───┐ ┌────┴──────────┐
  │ LEAF1  │ │ LEAF2  │ │ BORDER LEAF1  │◄──DCI──►│ LEAF1  │ │ LEAF2  │ │ BORDER LEAF1  │
  │AS65101 │ │AS65102 │ │   AS 65103    │        │AS65201 │ │AS65202 │ │   AS 65203    │
  │MLAG    │ │MLAG    │ │MLAG+EVPN GW  │        │MLAG    │ │MLAG    │ │MLAG+EVPN GW  │
  └────┬───┘ └────┬───┘ └────┬──────────┘        └────┬───┘ └────┴───┘ └───────────────┘
       │          │          │
  ┌────┴───┐ ┌────┴───┐  ┌───┴───┐
  │LEAF1C  │ │LEAF2C  │  │  FW   │ mills-avd-fw
  │L2 Leaf │ │L2 Leaf │  │AS65500│ (vEOS simulated)
  └────────┘ └────────┘  └───────┘
```

---

## Design Details

### Underlay
- **Protocol:** eBGP point-to-point
- **MTU:** 1500 (vEOS-lab in EVE-NG)
- **P2P Links:** `/31` subnets from `10.255.255.0/26` (DC1) and `10.255.255.64/26` (DC2)

### Overlay
- **Protocol:** EVPN over eBGP
- **VTEP Loopbacks:** `10.255.1.0/27` (DC1) and `10.255.129.0/27` (DC2)
- **Router Loopbacks:** `10.255.0.0/27` (DC1) and `10.255.128.0/27` (DC2)

### DCI (Data Center Interconnect)
- **Links:** Ethernet4 on border leafs
- **DC1 Border Leaf1a ↔ DC2 Border Leaf1a:** `172.100.100.0/31`
- **DC1 Border Leaf1b ↔ DC2 Border Leaf1b:** `172.100.100.2/31`
- **EVPN GW:** Border leafs act as EVPN Gateways for inter-DC L2/L3 routing

### Firewall (Simulated)
- **Device:** mills-avd-fw (vEOS-lab)
- **Connection:** MLAG bond to DC1 border leafs (Port-Channel5 ↔ Port-Channel1)
- **VRF10 Transit:** VLAN 3901, `10.255.251.0/29`
- **VRF11 Transit:** VLAN 3902, `10.255.252.0/29`
- **BGP AS:** 65500 (eBGP with DC1 border leafs)
- **Function:** Inter-VRF routing between VRF10 and VRF11

---

## Device Inventory

### DC1

| Hostname | Role | Mgmt IP | BGP AS |
|----------|------|---------|--------|
| dc1-spine1 | Spine | 192.168.4.120/22 | 65100 |
| dc1-spine2 | Spine | 192.168.4.121/22 | 65100 |
| dc1-leaf1a | L3 Leaf | 192.168.4.122/22 | 65101 |
| dc1-leaf1b | L3 Leaf | 192.168.4.123/22 | 65101 |
| dc1-leaf1c | L2 Leaf | 192.168.4.124/22 | N/A |
| dc1-leaf2a | L3 Leaf | 192.168.4.126/22 | 65102 |
| dc1-leaf2b | L3 Leaf | 192.168.4.127/22 | 65102 |
| dc1-leaf2c | L2 Leaf | 192.168.4.128/22 | N/A |
| dc1-border-leaf1a | Border Leaf + EVPN GW | 192.168.4.140/22 | 65103 |
| dc1-border-leaf1b | Border Leaf + EVPN GW | 192.168.4.141/22 | 65103 |

### DC2

| Hostname | Role | Mgmt IP | BGP AS |
|----------|------|---------|--------|
| dc2-spine1 | Spine | 192.168.4.130/22 | 65200 |
| dc2-spine2 | Spine | 192.168.4.131/22 | 65200 |
| dc2-leaf1a | L3 Leaf | 192.168.4.132/22 | 65201 |
| dc2-leaf1b | L3 Leaf | 192.168.4.133/22 | 65201 |
| dc2-leaf1c | L2 Leaf | 192.168.4.134/22 | N/A |
| dc2-leaf2a | L3 Leaf | 192.168.4.136/22 | 65202 |
| dc2-leaf2b | L3 Leaf | 192.168.4.137/22 | 65202 |
| dc2-leaf2c | L2 Leaf | 192.168.4.138/22 | N/A |
| dc2-border-leaf1a | Border Leaf + EVPN GW | 192.168.4.142/22 | 65203 |
| dc2-border-leaf1b | Border Leaf + EVPN GW | 192.168.4.143/22 | 65203 |

### Infrastructure

| Hostname | Role | IP |
|----------|------|----|
| mills-cvp | CloudVision Portal 2026.1.0 | 192.168.4.165/22 |
| mills-avd-fw | vEOS Simulated Firewall | 192.168.4.144/22 |
| mills-ubuntu | Ansible Controller (Ubuntu 24.04) | 192.168.4.208/22 |

### Servers (vEOS)

| Hostname | Mgmt IP | Data IP | VLAN | VRF |
|----------|---------|---------|------|-----|
| dc1-leaf1-server1 | 192.168.4.125/22 | 10.10.11.10/24 | 11 | VRF10 |
| dc1-leaf2-server1 | 192.168.4.129/22 | 10.10.21.10/24 | 21 | VRF11 |
| dc2-leaf1-server1 | 192.168.4.135/22 | 10.10.11.20/24 | 11 | VRF10 |
| dc2-leaf2-server1 | 192.168.4.139/22 | 10.10.21.20/24 | 21 | VRF11 |

---

## Network Services

### Tenant: TENANT1

| VRF | VLAN | Name | Subnet | Gateway |
|-----|------|------|--------|---------|
| VRF10 | 11 | VRF10_VLAN11 | 10.10.11.0/24 | 10.10.11.1 |
| VRF10 | 12 | VRF10_VLAN12 | 10.10.12.0/24 | 10.10.12.1 |
| VRF10 | 3901 | VRF10_FW_TRANSIT | 10.255.251.0/29 | 10.255.251.1 |
| VRF11 | 21 | VRF11_VLAN21 | 10.10.21.0/24 | 10.10.21.1 |
| VRF11 | 22 | VRF11_VLAN22 | 10.10.22.0/24 | 10.10.22.1 |
| VRF11 | 3902 | VRF11_FW_TRANSIT | 10.255.252.0/29 | 10.255.252.1 |
| N/A | 3401 | L2_VLAN3401 | L2 only | N/A |
| N/A | 3402 | L2_VLAN3402 | L2 only | N/A |

### Inter-VRF Routing via Firewall

Static routes on DC1 border leafs route inter-VRF traffic through the firewall:

| Device | VRF | Destination | Next Hop |
|--------|-----|-------------|----------|
| dc1-border-leaf1a/1b | VRF10 | 10.10.21.0/24 | 10.255.251.2 (FW) |
| dc1-border-leaf1a/1b | VRF10 | 10.10.22.0/24 | 10.255.251.2 (FW) |
| dc1-border-leaf1a/1b | VRF11 | 10.10.11.0/24 | 10.255.252.2 (FW) |
| dc1-border-leaf1a/1b | VRF11 | 10.10.12.0/24 | 10.255.252.2 (FW) |

---

## Toolchain

| Tool | Version | Location | Purpose |
|------|---------|----------|---------|
| AVD | 6.1.0 | Mac + Linux VM | Config generation |
| pyavd | 6.1.0 | Mac + Linux VM | Python AVD library |
| ansible-core | 2.20.4 | Mac + Linux VM | Playbook execution |
| arista.eos | 12.0.1 | Linux VM | EOS modules |
| ansible.netcommon | 8.4.0 | Linux VM | Network modules |
| EOS | 4.35.1F | All fabric switches | Network OS |
| CVP | 2026.1.0 | mills-cvp | Automation platform |
| EVE-NG | - | Hypervisor | Lab virtualization |
| GitKraken | - | Mac | Git management |
| VS Code | - | Mac (Remote SSH) | Config authoring |

---

## Automation Workflow

### Daily Workflow

```
Mac (VS Code Remote SSH → Linux VM)
  │
  ├── Edit group_vars/
  ├── ansible-playbook build.yml    (generate configs)
  └── Commit + Push (GitKraken)
            │
            ▼
         GitHub
            │
            ▼
  Linux VM (192.168.4.208)
  ├── git pull
  ├── ansible-playbook deploy-cvp.yml
  ├── Approve Change Control in CVP
  └── ansible-playbook full-compliance-check.yml
```

### Playbooks

| Playbook | Description |
|----------|-------------|
| `build.yml` | Generate configs and documentation from group_vars |
| `deploy-cvp.yml` | Deploy configs to fabric via CVP Change Control |
| `deploy.yml` | Deploy configs direct via eAPI (no CVP) |
| `validate.yml` | Run ANTA validation only |
| `full-compliance-check.yml` | Build + CVP compliance + ANTA validation |
| `post-change-validation.yml` | Compare startup vs running config |
| `push-bootstrap.yml` | Push bootstrap configs to fabric switches |
| `push-server-configs.yml` | Push configs to vEOS servers direct via eAPI |
| `re-register-cvp.yml` | Re-register all devices with CVP |
| `reset-to-bootstrap.yml` | Wipe all configs (requires 'yes' confirmation) |

### Full Reset Workflow

```
1. ansible-playbook reset-to-bootstrap.yml    # wipe configs (requires 'yes')
2. Manual decommission in CVP UI              # human safety gate
3. ansible-playbook re-register-cvp.yml       # re-register with CVP
4. ansible-playbook deploy-cvp.yml            # restore fabric via Change Control
5. Approve Change Control in CVP              # human approval gate
6. ansible-playbook push-server-configs.yml   # restore servers
```

---

## Repository Structure

```
my-homelab/
├── group_vars/
│   ├── CONNECTED_ENDPOINTS/connected_endpoints.yml   # Server and FW endpoints
│   ├── DC1/dc1.yml                                   # DC1 fabric settings
│   ├── DC1_L2_LEAVES/l2_leaves.yml                   # DC1 L2 leaf config
│   ├── DC1_L3_LEAVES/l3_leaves.yml                   # DC1 L3 + border leafs
│   ├── DC1_SPINES/spines.yml                         # DC1 spine config
│   ├── DC2/dc2.yml                                   # DC2 fabric settings
│   ├── DC2_L2_LEAVES/l2_leaves.yml                   # DC2 L2 leaf config
│   ├── DC2_L3_LEAVES/l3_leaves.yml                   # DC2 L3 + border leafs
│   ├── DC2_SPINES/spines.yml                         # DC2 spine config
│   ├── FABRIC/fabric_ansible_connectivity.yml        # CVP + eAPI connectivity
│   ├── FABRIC/fabric_variables.yml                   # Global fabric variables + DCI
│   └── NETWORK_SERVICES/network_services.yml         # VRFs, VLANs, SVIs, FW transit
├── switch-basic-configurations/                      # Bootstrap configs for all devices
├── server-configurations/                            # Full vEOS server configs
├── intended/configs/                                 # AVD generated EOS configs
├── intended/structured_configs/                      # AVD structured YAML configs
├── documentation/                                    # AVD generated documentation
├── anta/                                             # ANTA catalogs and reports
├── inventory.yml                                     # Ansible inventory
├── ansible.cfg                                       # Ansible configuration
├── build.yml                                         # Build playbook
├── deploy-cvp.yml                                    # CVP deploy playbook
├── deploy.yml                                        # eAPI deploy playbook
├── validate.yml                                      # ANTA validation playbook
├── full-compliance-check.yml                         # Full compliance playbook
├── post-change-validation.yml                        # Post change validation
├── push-bootstrap.yml                                # Bootstrap push playbook
├── push-server-configs.yml                           # Server config push playbook
├── re-register-cvp.yml                               # CVP re-registration playbook
└── reset-to-bootstrap.yml                            # Full reset playbook
```

---

## Credentials

| System | Username | Password |
|--------|----------|---------|
| All EOS devices | cvpadmin | cetest.123 |
| CVP | cvpadmin | cetest.123 |
| Linux VM | adolan | - |

**CVP API Token:** Stored in `~/.cvp_token` on both Mac and Linux VM. Never committed to git.

---

## Linux Ansible Controller Setup

```bash
# Prerequisites
sudo apt update && sudo apt install python3 python3-pip python3-venv git -y

# Create venv
mkdir -p ~/avd-projects
python3 -m venv ~/avd-projects/avd-venv
source ~/avd-projects/avd-venv/bin/activate

# Install AVD
pip install "pyavd[ansible-collection]==6.1.0"
ansible-galaxy collection install arista.avd:==6.1.0

# Clone repo
git clone git@github.com:rraidernc/avd-homelab.git ~/avd-projects/my-homelab

# Copy CVP token
scp ~/.cvp_token adolan@192.168.4.208:~/.cvp_token

# Auto-activate venv on login
echo 'source ~/avd-projects/avd-venv/bin/activate' >> ~/.bashrc
echo 'cd ~/avd-projects/my-homelab' >> ~/.bashrc
```

---

## CVP Notes

- CVP 2026.1.0 uses Studios-based management (no classic containers/configlets)
- Device onboarding requires IP addresses — hostname DNS uses internal K8s resolver
- All 24 device hostnames added to `/etc/hosts` on CVP
- API token generated from Service Accounts (not user profile)
- NRFU Dashboard imported from `exported-dashboards-*.json`

---

## NTP / DNS

- **NTP Server:** 192.168.4.250
- **Management Gateway:** 192.168.4.1
- **Management Subnet:** 192.168.4.0/22
