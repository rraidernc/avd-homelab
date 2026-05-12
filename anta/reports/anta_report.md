# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 472 | 441 | 0 | 31 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **dc1-border-leaf1a** | 26 | 23 | 0 | 3 | 0 | - | Configuration, Logging, System |
| **dc1-border-leaf1b** | 26 | 25 | 0 | 1 | 0 | - | Logging |
| **dc1-leaf1a** | 26 | 26 | 0 | 0 | 0 | - | - |
| **dc1-leaf1b** | 26 | 23 | 0 | 3 | 0 | - | Configuration, Logging, System |
| **dc1-leaf1c** | 20 | 18 | 0 | 2 | 0 | - | Configuration, System |
| **dc1-leaf2a** | 26 | 25 | 0 | 1 | 0 | - | Logging |
| **dc1-leaf2b** | 26 | 25 | 0 | 1 | 0 | - | Logging |
| **dc1-leaf2c** | 20 | 20 | 0 | 0 | 0 | - | - |
| **dc1-spine1** | 20 | 19 | 0 | 1 | 0 | - | Logging |
| **dc1-spine2** | 20 | 17 | 0 | 3 | 0 | - | Configuration, Logging, System |
| **dc2-border-leaf1a** | 26 | 25 | 0 | 1 | 0 | - | Logging |
| **dc2-border-leaf1b** | 26 | 23 | 0 | 3 | 0 | - | Configuration, Logging, System |
| **dc2-leaf1a** | 26 | 24 | 0 | 2 | 0 | - | Configuration, System |
| **dc2-leaf1b** | 26 | 24 | 0 | 2 | 0 | - | Configuration, System |
| **dc2-leaf1c** | 20 | 18 | 0 | 2 | 0 | - | Configuration, System |
| **dc2-leaf2a** | 26 | 24 | 0 | 2 | 0 | - | Configuration, System |
| **dc2-leaf2b** | 26 | 26 | 0 | 0 | 0 | - | - |
| **dc2-leaf2c** | 20 | 18 | 0 | 2 | 0 | - | Configuration, System |
| **dc2-spine1** | 20 | 20 | 0 | 0 | 0 | - | - |
| **dc2-spine2** | 20 | 18 | 0 | 2 | 0 | - | Configuration, System |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **BGP** | 16 | 16 | 0 | 0 | 0 |
| **Configuration** | 40 | 29 | 0 | 11 | 0 |
| **Connectivity** | 36 | 36 | 0 | 0 | 0 |
| **Interfaces** | 132 | 132 | 0 | 0 | 0 |
| **Logging** | 20 | 11 | 0 | 9 | 0 |
| **MLAG** | 36 | 36 | 0 | 0 | 0 |
| **Routing** | 20 | 20 | 0 | 0 | 0 |
| **STP** | 20 | 20 | 0 | 0 | 0 |
| **System** | 140 | 129 | 0 | 11 | 0 |
| **VXLAN** | 12 | 12 | 0 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Result | Messages |
| :- | :- | :- | :- | :- | :- |
| dc1-border-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -248,7 +248,6 @@<br> ip route vrf VRF11 10.10.12.0/24 10.255.252.2<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc1-border-leaf1a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 03:00:07 dc1-border-leaf1a Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.0.1 (VRF default AS 65100) 6/7 (Cease/connection collision resolution) 0 bytes <br> May 12 03:01:12 dc1-border-leaf1a Bgp: %BGP-3-NOTIFICATION: received from neighbor 172.100.100.1 (VRF default AS 65203) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc1-border-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-border-leaf1b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 03:00:11 dc1-border-leaf1b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.128.8 (VRF default AS 65203) 6/7 (Cease/connection collision resolution) 0 bytes <br> May 12 06:24:16 dc1-border-leaf1b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.252.2 (VRF VRF11 AS 65500) 4/0 (Hold Timer Expired Error/None) 0 bytes<br> May 12 06:33:54 dc1-border-leaf1b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.251.2 (VRF VRF10 AS 65500) 4/0 (Hold Timer Expired Error/None) 0 bytes<br> May 12 10:24:36 dc1-border-leaf1b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.252.2 (VRF VRF11 AS 65500) 4/0 (Hold Timer Expired Error/None) 0 bytes<br> <br> |
| dc1-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -247,7 +247,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc1-leaf1b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 02:58:59 dc1-leaf1b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.255.4 (VRF default AS 65100) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc1-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf1c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -98,6 +98,5 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> end<br> |
| dc1-leaf1c | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf2a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 02:59:02 dc1-leaf2a Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.255.10 (VRF default AS 65100) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc1-leaf2b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 02:59:02 dc1-leaf2b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.255.14 (VRF default AS 65100) 6/5 (Cease/connection rejected) 0 bytes<br> May 12 02:59:02 dc1-leaf2b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.255.12 (VRF default AS 65100) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc1-spine1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 02:58:49 dc1-spine1 Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.0.7 (VRF default AS 65103) 6/7 (Cease/connection collision resolution) 0 bytes <br> May 12 02:58:59 dc1-spine1 Bgp: %BGP-3-NOTIFICATION: received from neighbor 10.255.255.5 (VRF default AS 65101) 6/5 (Cease/connection rejected) 0 bytes<br> May 12 02:59:02 dc1-spine1 Bgp: %BGP-3-NOTIFICATION: received from neighbor 10.255.255.13 (VRF default AS 65102) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc1-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -93,7 +93,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc1-spine2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 02:59:02 dc1-spine2 Bgp: %BGP-3-NOTIFICATION: received from neighbor 10.255.255.15 (VRF default AS 65102) 6/5 (Cease/connection rejected) 0 bytes<br> May 12 02:59:02 dc1-spine2 Bgp: %BGP-3-NOTIFICATION: received from neighbor 10.255.255.11 (VRF default AS 65102) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc1-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-border-leaf1a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 02:59:53 dc2-border-leaf1a Bgp: %BGP-3-NOTIFICATION: sent to neighbor 172.100.100.0 (VRF default AS 65103) 6/5 (Cease/connection rejected) 0 bytes<br> <br> |
| dc2-border-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -233,7 +233,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc2-border-leaf1b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>May 12 03:00:10 dc2-border-leaf1b Bgp: %BGP-3-NOTIFICATION: sent to neighbor 10.255.0.8 (VRF default AS 65103) 6/7 (Cease/connection collision resolution) 0 bytes <br> <br> |
| dc2-border-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -247,7 +247,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc2-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -247,7 +247,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc2-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf1c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -98,6 +98,5 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> end<br> |
| dc2-leaf1c | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf2a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -247,7 +247,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc2-leaf2a | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf2c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -98,6 +98,5 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> end<br> |
| dc2-leaf2c | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ❌&nbsp;Failure | --- flash:/startup-config<br>+++ system:/running-config<br>@@ -93,7 +93,6 @@<br> ip route vrf MGMT 0.0.0.0/0 192.168.4.1<br> !<br> ntp local-interface vrf MGMT Management1<br>-ntp server vrf MGMT 192.168.4.250 prefer<br> !<br> route-map RM-CONN-2-BGP permit 10<br>    match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY<br> |
| dc2-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-border-leaf1a | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-border-leaf1a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-border-leaf1b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1a | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf1a | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-leaf1a | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc1-leaf1a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf1a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc1-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf1a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1b | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf1b | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-leaf1b | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf1b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf1b | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf1b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf1c | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-leaf1c | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1c | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc1-leaf1c | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf1c | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf1c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf1c | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf1c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf1c | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf1c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf1c | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf2a | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf2a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf2a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf2a | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-leaf2a | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf2a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-leaf2a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf2a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf2a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc1-leaf2a | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf2b | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf2b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf2b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf2b | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-leaf2b | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf2b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-leaf2b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf2b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf2b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc1-leaf2b | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf2c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf2c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf2c | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-leaf2c | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2c | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc1-leaf2c | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf2c | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc1-leaf2c | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-spine1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-spine1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-spine1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-spine2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-spine2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-spine2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-border-leaf1a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-border-leaf1b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1a | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf1a | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf1a | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-leaf1a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf1a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf1a | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf1a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1b | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf1b | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf1b | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-leaf1b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf1b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf1b | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf1b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf1c | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf1c | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1c | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-leaf1c | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf1c | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf1c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf1c | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf1c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf1c | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf1c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf1c | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf2a | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf2a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf2a | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf2a | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-leaf2a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf2a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf2a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf2a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf2a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf2a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf2a | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf2a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf2a | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf2a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf2a | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf2b | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf2b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-leaf2b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf2b | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf2b | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-leaf2b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf2b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf2b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf2b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf2b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc2-leaf2b | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf2c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf2c | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf2c | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2c | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-leaf2c | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf2c | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf2c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf2c | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf2c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf2c | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf2c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf2c | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-spine1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-spine1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-spine1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-spine1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-spine2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-spine2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-spine2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ✅&nbsp;Success | - |
| dc2-spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-spine2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
