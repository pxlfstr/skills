# Multi-gig copper negotiation — 2.5GBASE-T falling back to 1G

Why a 2.5G NIC on a 2.5G switch links at 1 Gb/s, how to turn a silent
fallback into a definite answer, and an unresolved case kept as a worked
example. Relevant to the IP-video pillar: NDI and ST 2110 bandwidth budgets
assume the link rate you think you have.

## Provenance

**Compiled 2026-09-17 from one live troubleshooting session on the user's own
machines. The case in §5 was NOT resolved** — the decisive test was never
run, and this document does not state a root cause.

| Section | Tier |
|---|---|
| §1 downshift mechanism | **Verified [Forum]** as of 2026-09-17 — mechanism from a kernel mailing-list thread; property and default read off the user's machine |
| §2 forcing method | **Bench-verified** — the forced-rate test was performed and produced a result |
| §3 adapter facts | **Verified**, user-reported — PowerShell output pasted verbatim. §3.2 identifications **Verified** 2026-09-17 against PCI ID databases |
| §4 switch facts | **[Lead]** — retailer and distributor copy, not TP-Link's own documentation |
| §5 case record | Session transcript; **unresolved** |
| §6 2.5GBASE-T fragility | **[Lead]** — community lore, no standards document read |
| §7 corrections | Session transcript |

**Sources actually read this session:**

- PowerShell output from the user's Windows 11 server: `Get-NetAdapter`,
  `Get-NetAdapterAdvancedProperty` (full advanced-property list and the
  `Speed & Duplex` valid-value list), `Get-PnpDevice -Class Net`. **Pasted
  verbatim by the user — strongest tier in this document.**
- Retailer and distributor listings for the TP-Link TL-SG608S-M2 (Micro
  Center, Best Buy, and reseller copy), via search extracts.

**NOT read:** IEEE 802.3bz; any Marvell AQtion datasheet, driver release note
or firmware notice; TP-Link's own TL-SG608S-M2 datasheet or manual; any
Gigabyte motherboard manual or BIOS release note; the PCI ID repository.

**Verification pass run 2026-09-17**, same day, after the first draft. Sources
added: the Linux Kernel Driver DataBase (`CONFIG_AQTION`,
`CONFIG_NET_VENDOR_AQUANTIA`), DeviceHunt PCI vendor/device pages,
linux-hardware.org probe records, coreboot mailing-list archives (2007-05) and
an lspci capture for the Gigabyte subsystem ID, a Marvell AQtion driver
changelog reproduced on a third-party archive, and a Linux kernel mailing-list
thread on PHY downshift behaviour.

**Result: §3.2's three identifications are now Verified, and the AQC107
firmware-bug claim is RETRACTED** — a targeted search found nothing supporting
it. §1's mechanism moved from reasoned to sourced, and **the conclusion it
supports changed** (see §1.1 and §5).

⚠️ **Still unsourced:** IEEE 802.3bz itself, and therefore the four-pair
requirement for 2.5GBASE-T stated in §1.1.

---

## §1 — Downshift: the mechanism that hides the failure

Marvell AQtion drivers expose an advanced property **`Downshift retries`**,
default **4** on the adapter examined (§3.1). It is a documented driver
feature — see §3.2a for the changelog entry.

### §1.1 — What downshift actually does — **VERIFIED 2026-09-17**

Described on the Linux kernel mailing list, in a thread on a PHY whose
downshift was misbehaving. Paraphrasing the explanation given there: gigabit
operation requires all four pairs in the cable to work; **if a link
negotiates at 1 Gb/s and then fails to establish because a pair is broken,
some PHYs downshift** — dropping to 100 Mb/s, which needs only two working
pairs. Done correctly, the PHY also stops advertising the higher rate so the
link partner follows it down.

**This is the important part, and it reverses the session's framing.**
Downshift is not a vague "negotiation didn't work" fallback. It is
specifically **a response to a physically bad cable pair.** A PHY that
downshifts is telling you something about the copper.

