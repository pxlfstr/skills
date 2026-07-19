# Bridge (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## Owners Manual

BRIDGE
OWNER’S MANUAL
BRIDGES BETWEEN WORLDS
Bridge at first glance is a modest selection of utility functions, but like the mundane contents of an adventurer’s backpack, the journey
can’t progress as far without it.  Our goal with this module was to provide a module that was small, low cost, and provided the kind of
functions that one can never have too many of.  Each functional block here multiplies the potential of every other module in your system
by allowing quick access to amplitude modulation, switching, signal mixing, amplification, buffering, and attenuation.
Lars Larsen
December, 2016
814 SE 14th Ave.
Portland, OR 97214
USA
Creative tools for video synthesis
and analog image processing.
BRIDGE
OWNER’S MANUAL
Written by Lars Larsen
Published December, 2016.
LZX-BR-OM-V1.0
FEATURES
TABLE OF CONTENTS
SPECIFICATIONS
USER CONTROLS & CONNECTIONS
BLOCK DIAGRAM
MANUFACTURER WARRANTY 6
EXAMPLE PATCHES 5
INSTALLATION 4
Bridge is a multi-function utility module for video synthesizers.  It is designed with the simple goal of packing a variety of always useful
utility functions into a compact, low cost package.
FEATURES
Dual buffered multiples with three outputs and voltage scaling.  In amplify setting, input signals are amplified by a factor of five.  In
attenuate setting, input signals are attenuated by a factor of five.  These scalers allow quick translation between standard EuroRack
audio world 5V signal levels and LZX video module 1V signal levels.
Single wideband voltage controlled crossfader/multiplier with CV inversion switch.  It can be patched as a single VCA, a crossfad-
er/switcher between two inputs, or when combined with the mixer section a 4-quadrant multiplier.
Single three input signal mixer.  Two adding inputs and one subtracting input.  One adding input can alternately perform a mirrored
inversion (1V - input signal.)
SPECIFICATIONS
EuroRack Synthesizer Module
8HP
1.25 inches (31.75 mm)
30mA
30mA
Format
EuroRack Width
Mounting Depth
+12V Power Consumption
-12V Power Consumption
1.5882 inches (40.34 mm) *  5.059 inches (128.5 mm)Frontpanel Dimensions
499 ohms
100K ohms
Series Output Resistance
Input Termination Resistance
0-1V DCVoltage Levels (Expected)
+/-12V DCVoltage Levels (Absolute Maximum)
Buffered Multiple/Scaler #1 input.  0-1V DC expected in buffered multiple or X5
(LZX to Euro) gain mode.  0-5V DC or +/-5V DC expected in /5 (Euro to LZX)
attenuation mode.
Buffered Multiple/Scaler #1 gain selection switch.  In the upper position, the
input voltage is amplified X5 to perform LZX (0-1V DC) to EuroRack Audio (0-5V
DC) level translation.   In the center position, the input signal is buffered at unity
gain.  In the lower position, the input voltage is divided by 5 to perform EuroRack
Audio (0-5V DC) to LZX (0-1V DC) level translation.
Buffered Multiple/Scaler #1 output jacks.  Each output is individually buffered.3
Buffered Multiple/Scaler #2 input.  Functions as (1).4
Buffered Multiple/Scaler #2 output jacks.  Functions as (3)6
Fader Channel A input. 0-1V DC expected.7
USER CONTROLS & CONNECTIONS
Fader Channel B input. 0-1V DC expected.8
Fader Voltage Control input. 0-1V DC expected.9
Buffered Multiple/Scaler #2 gain selection switch.  Functions as (2).5
Fader direction selection switch.  In downward position, a voltage control signal
(9) rising from 0V to 1V will cause the output (11) to crossfade from channel A
to channel B.  In the upward position, a rising control voltage will crossfade from
channel B to channel A.
Fader output. 0-1V typical.11
Mixer non-inverting input. 0-1V DC expected.  Signal patched here will be added
to other mixer inputs (13), (14).
Mixer inverting input.  0-1V DC expected.  Signal patched here will be subtracted
from other mixer inputs (12), (14).
Mixer multi-function input.  0-1V DC expected.  How this signal interacts with the
mix is determined by the position of the multi-function input mode switch (15).
Mixer multi-function input mode switch.  In its downward position, the multi-function input (14) adds to the mix in the same manner
as the non-inverting input (12).  In its upward position, Negative, the signal is subtracted from a 1V bias and then added to the mix.
Mixer output. 0-1V typical.16
BLOCK DIAGRAM
Channel A
Cross
Fader
Out
Voltage Control
Channel B
+ In
3 Input
Mixer
Out- In
+|1- In
Input Scaler
& Buffers
Out
Out
Out
Input Scaler
& Buffers
Out
Out
Out
INSTALLATION
Remove the module from its packaging and connect the 16-pin power cable to the keyed power entry header on the rear of the module as
shown. Connect the other end of the power cable to an empty connector on your EuroRack power distribution busboard.  Ensure pin 1
(-12V, with the red stripe) is oriented as indicated on your power distribution busboard.
After connecting the power cable, mount the module frontpanel flush to your enclosure's EuroRack mounting rails and secure the module
with the mounting screws provided by your enclosure's manufacturer.
Power down your EuroRack case and disconnect it from AC power outlet while installing new modules.
CV
Gate
+5V
+12V
0V
-12V
EuroRack module. EuroRack 16-pin
power cable.
EuroRack power distribution
bus board.
Power input header.
Red stripe on cable lines up
with -12V on bus board.
EuroRack rail
mounting screws.
EXAMPLE PATCHES
One of Bridge’s primary use cases is voltage level translation between EuroRack audio modules and LZX video synthesis modules.  LZX
modules are tolerant of voltages from audio modules, but the expected voltage range (0 to 1V) is smaller than what is typical from audio
modules (0 to 5V or +/-5V.)  This means an audio module plugged straight into an LZX module will clip.  Sometimes this is desirable. When
it’s not, Bridge has a preset attenuator for level translation as illustrated below.
Output to display.
Scaler/Multiple #1
input connects
to EuroRack
audio module’s
output.
Scaler/Multiple #1
switch is set to
/5.
EURORACK AUDIO TO LZX LEVEL TRANSLATION
Further exercises and experiments to explore:
Try using the scaler/multiples to amplify a video rate signal, process it with audio modules, and then send it back to video output.  This
works especially well if you set the Visual Cortex compositor up so that the processed signal is on the A channel and the original signal
is on the B channel.  You can now do a wet/dry mix between the two versions of the signal.
Try patching ramps and video sources into the fader and mixer sections and experiment with how the various combinations work.  Try
audio rate and low frequency sources into these processes as well.
Use the multiples in unity gain mode to send a single output to multiple destinations at the same time.  Parallel processing is incredibly
powerful in a video system.
After setting up a patch you like between other modules, use Bridge’s utility functions to insert more modulation into signals in the
patch to add further nuance and visual complexity.
MANUFACTURER’s WARRANTY
Fully assembled versions of this product are covered by our manufacturer warranty for one year following the date of manufacture. This
warranty covers any defect in the manufacturing of this product., such as assembly errors or faulty components. This warranty does not
cover any damage or malfunction caused by incorrect use – such as, but not limited to, power cables connected backwards, excessive
voltage levels, or exposure to extreme temperature or moisture levels. The warranty covers replacement or repair, as decided by the
manufacturer. Please contact customer service via our website at www.lzxindustries.net for instructions on returning the product.  The cost
of returning a product for repair or replacement is paid for by the customer.
DIY kits and bare printed circuit boards are not covered under any warranty and come with no guarantee of assembly troubleshooting or
customer support.  However, we are nice and will help you when possible. Please contact us if you have questions about or problems  with
your build.

