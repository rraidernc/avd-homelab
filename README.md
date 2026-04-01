# AVD Home Lab Build Summary
**Date:** March 29-30, 2026  
**Engineer:** Alex Mills  

---

## 🎉 What You Built

### Infrastructure
- ✅ Mac configured as Ansible controller with AVD 5.7.2
- ✅ Python venv with all dependencies
- ✅ VS Code configured for AVD development

### Fabric — Dual DC L3LS EVPN/VXLAN
- ✅ DC1 — Single DC L3LS EVPN/VXLAN (Day 1)
- ✅ DC2 — Extended to Dual DC with EVPN GW and DCI (Day 2)
- ✅ 2 spine switches per DC (DC1: AS 65100, DC2: AS 65200)
- ✅ 2 x MLAG L3 leaf pairs per DC
- ✅ 2 x L2 access leaves per DC
- ✅ DCI links between dc1-leaf2a/2b ↔ dc2-leaf2a/2b (Ethernet6)
- ✅ EVPN DC Gateway on dc1-leaf2a/2b and dc2-leaf2a/2b
- ✅ VLANs stretched across both DCs

### Automation
- ✅ All group_vars customized for your lab
- ✅ `build.yml` — generates configs locally
- ✅ `deploy-cvp.yml` — deploys via CVP Change Control
- ✅ `validate.yml` — ANTA fabric validation
- ✅ Bootstrap configs for all devices

### CloudVision
- ✅ CVP 2025.3.1 (on-prem OVA) — mills-cvp
- ✅ All 16 devices registered and streaming
- ✅ Change Controls deployed successfully
- ✅ EOS upgraded to 4.35.1F

---

## ⚠️ Important — CVP 2025.x Studios-Based Workflow

**CVP 2025.3.1 has removed the classic container, configlet, and provisioning workflows.**
Everything is now Studios-based.

| | Pre-2025.x (Classic) | 2025.x (Studios) |
|--|---------------------|-----------------|
| Config delivery | Configlets | Studios API |
| Device organization | Containers | Studios |
| Change Control | ✅ Still exists | ✅ Still exists |
| AVD integration | cv_deploy via configlets | cv_deploy via Studios API |

**AVD still works as the source of truth** — the `cv_deploy` role has been updated to work with the Studios API. The Change Control workflow remains intact. You just won't see configlets or containers in the CVP UI anymore.

---

## Device Inventory — DC1

| Hostname | Role | Mgmt IP | BGP AS |
|----------|------|---------|--------|
| dc1-spine1 | Spine | 192.168.4.120/22 | 65100 |
| dc1-spine2 | Spine | 192.168.4.121/22 | 65100 |
| dc1-leaf1a | L3 Leaf | 192.168.4.122/22 | 65101 |
| dc1-leaf1b | L3 Leaf | 192.168.4.123/22 | 65101 |
| dc1-leaf1c | L2 Leaf | 192.168.4.124/22 | N/A |
| dc1-leaf2a | L3 Leaf + EVPN GW | 192.168.4.126/22 | 65102 |
| dc1-leaf2b | L3 Leaf + EVPN GW | 192.168.4.127/22 | 65102 |
| dc1-leaf2c | L2 Leaf | 192.168.4.128/22 | N/A |
| dc1-leaf1-server1 | Server (vEOS) | 192.168.4.125/22 | N/A |
| dc1-leaf2-server1 | Server (vEOS) | 192.168.4.129/22 | N/A |

## Device Inventory — DC2

| Hostname | Role | Mgmt IP | BGP AS |
|----------|------|---------|--------|
| dc2-spine1 | Spine | 192.168.4.130/22 | 65200 |
| dc2-spine2 | Spine | 192.168.4.131/22 | 65200 |
| dc2-leaf1a | L3 Leaf | 192.168.4.132/22 | 65201 |
| dc2-leaf1b | L3 Leaf | 192.168.4.133/22 | 65201 |
| dc2-leaf1c | L2 Leaf | 192.168.4.134/22 | N/A |
| dc2-leaf2a | L3 Leaf + EVPN GW | 192.168.4.136/22 | 65202 |
| dc2-leaf2b | L3 Leaf + EVPN GW | 192.168.4.137/22 | 65202 |
| dc2-leaf2c | L2 Leaf | 192.168.4.138/22 | N/A |
| dc2-leaf1-server1 | Server (vEOS) | 192.168.4.135/22 | N/A |
| dc2-leaf2-server1 | Server (vEOS) | 192.168.4.139/22 | N/A |

## Infrastructure

| Hostname | Role | IP |
|----------|------|----|
| mills-cvp | CloudVision 2025.3.1 | 192.168.4.165/22 |

---

## DCI — Data Center Interconnect

| Link | DC1 Device | DC1 Interface | DC2 Device | DC2 Interface | IP Pool |
|------|-----------|---------------|-----------|---------------|---------|
| DCI-1 | dc1-leaf2a | Ethernet6 | dc2-leaf2a | Ethernet6 | 172.100.100.0/31 |
| DCI-2 | dc1-leaf2b | Ethernet6 | dc2-leaf2b | Ethernet6 | 172.100.100.2/31 |

