# AVD Home Lab — Dual DC L3LS EVPN/VXLAN Fabric
**Engineer:** Alex Mills  
**Built:** March 29-30, 2026  
**Platform:** EVE-NG + CloudVision Portal 2025.3.1 + AVD 5.7.2

---

## 🏗️ Fabric Overview

A fully automated dual data center L3LS EVPN/VXLAN fabric built using Arista Validated Design (AVD) with CloudVision Portal as the deployment and telemetry platform.

```
DC1                                    DC2
┌─────────────────────┐               ┌─────────────────────┐
│  dc1-spine1/spine2  │               │  dc2-spine1/spine2  │
│     AS 65100        │               │     AS 65200        │
└────────┬────────────┘               └────────┬────────────┘
         │                                     │
┌────────┴────────────┐               ┌────────┴────────────┐
│  dc1-leaf1a/leaf1b  │               │  dc2-leaf1a/leaf1b  │
│  MLAG  AS 65101     │               │  MLAG  AS 65201     │
│  dc1-leaf1c (L2)    │               │  dc2-leaf1c (L2)    │
├─────────────────────┤               ├─────────────────────┤
│  dc1-leaf2a/leaf2b  │◄──── DCI ────►│  dc2-leaf2a/leaf2b  │
│  MLAG  AS 65102     │  Et6↔Et6      │  MLAG  AS 65202     │
│  EVPN GW            │               │  EVPN GW            │
│  dc1-leaf2c (L2)    │               │  dc2-leaf2c (L2)    │
└─────────────────────┘               └─────────────────────┘
```

---

## 📋 Device Inventory

### DC1
| Hostname | Role | Mgmt IP | BGP AS |
|----------|------|---------|--------|
| dc1-spine1 | Spine | 192.168.4.120/22 | 65100 |
| dc1-spine2 | Spine | 192.168.4.121/22 | 65100 |
| dc1-leaf1a | L3 Leaf (MLAG) | 192.168.4.122/22 | 65101 |
| dc1-leaf1b | L3 Leaf (MLAG) | 192.168.4.123/22 | 65101 |
| dc1-leaf1c | L2 Leaf | 192.168.4.124/22 | N/A |
| dc1-leaf2a | L3 Leaf + EVPN GW | 192.168.4.126/22 | 65102 |
| dc1-leaf2b | L3 Leaf + EVPN GW | 192.168.4.127/22 | 65102 |
| dc1-leaf2c | L2 Leaf | 192.168.4.128/22 | N/A |
| dc1-leaf1-server1 | Server (vEOS) | 192.168.4.125/22 | N/A |
| dc1-leaf2-server1 | Server (vEOS) | 192.168.4.129/22 | N/A |

### DC2
| Hostname | Role | Mgmt IP | BGP AS |
|----------|------|---------|--------|
| dc2-spine1 | Spine | 192.168.4.130/22 | 65200 |
| dc2-spine2 | Spine | 192.168.4.131/22 | 65200 |
| dc2-leaf1a | L3 Leaf (MLAG) | 192.168.4.132/22 | 65201 |
| dc2-leaf1b | L3 Leaf (MLAG) | 192.168.4.133/22 | 65201 |
| dc2-leaf1c | L2 Leaf | 192.168.4.134/22 | N/A |
| dc2-leaf2a | L3 Leaf + EVPN GW | 192.168.4.136/22 | 65202 |
| dc2-leaf2b | L3 Leaf + EVPN GW | 192.168.4.137/22 | 65202 |
| dc2-leaf2c | L2 Leaf | 192.168.4.138/22 | N/A |
| dc2-leaf1-server1 | Server (vEOS) | 192.168.4.135/22 | N/A |
| dc2-leaf2-server1 | Server (vEOS) | 192.168.4.139/22 | N/A |

### Infrastructure
| Hostname | Role | IP |
|----------|------|----|
| mills-cvp | CloudVision 2025.3.1 | 192.168.4.165/22 |

---

## 🌐 Network Services

| Tenant | VRF | VLAN | Subnet | Gateway |
|--------|-----|------|--------|---------|
| TENANT1 | VRF10 | 11 | 10.10.11.0/24 | 10.10.11.1 |
| TENANT1 | VRF10 | 12 | 10.10.12.0/24 | 10.10.12.1 |
| TENANT1 | VRF11 | 21 | 10.10.21.0/24 | 10.10.21.1 |
| TENANT1 | VRF11 | 22 | 10.10.22.0/24 | 10.10.22.1 |
| TENANT1 | N/A | 3401/3402 | L2 only | N/A |

All VLANs stretched across both DCs via EVPN/VXLAN.

---

## 🔗 DCI — Data Center Interconnect

| Link | DC1 Device | Interface | DC2 Device | Interface | Subnet |
|------|-----------|-----------|-----------|-----------|--------|
| DCI-1 | dc1-leaf2a | Ethernet6 | dc2-leaf2a | Ethernet6 | 172.100.100.0/31 |
| DCI-2 | dc1-leaf2b | Ethernet6 | dc2-leaf2b | Ethernet6 | 172.100.100.2/31 |

---

## 🗂️ Repository Structure