## User Reference Card

LZX-BR-URC
Written by Lars Larsen
Illustrated by Dave Larsen
First Printing, September 2017
©2017 LZX Industries LLC
Take a moment to familiarize yourself with our website
lzxindustries.net.  You’ll find documentation, instructional videos,
links to community forums, and other user resources.  Register
your product’s serial number with us to aid any future technical
support requests.  Some synthesists will find everything they
need to learn this module in this reference card, but don’t forget
there are videos and patch tips online.   If you get stuck, have
questions, or need help of any kind -- please write to us.
ONE YEAR
WARRANTY
BEFORE YOU BEGIN STAIRCASE
SPECIFICATIONS
8HP
WIDTH
31.75mm
DEPTH
30mA
30mA
N/A
MAX POWER DRAW
+12V
-12V
+5V
100K ohms
INPUT TERMINATION
499 ohms
OUTPUT RESiSTANCE
+/-12V
MAX INPUT VOLTAGE
0-1V
VC CONTROL RANGE
0-1V
OUTPUT LEVELS
3U EuroRack
Synth Module
FORMAT
Mounting
screw.
-12V
0V
+12V
+5V
GATE
CV
Red stripe
to -12V.
Power down the EuroRack case and unplug it from the wall.
Connect the provided EuroRack power cable to your module and
then to your EuroRack power bus board as shown.  Mount the
module in your case using the mounting screws provided by
your case’s manufacturer.
Power cable.
INSTALLATION
YOUR NEXT MODULE?
Arch and Bridge are the Expedition Series’
utility modules -- swiss army knives that
serve as glue between modules in larger
patches, or enabling more advanced
techniques requiring access to simple
core functions.  While they may look
nonassuming, don’t underestimate them!
+
TIPS & TECHNIQUES
    The Fader section can be patched as
