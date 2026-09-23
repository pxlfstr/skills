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
  disassembled and not run.**
- **Firmware tables — located and compared, 2026-09-23:** each updater's COFF symbol table
  names four arrays in its `.data` section; each was sliced out by symbol address and the two
  updaters compared byte for byte (§ *What each updater carries*). Contents not decoded.
- **Not committed:** none of the vendor files above are in this repository.
- **User-stated:** users report updating fails on anything after Windows XP.
- **`[Forum]` — one field report**, relayed by the user, poster not named. See *Field reports*.
  A lead, not a fact.
- **Memory, not verified this session** — marked ⚠️ in *Routes on 64-bit Windows*.
- **`[Official]` — Texas Instruments, read 2026-09-23** (section *The processor and U mode*):
  - *Using the TMS320VC5506/C5507/C5509/C5509A USB Bootloader* — application report
    SPRA840C, dated October 2008 on the document. Fetched as PDF from ti.com, text read in
    full.
  - *TMS320VC5509A* product page, ti.com — fetched 2026-09-23; the page shows no
    last-edited date. Feature list and document list read.
  - **Not read:** the general bootloader note *Using the TMS320VC5503/C5506/C5507/C5509/
    C5509A Bootloader* (SPRA375, Rev. F); the data manual (SPRS205, Rev. K); the USB module
    reference guide (SPRU596); the SPRA840 example-code zip.
- **User-stated:** the mixer's processor is a TI TMS320VC5509A.
- **Open contradictions:** none known.
- **Revised 2026-09-23, additive audit:** INF class/service detail, the libusb package's own
  tools, and three further updater strings added.
- **Revised 2026-09-23, correction:** the audit revision said v2.12's `fErase` and
  `fIncUpdate` strings "suggest erase and incremental-update modes". **Wrong.** In the debug
  information they sit inside `tagPAINTSTRUCT` (`hdc`, `fErase`, `rcPaint`, `fRestore`,
  `fIncUpdate`, `rgbReserved`) — Windows' standard screen-painting structure, nothing to do
  with firmware. Cause: the names were read without checking the surrounding symbols. The line
  is removed and replaced below. Also added: firmware-table comparison, the answer to
  "step through v2.00 first?", and the field report.

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

## The processor and U mode

**Processor: TI TMS320VC5509A**, 16-bit fixed-point DSP. **Confirmed** — two independent
sources: the user's statement, and the INF's device ID matching TI's documented ROM
bootloader ID below.

[TI product page, ti.com [Official]]

| Item | Value |
|---|---|
| Core | TMS320C55x, 16-bit fixed point, 108 / 144 / 200 MHz |
| On-chip memory | 128K × 16-bit RAM · 32K × 16-bit ROM |
| USB | Full-speed (12 Mbps) slave: bulk, interrupt, isochronous |
| Debug | JTAG boundary scan; on-chip scan-based emulation logic |
| TI status | Active part; **no ongoing design support** from TI |

[*Using the … USB Bootloader*, SPRA840C [Official], Table 1, §§2, 4, 6, 9.1]

| Item | Value |
|---|---|
| Where the bootloader lives | **On-chip ROM**, byte address 0xFF0000 |
| USB vendor / product ID in USB-boot mode | **0x0451 / 0x9001** — identical to `VJX16-4.inf` |
| How USB-boot is selected | BOOTM[3:0] pins = **0010b** at reset (the same pins as GPIO0 and GPIO[3:1]) |
| Host sends | A boot table to **bulk OUT endpoint 0x06** |
| After the transfer | The DSP disconnects itself from USB and runs the loaded code |
| Reserved RAM during boot (5509/5509A) | Byte addresses 0x03F800–0x03FFFF |
| Input clock | 12.0 MHz |
| Can the ROM bootloader change? | **No** — TI: it resides in ROM and cannot be changed; every device uses the same VID/PID |

What follows:

- **U mode is the DSP's own ROM USB-boot mode.** ⚠️ That the rear U switch drives BOOTM[3:0]
  is inferred from the matching ID; not traced on the board.
