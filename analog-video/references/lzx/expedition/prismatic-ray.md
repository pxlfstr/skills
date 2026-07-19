# Prismatic Ray (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## Owners Manual

PRISMATIC RAY
OWNER’S MANUAL
THE EXCELLENT PRISM
Prismatic Ray is a reference to the mid-century fantasy fiction of Jack Vance, and to the tabletop roleplaying games inspired by it.  It is a
magic spell which blinds ones opponents with searing rays of multi-colored light.  Your video synthesis projections likely accomplish the
same effect, if you perform live with your video synthesizer.
VCOs are an essential building block of both audio and video synthesis, and a stable, highly usable wide frequency range VCO core was
one of the first items on our to-do list as we began developing video synthesis circuitry.  Prismatic Ray represents the latest evolution of
our video VCO design, also seen in the Video Waveform Generator module and earlier prototypes.
With Video Waveform Generator, we followed a design inspired by audio oscillators: Sine Shape and Pulse Width modulation had
dedicated control circuits and independent outputs.  In Prismatic Ray, I wanted to make these features more molded around the needs of
a visual synthesizer.  To that end, rather than having separate PWM and Sine shape modulators, we have an offset (Pedestal) and
amplitude modulation (Multiply) section, and a high gain amplifier, in the signal path between the VCO core and ALL of the output
waveshapers.  Modulation of these parameters now happens to all output waveshapes simultaneously, and the high gain control allows
for a smooth interpolation between gradual slopes or hard edged pulses.   We’ve also introduced 4 quadrant multiplication as a feature,
which allows the inversion of the output waveshape to be a function of voltage control!  This allows XOR-style patternmaking without the
need for external logic circuitry.
Please send us photos and videos of your dazed audiences after exposing them to the Prismatic Ray.  Happy patching!
Lars Larsen
December, 2016
814 SE 14th Ave.
Portland, OR 97214
USA
Creative tools for video synthesis
and analog image processing.
PRISMATIC RAY
OWNER’S MANUAL
Written by Lars Larsen
Published December, 2016.
LZX-PR-OM-V1.0
FEATURES
TABLE OF CONTENTS
SPECIFICATIONS
USER CONTROLS & CONNECTIONS
BLOCK DIAGRAM
MANUFACTURER WARRANTY 6
EXAMPLE PATCHES 5
INSTALLATION 4
Prismatic Ray is the next generation of the LZX Industries analog widerange Voltage Controlled Oscillator design.  With a max frequency
range into the megahertz and hard sync input with phase stability, it is uniquely qualified for video synthesis techniques.  In many VCO
designs, modulation of waveform shape is achieved after the oscillator core, with modulation over output waveshaper circuits.  In this
design, we place modulation in the core of the oscillator itself, allowing complex summing, linear key generation, multiplication and
inversion to affect all the output waveshapes simultaneously.   When multiple waveshapes are patched to different color channels, the
prismatic nature of this module begins to emerge.
FEATURES
Coarse & Fine tuning controls for oscillator frequency. Frequency Modulation voltage control input with dedicated level and inversion
control.
Simultaneous Triangle, Square, Sine, Anti-Sine, Exponential and Logarithmic waveshape outputs.
VCO core multiplier with dedicated level control and voltage control input.  High gain amplifier control enables fluid morphs between
hard and soft edged waveshapes.  In 4 Quadrant mode, the output waveshapes can be inverted under voltage control.
All signal and control paths perform at high frequency, video rate modulation speeds.
AC/DC input coupling switches and inverting level attenuators on  voltage control inputs.
SPECIFICATIONS
EuroRack Synthesizer Module
16HP
1.25 inches (31.75 mm)
120mA
90mA
Format
EuroRack Width
Mounting Depth
+12V Power Consumption
-12V Power Consumption
3.185 inches (80.9 mm) *  5.059 inches (128.5 mm)Frontpanel Dimensions
499 ohms
100K ohms
Series Output Resistance
Input Termination Resistance
0-1V DCVoltage Levels (Expected)
+/-12V DCVoltage Levels (Absolute Maximum)
VCO core bias level control and voltage control input allows control over the relative brightness of all the output waveshapes.  With
other patterns or video as a modulation source, the bias input allows this module to function as a powerful external slope and key
processor for any video signal.
USER CONTROLS & CONNECTIONS
Frequency Range & Sync Source selection
switch.  First position is slow animation (no
sync), second position is fast animation (no
sync), third position is horizontal bars (vertical
sync) and fourth position is vertical bars
(horizontal sync.)
Sync pushbutton switch.  Push to activate or
deactive oscillator sync.
Frequency fine tuning control.3
Triangle output level LED indicator.4
Multiplier high gain control.  Fully counter-clock-
wise and the multiplier functions at unity gain.
Adjusted clockwise and the outputs clip,
creating more hard-edged waveforms.
Pedestal offset control.  Pedestal mixes a
voltage with the internal triangle waveshape.  Its
position in the signal path is determined by the
multiplier mode switch (12.)
Frequency offset control.  Fully counter-clock-
wise, frequency is at its minimum value for the
selected range.  Adjusted clockwise, frequency
increases.
Sync mode selection switch.  In trigger mode, the VCO will
stop oscillation and reset as quickly as possible based on the
rising edge of the sync input signal.  In gate mode, the VCO
will not resume oscillation until the sync input signal goes low.
Voltage control AC/DC coupling switches.  In AC mode, slow
moving voltages are removed from the input signal and only
high frequency content remains.
2 3 4
11 11 11
14 15 16
19 20 21
Multiply offset control.  Controls the amplitude
and inversion of the internal waveform.  Its
function and signal path are determined by the
multiply mode switch (12.)
Inverting level controls.  These controls set the
depth of external voltage control modulation
applied to the associated parameter.  In their
center positions, the output is 0.  Adjusted
clockwise from center, the signal is added to the associated
parameter.  Adjusted counter-clockwise, the signal is
subtracted.
Multiply mode switch.  In 2Q (2 Quadrant) mode, the multiply
control functions as a crossfader between the Pedestal value
(6) and the internal triangle VCO waveform.  In 4Q (4
Quadrant) mode, multiply controls both the inversion and
amplitude of the internal triangle VCO waveform, and the
Pedestal value (6) is summed with the waveform afterwards.
See the block diagrams for details.
Oscillator sync/reset input. 0-1V DC expected, 0.5V compara-
tor threshold.  The oscillator will reset on the rising edge of
any input signal. Patching this connection will override any
sync source selected by the range selection switch (1).
Pedestal voltage control input. 0-1V DC full scale. The depth of
modulation is set by the associated inverting level control (9).
Frequency voltage control input. 0-1V DC full scale. The depth
of modulation is set by the associated inverting level control
(9).
Multiply voltage control input. 0-1V DC full scale. The depth of
modulation is set by the associated inverting level control (9).
Square wave output, 0-1V level.
Sine wave output, 0-1V level.
Parabolic wave output, 0-1V level.
Triangle wave output, 0-1V level.
Exponential wave output, 0-1V level.
Anti-sine wave output, 0-1V level.
BLOCK DIAGRAM
Voltage
Controlled
Oscillator
Square Out
Frequency & Range Controls
Sync Input & Settings
Voltage
Controlled
Crossfader
Multiply Control
Pedestal Control
High Gain
Amplifier
Gain Control
Triangle Out
Triangle Out
Wave
Shapers
Sine Out
Parabola Out
Anti-Sine Out
Expo Out
Voltage
Controlled
Oscillator
Square Out
Frequency & Range Controls
Sync Input & Settings
4 Quadrant
Multiplier
Pedestal Control
Multiply Control
High Gain
Amplifier
Gain Control
Triangle Out
Triangle Out
Wave
Shapers
Sine Out
Parabola Out
Anti-Sine Out
Expo Out
2 Input
Mixer
SIGNAL PATH IN 2 quadrant (2Q) MODE
SIGNAL PATH IN 4 quadrant (4Q) MODE
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
The VCO is a core element of analog synthesis, whether we’re discussing audio or video.  In this patch, we familiarize you with a use case
for the simultaneous waveshape outputs of Prismatic Ray and a basic setup for modulating a horizontally synchronized oscillator with a
vertically synchronized waveform (such as the V Ramp output on Visual Cortex.)
Output to display.
Vertical ramp
modulating VCO
frequency creates
horizontal
displacement.
2D Pattern GENERATION w/COLORIZED EDGE GRADIENTS
Further exercises and experiments to explore using this patch as a starting point:
Patch the RGB connections in different orders and to different waveform outputs to get different color palettes.
Instead of modulating the frequency CV input, explore the visual differences of modulating Pedestal and Multiply instead.
Play with the gain control for more pulse-width modulation based responsiveness from pedestal modulation.
Explore 4 quadrant and 2 quadrant modes, with and without modulation.  These modes change the functions of Multiply and Pedestal.
Try using external audio and video images as modulation sources.  Play with all the frequency ranges while doing this.
In 2 quadrant mode, with Multiply fully counter-clockwise and Pedestal centered, patch an external signal into the Pedestal VC input.
Put the Pedestal VC level control fully clockwise.   You are now processing the external signal through all of Prismatic Ray’s output
waveshapers and high gain amp, with the internal VCO fully suppressed.
By patching the Anti-Sine/Sine or Exponential/Parabola outputs into the A/B inputs of a crossfader module, you can control the
crossfader to get a waveshape morph.  The center position of the crossfader (both inputs at 50%) will give triangle output.    Combined
with the technique for external processing described above, you can achieve gamma and gray level expansion/compression when
your source is a video image.
Try patching a 2D shape or external camera image into the sync input.
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
BEFORE YOU BEGIN PRISMATIC RAY
SPECIFICATIONS
16HP
WIDTH
32mm
DEPTH
120mA
90mA
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
LZX-PR-URC
Written & Illustrated by Lars Larsen
First Printing, Feb 2017
©2017 LZX Industries LLC
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
For automatic connection to video sync signals, Prismatic Ray must
be installed on the same power bus as your system’s video sync
generator module (such as Visual Cortex.)  Your sync generator
module must also be set to send H/V sync to the EuroRack CV/Gate
bus.
INSTALLATION
YOUR NEXT MODULE?
Dedicated horizontal and vertical
oscillators are a powerful pairing for
pattern synthesis.  Adding a second (or
third, or fourth...) Prismatic Ray to your
video synthesis system will instantly
unveil a new layer of cross modulation
and geometric density to explore.
+
TIPS & TECHNIQUES
    Use mults to send the same
