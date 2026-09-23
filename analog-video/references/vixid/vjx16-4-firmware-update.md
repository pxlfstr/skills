# VIXID VJX16-4 — firmware update and USB driver

How the VJX16-4 is flashed, what the two known updaters contain, and why updating fails on
64-bit Windows after XP. Device reference: `vjx16-4.md` (this folder).

## Provenance

- **`[Official]`** — *Vixid VJX16-4 video mixer — Upgrade procedure* [Official], user-supplied
  PDF (2 pp., created 2010-03-29), read in full 2026-09-23.
- **`[Official]`, inspected directly** — VIXID's own update package, user-supplied, examined
  2026-09-23: `USBUpdaterGUI_v2_00.exe`, `USBUpdaterGUI_v2_12.exe`, `VJX16-4.inf`,
  `VJX16-4.cat`, `VJX16-4_x64.cat`, `libusb0.dll`, `libusb0.sys`,
  `libusb-win32-device-bin-0_1_12_1.rar`. Method: INF read as text; PE headers, import tables,
  build timestamps and digital-signature directories read with `pefile`; readable strings
  extracted; the .rar unpacked and its binaries compared. **The updaters were not
  disassembled and not run.** The firmware images inside them were not extracted.
- **Not committed:** none of the vendor files above are in this repository.
- **User-stated:** users report updating fails on anything after Windows XP.
- **Memory, not verified this session** — marked ⚠️ in *Routes on 64-bit Windows*. No web
  source read.
- **Open contradictions:** none known.

---

## Procedure (vendor)

1. Mixer off. Rear selector to **U**. Handle the switch with care.
2. USB cable to the computer. Mixer on.
3. Windows asks for a driver: point it at the updater's folder (first run only; may ask twice
   — a second prompt can make the update fail; close, rerun, reboot if repeated).
4. Run the updater .exe; it walks through the flash.
5. Mixer off, selector **off U**, mixer on — new firmware runs.

The updater's own closing text says to put the switch "in the bottom position" before
powering up.

## USB identity and driver

| Item | Value | Source |
|---|---|---|
| Device ID in update mode | `USB\VID_0451&PID_9001` | `VJX16-4.inf` [Official] |
| Driver | libusb-win32 **0.1.12.1** (DriverVer 03/20/2007) | `VJX16-4.inf` |
| Catalog files | `VJX16-4.cat` and `VJX16-4_x64.cat` are 168-byte placeholder text ("will be provided by Microsoft upon certification") — **no signature** | read directly |
| x64 driver | `libusb0_x64.sys` / `libusb0_x64.dll` inside the .rar only; **no Authenticode signature** (PE security directory empty) | inspected |
| x86 driver | loose `libusb0.sys` / `libusb0.dll` are byte-identical to the .rar's `bin/` copies; unsigned | inspected |

- The INF's x64 section needs `libusb0_x64.sys` and `libusb0_x64.dll` **in the same folder as
  the .inf**. The loose files supplied are the 32-bit pair only.
- ⚠️ Why post-XP fails: 64-bit Windows refuses unsigned kernel drivers, so the mixer never
  gets a driver and the updater reports it can't find the VJX16-4. Consistent with the user
  reports; not tested.

## The updaters

| File | Build (PE timestamp) | Build folder in strings | Embedded data |
|---|---|---|---|
| `USBUpdaterGUI_v2_00.exe` | 2010-03-24 | `USBUpdaterGUI_v2.00_sm1.0` | `.data` 411,648 bytes |
| `USBUpdaterGUI_v2_12.exe` | 2012-02-28 | `zUSBUpdaterGUI_v2.12_sm1.2.1` (also a `…v2.10…` path) | `.data` 412,672 bytes |

- Both are 32-bit GUI apps (MinGW) that **load `libusb0.dll` at runtime** — no static import.
  Strings name the libusb-0.1 calls they use: `usb_bulk_write`, `usb_bulk_read`,
  `usb_claim_interface`, `usb_close`.
- Strings state the build was "designed using version 0.1.12.1 of the Libusb-win32 library".
- ⚠️ The firmware image is embedded in each .exe (the ~400 KB data section and an
  `UpdateData` build folder). Inferred, not extracted.
- ⚠️ "sm1.0" / "sm1.2.1" read as the matching Snapshot Manager version. The Snapshot Manager
  (build 2012-02-14) asks for mixer firmware **v2.11** or later — see
  `creative-coding/references/protocols/vixid-vjx16-4-midi.md`.
- Keyer colour CCs moved from 107–109 to 14–16 at firmware **v2.00**, "released in early
  2010" (User Guide v5.8.3 p. 69 [Official]) — matches the v2.00 updater's build date.
- **No read-back or backup function** appears in either updater's strings. ⚠️ Flashing
  replaces whatever is on the unit with no way back.

Updater error strings, for diagnosis: `Error: could not find the VJX16-4` ·
`Error: usb communication failed` · `Error (%d) loading libusb0.dll` ·
`Make sure that the libusb library is correctly installed.`

## Routes on 64-bit Windows

⚠️ **All from memory, none verified or tried.** Verify before use.

| Route | How | Risk |
|---|---|---|
| Driver-signature enforcement off for one boot | Advanced Startup → Disable driver signature enforcement; install the original .inf with the x64 files beside it | Closest to what the updater was built for; reverts on reboot |
| Newer signed libusb-win32 1.2.x | Bind the device with Zadig (libusb-win32 option); put the matching 32-bit `libusb0.dll` beside the updater | API compatibility with a 0.1.12.1-era app assumed; do not mix an old DLL with a new driver |
| Windows XP virtual machine | USB passthrough (VMware / VirtualBox) with the original package | A USB dropout mid-flash could brick the unit |

**Before flashing at all:** check whether current firmware already answers the Snapshot
Manager sync request (see the MIDI doc). If it does, there may be nothing to gain.

## Not yet verified — open items

- Any of the three Windows routes, end to end.
- Whether a failed flash is recoverable by re-entering **U** mode (the manual doesn't say).
- Firmware versions actually inside each updater (not extracted).
- Where the mixer displays its firmware version.

| Section | Status |
|---|---|
| Procedure | `[Official]` |
| USB ID, driver version, signature state | `[Official]` files, inspected directly |
| Updater contents | Strings and headers only — not disassembled or run |
| Windows routes | ⚠️ Memory; unverified |