---

## Network Services

| Tenant | VRF | VLAN | Subnet | Gateway |
|--------|-----|------|--------|---------|
| TENANT1 | VRF10 | 11 | 10.10.11.0/24 | 10.10.11.1 |
| TENANT1 | VRF10 | 12 | 10.10.12.0/24 | 10.10.12.1 |
| TENANT1 | VRF11 | 21 | 10.10.21.0/24 | 10.10.21.1 |
| TENANT1 | VRF11 | 22 | 10.10.22.0/24 | 10.10.22.1 |
| TENANT1 | N/A | 3401 | L2 only | N/A |
| TENANT1 | N/A | 3402 | L2 only | N/A |

---

## Server Configs — DC1

| Server | Mgmt IP | Data IP | VLAN | Gateway |
|--------|---------|---------|------|---------|
| dc1-leaf1-server1 | 192.168.4.125/22 | 10.10.11.10/24 | 11 (VRF10) | 10.10.11.1 |
| dc1-leaf2-server1 | 192.168.4.129/22 | 10.10.21.10/24 | 21 (VRF11) | 10.10.21.1 |

---

## Credentials

| Account | Username | Password | Purpose |
|---------|----------|----------|---------|
| EOS devices | cvpadmin | cetest.123 | Ansible + management |
| CloudVision | cvpadmin | cetest.123 | UI + API access |

---

## Key File Locations

| File | Location |
|------|----------|
| Project root | `~/avd-projects/my-homelab/` |
| Python venv | `~/avd-projects/avd-venv/` |
| Inventory | `~/avd-projects/my-homelab/inventory.yml` |
| Group vars | `~/avd-projects/my-homelab/group_vars/` |
| Generated configs | `~/avd-projects/my-homelab/intended/configs/` |
| ANTA reports | `~/avd-projects/my-homelab/anta/reports/` |
| Bootstrap configs | `~/avd-projects/my-homelab/switch-basic-configurations/` |

---

## Group Vars Structure

```
group_vars/
├── CONNECTED_ENDPOINTS/connected_endpoints.yml
├── DC1/dc1.yml
├── DC1_L2_LEAVES/l2_leaves.yml
├── DC1_L3_LEAVES/l3_leaves.yml       ← includes EVPN GW on leaf2a/2b
├── DC1_SPINES/spines.yml
├── DC2/dc2.yml
├── DC2_L2_LEAVES/l2_leaves.yml
├── DC2_L3_LEAVES/l3_leaves.yml       ← includes EVPN GW on leaf2a/2b
├── DC2_SPINES/spines.yml
├── FABRIC/fabric_ansible_connectivity.yml
├── FABRIC/fabric_variables.yml        ← includes DCI l3_edge links
└── NETWORK_SERVICES/network_services.yml
```

---

## Daily Workflow

```bash
# Activate venv
source ~/avd-projects/avd-venv/bin/activate
cd ~/avd-projects/my-homelab

# Fix macOS fork issue (if not already in ~/.zshrc)
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

# Build configs
ansible-playbook build.yml

# Deploy via CVP
ansible-playbook deploy-cvp.yml

# Validate fabric
ansible-playbook validate.yml

# Save configs across all devices
ansible FABRIC -i inventory.yml \
  -m arista.eos.eos_command \
  -a "commands='write memory'" \
  -e "ansible_user=cvpadmin" \
  -e "ansible_password=cetest.123" \
  -e "ansible_become=true" \
  -e "ansible_become_method=enable" \
  -e "ansible_httpapi_use_ssl=true" \
  -e "ansible_httpapi_validate_certs=false" \
  -e "ansible_network_os=arista.eos.eos" \
  -e "ansible_connection=ansible.netcommon.httpapi"
```

---

## BGP ASN Design

```
DC1:
  Spines:    AS 65100
  DC1-LEAF1: AS 65101 (dc1-leaf1a, dc1-leaf1b)
  DC1-LEAF2: AS 65102 (dc1-leaf2a, dc1-leaf2b) ← EVPN GW

DC2:
  Spines:    AS 65200
  DC2-LEAF1: AS 65201 (dc2-leaf1a, dc2-leaf1b)
  DC2-LEAF2: AS 65202 (dc2-leaf2a, dc2-leaf2b) ← EVPN GW
```

---

## Next Steps
- [ ] Verify EVPN GW sessions between DC1 and DC2 border leafs
- [ ] Test inter-DC server-to-server ping across VXLAN fabric
- [ ] Run `validate.yml` across full dual-DC fabric
- [ ] Run `write memory` across all 16 devices
- [ ] Build DC2 server configs (dc2-leaf1-server1, dc2-leaf2-server1)
- [ ] Explore CVP Studios telemetry and topology views
- [ ] Try making a fabric change via AVD and deploying through Change Control