a crossfader or a VCA/2-quadrant
multiplier.  This is one of the most
useful functions in your video
synthesis arsenal, as it allows you to
switch between and mix 2 different
input signals.  Don’t forget that you can
also use it for image multiplication for
techniques such as image brightness
restoration or controlled by a key
generator as a keying function.
MADE IN PORTLAND, OR USA
BRIDGE
USER REFERENCE CARD

Buffered output 3
Buffered output 2
Input
Gain
Buffered output 1
Multiple/SCALER 1
VC input
Output
0-1V FS
Channel A+/- 1v/5V
+/- 1v/5V
Channel B
FADER
CONTROLS & CONNECTIONS SIGNAL PATH BLOCK DIAGRAM
Direction
SCALING SIGNALS FROM AUDIO SYNTHESIZERS
Bridge is often used to convert between the voltage ranges used
by audio synthesizers and video synthesis modules.  To
accomplish this, patch your source signal into one of the
Multiple/Scaler section inputs.  Set the gain switch to Divide-By-5
to convert audio synthesizer signals to video synthesis scale.  Set
the gain switch to Multiply-By-5 to onvert video synthesis signals
to audio synthesizer ranges.
MULTING: A CORE PATCHING TECHNIQUE
“Multing” is the process of splitting an output in order to send a
signal to multiple destinations in parallel.  It is one of the most
important core patching techniques of a video synthesis system,
and is used in almost any advanced patch.  Multing can be done
passively with stackable cables or splitters, but Bridge offers two
buffered multiples/scalers.   A buffered multiple will ensure there
is no signal or bandwidth lost which may occur as a result of
passive multing.  A dedicated mult module (1 in, multiple outputs)
also allows you to mult your signals with normal patch cables.
5 1 X5
Buffered output 3
Buffered output 2
Input
Gain
Buffered output 1
Multiple/SCALER 2
5 1 X5
0-1V FS
0-1V FS
1V DC
Add/Negative
Output
0-1V FS
Add
Subtract
MIXER
Mode
0-1V FS
0-1V FS
1V DC
OFF NEGATIVE
Scaler Scaler
ADD
ADD
SUBTRACT
Mixer
Negative
Crossfader
VC IN
Unipolar CV & Logic
AUDIO SYNTH TYPICAL RANGES
0-5VAll signals
VIDEO SYNTH TYPICAL RANGES
0-1V
Bipolar CV & Audio +/-5V