- **A failed flash cannot erase U mode.** Whatever the update overwrites, the ROM bootloader
  is untouched, so retrying from U mode stays possible while the switch and USB work. This is
  the documented basis for the recovery in *Field reports*.
- ⚠️ **How the update probably runs**, inferred: the updater sends `DownloaderTab` (14,848
  bytes, identical in both updaters) as the boot table; it runs from RAM and then receives and
  writes the main program, FPGA code and presets.
- **Driver choice binds to fixed ROM code.** Any driver on VID 0451 / PID 9001 talks to the
  same unchangeable bootloader, which lowers the risk of the newer-driver route below. Its
  compatibility with the updater itself is still unverified.
- ⚠️ **Last resort, reasoning only:** the chip has JTAG and on-chip emulation. Whether the
  mixer's board brings JTAG out to a header is unknown.

## USB identity and driver

| Item | Value | Source |
|---|---|---|
| Device ID in update mode | `USB\VID_0451&PID_9001` | `VJX16-4.inf` [Official] |
| Driver | libusb-win32 **0.1.12.1** (DriverVer 03/20/2007) | `VJX16-4.inf` |
| Catalog files | `VJX16-4.cat` and `VJX16-4_x64.cat` are 168-byte placeholder text ("will be provided by Microsoft upon certification") — **no signature** | read directly |
| x64 driver | `libusb0_x64.sys` / `libusb0_x64.dll` inside the .rar only; **no Authenticode signature** (PE security directory empty) | inspected |
| x86 driver | loose `libusb0.sys` / `libusb0.dll` are byte-identical to the .rar's `bin/` copies; unsigned | inspected |

- INF class `LibUsbDevices`, ClassGUID `{EB781AAF-9C70-4523-A5DF-642A87ECA567}`; kernel
  service `libusb0`, demand-start (StartType 3). Useful for finding and removing the driver
  later. [`VJX16-4.inf`]
- The .rar also carries libusb-win32's own tools: `testlibusb-win.exe` and `testlibusb.exe`
  (list USB devices the driver can see), `inf-wizard.exe` (builds an .inf for a device),
  `install-filter.exe`, plus headers and libs. ⚠️ Using `testlibusb-win.exe` to confirm the
  mixer is visible before running an updater is my suggestion, not VIXID's.
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
- The firmware is embedded in each .exe — see *What each updater carries*.
- ⚠️ "sm1.0" / "sm1.2.1" read as the matching Snapshot Manager version. The Snapshot Manager
  (build 2012-02-14) asks for mixer firmware **v2.11** or later — see
  `creative-coding/references/protocols/vixid-vjx16-4-midi.md`.
- Keyer colour CCs moved from 107–109 to 14–16 at firmware **v2.00**, "released in early
  2010" (User Guide v5.8.3 p. 69 [Official]) — matches the v2.00 updater's build date.
- **No read-back or backup function** appears in either updater's strings. ⚠️ Flashing
  replaces whatever is on the unit with no way back.

- `FlashStartAdress`, `StartAdress`, `ReadPtr`, `BlocSize` and `Swap` in both updaters are
  variable names in the flashing code, from its debug information. Not features.

### What each updater carries

Four arrays per updater, named in the symbol table and built from the `UpdateData/` source
folder. Sizes are the distance between consecutive symbol addresses in `.data`.

| Array | v2.00 | v2.12 | Compared |
|---|---|---|---|
| `DSPMainTab` — main program | 102,688 bytes | 103,808 bytes | **Different** (23,686 of 102,688 bytes equal) |
| `DownloaderTab` | 14,848 bytes | 14,848 bytes | **Identical** |
| `FPGACodeTab` / `FPGATab` — FPGA code | 291,104 bytes | 291,104 bytes | **Identical** |
| `PresetTab` — factory presets | 2,688 bytes | 2,688 bytes | **Identical** |