Scale it up one tier: **2.5GBASE-T likewise uses all four pairs**, so the same
mechanism applies — a link that cannot hold 2.5G on a damaged pair drops to
1000BASE-T, which also uses four pairs but at a far lower symbol rate and with
correspondingly more margin.

⚠️ **Tier:** the quoted mechanism is [Forum] — a kernel mailing-list
discussion between developers, which is strong for mechanism and is not a
standards document. **IEEE 802.3bz was not read.** The four-pair requirement
for 2.5GBASE-T is stated here from general knowledge and is **not sourced**.

### §1.2 — Why it matters for video work

A link that silently self-demotes is worse than one that fails. An NDI or
ST 2110 bandwidth budget written against 2.5 Gb/s runs on 1 Gb/s, and the
discovery happens under load.

### §1.3 — The anomaly in the §5 case

⚠️ **On the adapter in §5, setting `Downshift retries` to `Disabled` did not
change the outcome — the link still came up at 1 Gb/s.**

Under §1.1's mechanism that is genuinely odd: with downshift off, a PHY that
cannot hold 2.5G should fail to link rather than quietly settle at 1 Gb/s.
Two readings, neither confirmed:

- The property did not take effect on the hardware, only in the driver.
- Something other than downshift is selecting 1 Gb/s.

**Both are consistent with the forced-rate result** (§2 — forcing 2.5G gave no
link at all), which does show the path refusing 2.5G. **Recorded as an open
anomaly, not resolved.**


---

## §2 — Forcing the rate turns a silent fallback into a pass/fail

**The transferable technique in this document. Bench-verified — it produced a
clean result on the first attempt.**

Set the adapter's `Speed & Duplex` from `Auto Negotiation` to the target rate.
Three outcomes, each meaning something different:

| Result | Reading |
|---|---|
| Link up at the target rate | The path carries it. Negotiation was the problem, not the path. |
| **No link at all (0 Mb/s)** | The path cannot carry that rate. A definite answer — the fallback was hiding a real failure. |
| Still the lower rate | The driver accepted the setting and the hardware ignored it. Points at firmware or at the property not being honoured. |

**The point is that a negative result is useful.** Auto-negotiation converts
"cannot do 2.5G" into "here is 1G", which looks like success. Forcing removes
the fallback so the failure becomes visible.

Restore with the same command set back to `Auto Negotiation`.

⚠️ **Do this with console access or a second path to the machine.** Forcing a
rate the link cannot carry takes the interface down, which on a headless
server means no network at all.

---

## §3 — The adapter in the §5 case

### §3.1 — Read off the machine (Verified, user-reported)

```
InterfaceDescription : Marvell AQtion 10GBASE-T Network Adapter
DriverVersion        : 3.1.11.0
DriverProvider       : Marvell
DriverDate           : 2025-10-03
```

`Speed & Duplex` valid values, verbatim:

```
Auto Negotiation
100 Mbps Full Duplex
1.0 Gbps Full Duplex
10 Mbps Full Duplex
2.5 Gbps Full Duplex
5 Gbps Full Duplex
10 Gbps Full Duplex
```

**2.5G and 5G are both advertised by the driver**, so a driver that does not
know about the intermediate rates is ruled out on this machine.

Selected advanced properties as found: `Downshift retries` **4**,
`Energy-Efficient Ethernet` **Disabled**, `Jumbo Packet` **Disabled**,
`Flow Control` **Rx & Tx Enabled**, `Speed & Duplex` **Auto Negotiation**.

PnP identity, both entries:

```
PCI\VEN_1D6A&DEV_14C0&SUBSYS_E0001458&REV_03
```

### §3.2 — Identification — **VERIFIED 2026-09-17**

All three were Claude recall when first written. All three now have sources.

| Field | Resolves to | Source |
|---|---|---|
| `VEN_1D6A` | **Aquantia Corp.** (acquired by Marvell) | Linux Kernel Driver DataBase `CONFIG_NET_VENDOR_AQUANTIA`; DeviceHunt PCI vendor 1D6A |
| `DEV_14C0` | **AQC113C** — "NBase-T/IEEE 802.3an Ethernet Controller [Marvell Scalable mGig]" | lkddb `CONFIG_AQTION`; DeviceHunt PCI 1D6A:14C0; linux-hardware.org probe records |
| `SUBSYS` vendor `1458` | **Giga-byte Technology** | coreboot mailing list (2007-05, Gigabyte vendor id stated as 0x1458); an lspci capture rendering `Subsystem: Giga-byte Technology Device [1458:5000]` |

