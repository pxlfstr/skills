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
| §1 downshift mechanism | **Bench-verified** on one adapter — property and default read off the user's machine; behaviour is reasoned |
| §2 forcing method | **Bench-verified** — the forced-rate test was performed and produced a result |
| §3 adapter facts | **Verified**, user-reported — PowerShell output pasted verbatim into the session |
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

⚠️ **Every chip- and vendor-identification claim in §3.2 is Claude recall and
is marked unverified.** They were stated confidently in session before being
marked. Do not quote them.

---

## §1 — Downshift: the mechanism that hides the failure

Marvell AQtion drivers expose an advanced property **`Downshift retries`**,
default **4** on the adapter examined (§3.1).

**Behaviour as understood — reasoned, not measured:** the PHY attempts the
highest common rate, and after the configured number of failed attempts drops
to a lower rate and stays there. The link comes up, traffic flows, nothing is
logged where anyone looks, and the only symptom is a link speed nobody
notices until a transfer is slower than budgeted.

**Why it matters for video work:** a link that silently self-demotes is worse
than one that fails. An NDI or 2110 bandwidth budget written against 2.5 Gb/s
runs on 1 Gb/s and the discovery happens under load.

⚠️ **On the adapter in §5, setting `Downshift retries` to `Disabled` did not
change the outcome — the link still came up at 1 Gb/s.** Whatever demoted
that link, disabling this property did not stop it. The mechanism above is
the documented-sounding explanation; it did not predict this machine's
behaviour.

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

### §3.2 — Identification ⚠️ UNVERIFIED

**None of the following was checked against the PCI ID repository, a Marvell
datasheet or any vendor document. All are Claude recall, stated in session
before being marked.**

- `VEN_1D6A` → Aquantia (acquired by Marvell) — **unverified**
- `DEV_14C0` → AQC113 / AQC113C generation — **unverified**
- `SUBSYS` vendor `1458` → Gigabyte — **unverified**
- **"AQC107-generation cards have a known firmware bug where 2.5G/5G
  negotiation fails against certain switches while 10G and 1G work"** —
  **unverified community lore.** Asserted several times in session as though
  established. It may be real; nothing in this library confirms it, and it was
  used to argue *against* a firmware theory once the device ID was read, which
  compounds the error.

**A single lookup in the PCI ID repository settles the first three.**

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
never moved to the server. **Everything above is consistent with a bad server
cable, a bad termination, and with a NIC or firmware fault — the evidence does
not separate them.**

⚠️ **Do not read this document as saying the NIC was at fault.** Two
explanations remain open and one free test discriminates between them.

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