```
my-homelab/
├── group_vars/
│   ├── CONNECTED_ENDPOINTS/    # Server port definitions
│   ├── DC1/                    # DC1 management settings
│   ├── DC1_L2_LEAVES/          # DC1 L2 leaf definitions
│   ├── DC1_L3_LEAVES/          # DC1 L3 leaf + EVPN GW definitions
│   ├── DC1_SPINES/             # DC1 spine definitions
│   ├── DC2/                    # DC2 management settings
│   ├── DC2_L2_LEAVES/          # DC2 L2 leaf definitions
│   ├── DC2_L3_LEAVES/          # DC2 L3 leaf + EVPN GW definitions
│   ├── DC2_SPINES/             # DC2 spine definitions
│   ├── FABRIC/                 # Fabric-wide settings + DCI l3_edge
│   └── NETWORK_SERVICES/       # VRFs, VLANs, SVIs
├── documentation/              # Auto-generated fabric documentation
├── intended/                   # Auto-generated device configs
├── anta/                       # ANTA validation catalogs and reports
├── server-configurations/      # vEOS server bootstrap configs
├── switch-basic-configurations/ # Switch bootstrap configs
├── build.yml                   # Generate configs from group_vars
├── deploy-cvp.yml              # Deploy via CVP Change Control
├── deploy.yml                  # Deploy direct via eAPI
├── validate.yml                # ANTA fabric validation
├── full-compliance-check.yml   # Full end-to-end compliance check
├── post-change-validation.yml  # Post change control validation
├── push-bootstrap.yml          # Push bootstrap configs to switches
├── push-server-configs.yml     # Push configs to vEOS servers
└── inventory.yml               # Ansible inventory
```

---

## ⚙️ Environment Setup

```bash
# Activate Python virtual environment
source ~/avd-projects/avd-venv/bin/activate
cd ~/avd-projects/my-homelab

# Verify AVD version
ansible-galaxy collection list | grep avd
```

**Toolchain:**
- AVD 5.7.2
- ansible-core 2.18.x
- Python 3.13
- pyavd 5.7.2

---

## 🔄 Daily Workflow

### Standard Change Deployment
```bash
# 1. Edit group_vars (source of truth)
# 2. Generate intended configs
ansible-playbook build.yml

# 3. Review generated configs
cat intended/configs/<device>.cfg

# 4. Deploy via CVP Change Control
ansible-playbook deploy-cvp.yml

# 5. Approve Change Control in CVP UI

# 6. Verify compliance
ansible-playbook full-compliance-check.yml
```

### Full Compliance Check (post-change)
```bash
ansible-playbook full-compliance-check.yml
```
This single command:
- Regenerates intended configs from group_vars
- Checks CVP compliance (no Change Control = compliant)
- Runs full ANTA fabric validation

### ANTA Validation Only
```bash
ansible-playbook validate.yml
```

### Save configs across all devices
```bash
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

## 📊 Compliance Levels

| Level | What it checks | Tool |
|-------|---------------|------|
| startup vs running | Did the device save after the change? | `post-change-validation.yml` |
| CVP vs running | Does CVP's intended config match the device? | CVP Compliance Overview |
| AVD repo vs running | Does group_vars match what's deployed? | `full-compliance-check.yml` |

---

## ⚠️ CVP 2025.x Studios Workflow

CVP 2025.3.1 removed classic containers, configlets and provisioning workflows. Everything is now Studios-based.

| | Pre-2025.x | 2025.x |
|--|------------|--------|
| Config delivery | Configlets | Studios API |
| Device organization | Containers | Studios |
| Change Control | ✅ | ✅ |
| AVD integration | cv_deploy via configlets | cv_deploy via Studios API |

AVD remains the source of truth — the `cv_deploy` role has been updated to work with the Studios API.

---

## 🔐 Credentials & Security

| Account | Username | Purpose |
|---------|----------|---------|
| EOS devices | cvpadmin | Ansible + management |
| CloudVision | cvpadmin | UI + API access |

**CVP API Token:** Stored in `~/.cvp_token` (outside repo, never committed to Git)

---

## 🖥️ macOS Notes

```bash
# Fork safety fix (already in ~/.zshrc)
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

# Verify it's set
echo $OBJC_DISABLE_INITIALIZE_FORK_SAFETY
```

---

## 📈 Validation Results

| Category | Tests | Result |
|----------|-------|--------|
| BGP | ✅ | 100% pass |
| VXLAN | ✅ | 100% pass |
| Connectivity | ✅ | 100% pass |
| System | ✅ | 100% pass |
| MLAG | ✅ | 100% pass |
| STP | ✅ | 100% pass |
| Routing | ✅ | 100% pass |
| Hardware | ⏭️ | Skipped (vEOS-lab) |

---

## 🚀 Production Considerations

To extend this to a production environment:

- **CI/CD Pipeline** — GitHub Actions triggering `build.yml` on pull requests
- **Branch Strategy** — feature branches for changes, main = production
- **Secrets Management** — HashiCorp Vault instead of `~/.cvp_token`
- **Multi-environment** — dev/staging/prod fabric definitions
- **Automated Testing** — ANTA runs as part of CI pipeline before merge
- **Peer Review** — all `group_vars` changes reviewed via pull requests

# NOTE: Upgrade to Ansible AVD version 6.1.0 has been completed. 