So the adapter is an **AQC113C on a Gigabyte board** — recall was right, and is now sourced rather than asserted.

⚠️ **Tier note:** these are community ID databases and mailing-list archives, not
Marvell or Gigabyte documents. Three independent databases agree on `14C0` and
two independent sources agree on `1458`, which is strong for an ID lookup, but
no vendor document was read.

**The AQC107 negotiation bug: RETRACTED.**

It was asserted repeatedly in session as an established firmware defect —
that AQC107-generation parts negotiate 10G and 1G but skip 2.5G/5G against
certain switches. **A targeted search on 2026-09-17 found no support for it
whatsoever** — not in Marvell material, not in driver changelogs, not in the
forum threads that surfaced. It was community lore at best and possibly a
conflation with the Intel i225-V stepping problems, which *are* widely
reported (B0/B1/B2 steppings, dropouts) and are a different vendor and
different part entirely.

**Do not repeat the AQC107 claim.** It entered this session as a confident
diagnosis and led the troubleshooting toward firmware for several turns.

### §3.2a — Downshift is a documented driver feature (Verified)

The Marvell FastLinQ Edge (AQtion) driver changelog records, under
**v3.0.10.0, dated 2020-02-05**:

> Add downshift support

Listed alongside thermal shutdown support and link-interrupt support in the
same release. **So `Downshift retries` is a deliberate feature with a vendor
changelog entry, not an obscure tuning knob.** [Lead tier on the hosting —
read from a third-party driver archive reproducing Marvell's release notes,
not from Marvell's own site.]

### §3.2b — AQC113 firmware updates separately from the BIOS — **corrects §8**

A standalone **AQC113 / AQC113C / AQC113CS firmware package, version 1.5.48**,
is distributed publicly, with users reporting flashing it onto *onboard*
controllers on Asus motherboards and seeing throughput change. **This
contradicts the session's claim that an onboard AQtion's firmware is carried
by the motherboard BIOS and can only be updated that way.**

⚠️ **[Forum] tier and a real caution:** the package is hosted on a third-party
driver archive, not Marvell, and the posted procedure involves editing a
subsystem code ID to match the board before flashing. **This library does not
endorse flashing it.** The finding that matters is narrower and solid — **the
firmware is a separate updatable component from the BIOS**, so "wait for a
Gigabyte BIOS release" was the wrong advice.


### §3.3 — Ghost adapter entries

`Get-PnpDevice -Class Net` returned **two** AQtion entries with identical
`VEN`/`DEV`/`SUBSYS`. The second reported `Status: Unknown`, `Present: False`
— a non-present leftover from an earlier driver or hardware state, not a
second NIC.

**Worth knowing generally:** `Get-PnpDevice` lists non-present devices, so a
count from it is not a count of installed hardware. Filter on `Present`.
A ghost entry can also hold a static IP and cause an address conflict later;
uninstalling it from Device Manager with hidden devices shown clears it.

---

## §4 — The switch

TP-Link **TL-SG608S-M2**, unmanaged. **[Lead] — retailer and distributor
copy, not TP-Link documentation.**

| Item | Listed |
|---|---|
| Ports | 8 × 2.5G RJ-45 |
| Management | Unmanaged |
| Rates | 10/100/1000/2500 Mb/s |
| Standards | 802.3 i/u/ab/x/p/bz |
| Switching capacity | 40 Gb/s |
| MAC table | 16K |
| Jumbo frames | 10 kB |

**Consequences for diagnosis:** all ports are multi-gig, so there is no wrong
port to avoid; and it is unmanaged, so there is no per-port configuration to
have got wrong and no port statistics to read. A per-port speed LED is
reported in retailer copy as distinguishing 1G from above — **unverified, and
worth checking against the unit**, since it gives a reading independent of
what Windows reports.

---

## §5 — Case record: unresolved

**Recorded as a worked example of elimination, not as a solved problem.**

Topology as described by the user: a 2.5G island on the TL-SG608S-M2,
uplinked to a 1G Netgear M4250. All 2.5G devices sit on the unmanaged switch.

| Fact established | How |
|---|---|
| Switch and cabling carry 2.5G | A Windows 10 laptop with a Realtek 2.5G NIC links at 2.5G through the same switch |
| Server driver is current and advertises 2.5G | §3.1 |
| Disabling downshift did not help | Set to `Disabled`; still 1 Gb/s |
| Forced 2.5G produces **no link at all** | §2 test, result 0 Mb/s |
| There is only one physical NIC in the server | §3.3 — the second entry is a ghost |

**Not established, because the test was never run:** whether the *server's own*
cable and switch port carry 2.5G. The laptop's working cable and port were
never moved to the server.

**Weighting revised 2026-09-17 after §1.1 was sourced.** Downshift is
specifically a response to a bad cable pair, and the forced-rate test returned
no link at all — both point at the copper rather than at the controller. **The
cable explanation is now the stronger of the two.** It is still not confirmed,
because the discriminating test was never performed, and §1.3 records a real
anomaly the cable theory does not by itself explain.

⚠️ **Do not read this document as saying the NIC was at fault** — that was the
session's working theory and it rested partly on a claim since retracted
(§3.2). Do not read it as saying the cable was at fault either. **One free
test settles it.**

**Note on the topology, arithmetic rather than diagnosis:** with a 1 Gb/s
uplink between the two switches, any traffic crossing between them is capped
at 1 Gb/s regardless of what either end negotiates. Traffic that stays on the
2.5G island is unaffected. This has nothing to do with the fault above and is
recorded because it bounds what the network can do.

---

## §6 — 2.5GBASE-T is less tolerant than 1000BASE-T

**[Lead] — community lore. No standards document was read and no cable was
tested.**

The reported pattern: 2.5G and 5G are more sensitive than gigabit to
termination quality, untwist at the connector, couplers, wall plates and
physical damage. A link with one marginal pair can run 1000BASE-T
indefinitely and refuse 2.5GBASE-T.

**The practical consequence, which holds regardless of the mechanism:** the
category printed on the jacket describes what the cable was, not what it is.
Cat6A that has been rolled, stepped on or pulled through truss for a season is
not evidence. **A short factory patch cord is the test**, and it is the one
that never got run in §5.

⚠️ **This section would be much stronger with IEEE 802.3bz read directly.**
Nothing here is sourced.

---

## §7 — Corrections log

Per `RULES.md` Rule 6.

| Claim made in session | Status | Cause |
|---|---|---|
| AQC107 2.5G negotiation firmware bug, offered as the leading theory | **Unsourced** | Community lore written from recall and presented as established device behaviour |
| "`DEV_14C0` is AQC113, so the AQC107 bug doesn't apply" | **Unverified both ways** | Used one unverified recall to retire another, producing a confident conclusion resting on nothing checked |
| Repeatedly proposed firmware and BIOS updates | **Premature** | The free discriminating test — the cable swap — was named but never insisted on before escalating to flashing |

---

## §8 — Open items

1. **Move the laptop's working cable and switch port to the server.** One
   test, two minutes, discriminates cable from NIC. Nothing else should be
   attempted first.
2. **PCI ID lookup** for `VEN_1D6A` / `DEV_14C0` / `SUBSYS_E0001458` — settles
   §3.2 entirely.
3. **Whether the AQC107 negotiation bug is real**, from Marvell or Aquantia
   rather than from recall.
4. **The switch's per-port speed LED behaviour**, from TP-Link's own manual —
   gives a reading independent of the OS.
5. **IEEE 802.3bz**, read directly, to put §6 on a source.
6. **Whether this NIC's firmware updates independently of the motherboard
   BIOS** — asserted in session as BIOS-carried on the strength of the
   unverified Gigabyte identification.