- Arrays are 16-bit words (`short unsigned int` in v2.00's debug info). v2.00's debug info
  gives element counts for three of them: 51,342 / 7,422 / 145,539. × 2 bytes = 102,684 /
  14,844 / 291,078 — each fits its slot with 4 / 4 / 26 bytes spare.
- **Each updater is a complete package.** v2.12 differs from v2.00 only in the main program.
- **Stepping v2.00 → v2.12 gains nothing:** v2.00 would write the same downloader, FPGA code
  and presets that v2.12 writes anyway, then be overwritten — one extra flash, one extra
  chance to fail. Neither the procedure PDF nor either updater's text mentions a required
  order.
- ⚠️ Not established: whether every run rewrites all four parts (the send routine is named
  `SendDspFPGACode`), or whether the updater checks what is already on the unit.

Updater error strings, for diagnosis: `Error: could not find the VJX16-4` ·
`Error: usb communication failed` · `Error (%d) loading libusb0.dll` ·
`Make sure that the libusb library is correctly installed.`

## Routes on 64-bit Windows

⚠️ **The first three rows are from memory, none verified or tried.** Verify before use.

| Route | How | Risk |
|---|---|---|
| Driver-signature enforcement off for one boot | Advanced Startup → Disable driver signature enforcement; install the original .inf with the x64 files beside it | Closest to what the updater was built for; reverts on reboot |
| Newer signed libusb-win32 1.2.x | Bind the device with Zadig (libusb-win32 option); put the matching 32-bit `libusb0.dll` beside the updater | API compatibility with a 0.1.12.1-era app assumed; do not mix an old DLL with a new driver |
| Windows XP virtual machine | USB passthrough (VMware / VirtualBox) with the original package | A USB dropout mid-flash could brick the unit |
| **Physical Windows XP machine** | Original package, as VIXID intended | The only route with a reported success — see *Field reports* |

## Field reports

**One user report `[Forum]`**, relayed 2026-09-23, poster not named:

- Drivers would only work on a Windows XP machine — not "7 or later", which the poster
  expected to work.
- The update **failed about a third of the way through, leaving the mixer unusable**.
- Reinstalling the drivers and restarting, about three times, then retrying, **completed the
  update**.
- The poster's understanding: the update was for Snapshot Manager compatibility.
- The Snapshot Manager, on that XP machine, asked for registration once the mixer was
  connected by MIDI.

What it does and doesn't settle:

- **A failed mid-flash appears recoverable** by staying in U mode and retrying. One report —
  now backed by TI's documentation that U mode is ROM code (see *The processor and U mode*).
- ⚠️ "7 or later" failing isn't fully explained. Unsigned drivers explain 64-bit Windows;
  32-bit Windows 7 normally allows unsigned drivers after a warning. Unknown which the poster
  used.
- ⚠️ The driver-reinstall loop resembles VIXID's own warning that a second driver prompt can
  make the update fail. Consistent, not established.

Precautions, **reasoned from the above, not tested:** physical XP machine; USB straight to a
port, no hub; mains power, sleep off; install the driver and reboot **before** running the
updater; on failure, stay in U mode and retry rather than power-cycling and giving up.

**Before flashing at all:** check whether current firmware already answers the Snapshot
Manager sync request (see the MIDI doc). If it does, there may be nothing to gain.

## Not yet verified — open items

- Any of the three Windows routes, end to end.
- Recovery by re-entering **U** mode: one `[Forum]` report says yes, and TI documents the
  USB bootloader as unchangeable ROM. Not tested on this unit.
- Whether the U switch drives BOOTM[3:0] directly; whether a JTAG header is on the board.
- What the updater sends first, and in what order (the boot-table sequence is inferred).
- What the firmware tables contain beyond their size and whether they match (not decoded).
- Whether the beta B11.8r3d carries a different downloader or FPGA code than v2.00/v2.12.
- Where the mixer displays its firmware version.

| Section | Status |
|---|---|
| Procedure | `[Official]` |
| USB ID, driver version, signature state | `[Official]` files, inspected directly |
| Updater contents | Strings, headers and symbol tables; firmware arrays compared byte for byte; not disassembled or run |
| Field report | `[Forum]`, single source |
| Processor and U mode | `[Official]` TI application report + product page; switch-to-pins link and update sequence ⚠️ inferred |
| Windows routes | ⚠️ Memory; unverified |