modulation source to multiple VC
inputs at once.  Use mixer modules
(like Passage or Bridge) to mix together
many modulation sources.
    Use video images as a modulation
or sync source -- all the output
waveshapers can process video too!
    Feed different output waveshapes to
RGB color channels simultaneously, to
create subtle gradients.
MADE IN PORTLAND, OR USA
PRISMATIC RAY
USER REFERENCE CARD

DCVC coupling AC DC
VC input 0-1V FS
Range
Mode gATE TRIGGER
Sync input 0.5V
VC input 0-1V FS
VC coupling AC DC
Sync enable ON OFF
Coarse tune 100%
Pedestal +/-1V
Fine tune +/-10%
VC level +/-
VC level +/-
FREQUENCY
SYNC
VC coupling AC
VC input 0-1V FS
Multiply 0X-1X
1V DCSine
1V DCParabola
1V DCExponential
1V DCAnti Sine
1V DCSquare
Gain 1X-25X
Triangle indicator
Mode 2QUAD 4QUAD
VC level +/-
1V DCTriangle
MULTIPLY
OUTPUTS
PEDESTAL
Wideband
Voltage Controlled
OscillatorMix
Voltage Controlled
Crossfader
Mix
B
VC
A
Wave Shapers
MULTIPLY
VC
SYNC
FREQUENCY
Mix
High Gain
Amplifier
RANGE
GAIN
PEDESTAL
Mix Mix
Four Quadrant
Multiplier
X Y
MULTIPLY
PEDESTAL
2QUAD
4QUAD
CONTROLS & CONNECTIONS
Prismatic Ray receives H and V sync signals automatically through
its power cable.  These signals are sent by your system’s video
sync generator module (such as Visual Cortex) but can also be
patched directly.  See installation notes for more details.
Horizontal bars 90Hz - 6.25KHz
22.5KHz - 1MHzVertical bars
Animation 7 secs/cycle - 10Hz None
2Hz - 150Hz NoneStrobing
GENERATes FREQUENCY RANGE SYNC SOURCE
FREQUENCY RANGES & VIDEO SYNC
SIGNAL PATH BLOCK DIAGRAM
FIRST STEPS
   Set all controls and switches to the default settings shown on
the frontpanel illustration to the left.
   Patch one of the waveshape outputs to your video display
module or video output module (such as Visual Cortex).
   Play with the frequency range and tuning controls first. Select
each range and view the output while adjusting coarse tune. Push
the sync enable on/off pushbutton at each range as well.
   Explore the other controls, one by one.  Then work through the
signal path diagram above to learn how they all connect.
   Modulate Prismatic Ray with audio or CV.  Experiment with all
VC inputs, multiply modes, and different frequency ranges.
CV/
Gate
BUS
