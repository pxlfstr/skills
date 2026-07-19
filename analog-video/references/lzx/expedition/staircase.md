# Staircase (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## Owners Manual

STAIRCASE
OWNER’S MANUAL
FLIGHT OF STAIRS
Staircase is the result of a few years of thought put into the subject of abstract pattern generation using analog computing techniques.  It
is a component of several modules designed for the purpose of processing horizontal and vertical ramp waveforms as the core source of
a complex 2D figure or pattern.  Staircase can be used in much the same way as a synced horizontal or vertical oscillator when fed a
horizontal or vertical ramp as its source, but its applications are much more open ended.
In video synthesis patches using our first generation of modules, it was often difficult to break away from the restriction of horizontal and
vertical elements and motions.  This was largely due to VCOs being the primary pattern generation source, and VCOs being able to lock
to either horizontal or vertical directions only.  To generate a 2D pattern, a vertically locked oscillator would modulate a horizontally
locked oscillator.  Staircase breaks out of this paradigm entirely, since its frequency modulation function is achieved through nonlinear
waveshaping.  This makes it possible to multiply the frequency of a 2D plane rather than a unidimensional one.   By this methodology,
one pattern can create another, in endless configurations.
This method of using chained full wave rectifiers as frequency doublers was first used by us in the original Video Waveform Generator
module, to double the frequency of the triangle oscillator core and enable the generation of a sawtooth/ramp waveshape output.  It was
used again in the polar-to-cartesian waveshaping portion of the Mapper module.  Doorway expands on the concept and grants access to
its inner workings in a creatively potent manner.
The artistic implications of this module go beyond the limits of my imagination, and I am beyond thrilled to see what you make with it.
Lars Larsen
November, 2016
814 SE 14th Ave.
Portland, OR 97214
USA
Creative tools for video synthesis
and analog image processing.
STAIRCASE
OWNER’S MANUAL
Written by Lars Larsen
Published November, 2016.
LZX-SC-OM-V1.0
FEATURES
TABLE OF CONTENTS
SPECIFICATIONS
USER CONTROLS & CONNECTIONS
BLOCK DIAGRAM
MANUFACTURER WARRANTY 6
EXAMPLE PATCHES 5
INSTALLATION 4
Staircase is a wideband analog frequency multiplier for video processing and pattern generation.  It allows the video synthesist to instantly
add greater visual complexity to their patches.   It can split an elliptical gradient into a series of concentric rings, solarize an input camera
source until the brightness of the signal has wrapped around many times, or perform the simple functions of a VCA, mixer, and
sawtooth-to-triangle waveshaper.
FEATURES
Voltage controlled multiplication of the input frequency up to 32 times.
Voltage controlled phase with harmonics selection allows 243 different visually rich modulation routings.
Simultaneous output of three different multiplication frequencies enables the rapid generation of full color patterns.
All signal and control paths perform at high frequency, video rate modulation speeds.
AC/DC input coupling switches and inverting level attenuators on  voltage control inputs.
SPECIFICATIONS
EuroRack Synthesizer Module
10HP
1.25 inches (31.75 mm)
70mA
70mA
Format
EuroRack Width
Mounting Depth
+12V Power Consumption
-12V Power Consumption
1.9882 inches (50.5 mm) *  5.059 inches (128.5 mm)Frontpanel Dimensions
499 ohms
100K ohms
Series Output Resistance
Input Termination Resistance
0-1V DCVoltage Levels (Expected)
+/-12V DCVoltage Levels (Absolute Maximum)
Fine tune control of phase modulation channel allows precise tuning of modulation input amplitudes for use cases in which visually
continuous phase scrolling is desired.
Phase control routing switches.  In the upward positions, the phase
voltage adds to the signal going into the associated frequency doubling
block (first, second, third, fourth, or fifth.)  In the downward positions, it
subtracts.  The combination of settings between these five switches
determines the overall visual effect phase modulation will have on the
output signals.
Frequency offset control.  Counter-clockwise, the input source is fully
attenuated.  Adjusted clockwise, the frequency multiplication of the
input signal increases from 1 to 32 repetitions.
Phase offset control.  In its center position, the output is 0.  Adjusted
counter-clockwise, voltage is subtracted from the phase modulation
channel.  Adjusted clockwise, voltage is added.  Modulation  destina-
tions are determined by the routing switches (1).
Inverting level controls.  These controls set the depth of external voltage
control modulation applied to the associated parameter.  In their center
positions, the output is 0.  Adjusted clockwise from center, the signal is
added to the associated parameter.  Adjusted counter-clockwise, the
signal is subtracted.
Voltage control AC/DC coupling switches.  In AC mode, slow moving
voltages are removed from the input signal and only high frequency
content remains.
Phase fine tune control.  This control adjusts the overall level of phase
modulation by +/-10%.  It is useful when attempting to match the level
of an input voltage to the exact scale of the source amplitude for contin-
uous scrolling.
USER CONTROLS & CONNECTIONS
Frequency external voltage control input. 0-1V DC full scale. The depth
of modulation is set by the associated inverting level control (4).
Primary source signal input for frequency multiplier. 0-1V DC expected.8
Phase external voltage control input. 0-1V DC full scale. The depth of modulation is set by the associated inverting level control (4).9
Frequency multiplier outputs, 0-1V DC levels.  The  /1 jack is the primary output.  The /2 and /4 outputs are direct outputs from the
third and fourth frequency doublers in the chain, and will output frequences half and one fourth the frequency of the primary output.
BLOCK DIAGRAM
Source In VCA Frequency
Doubler
Frequency
Doubler
Frequency
Doubler
Frequency
Doubler
Frequency
Doubler /1 Out
/2 Out
/4 Out
Frequency Control
Phase Control & Routing
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
Part of what makes Staircase such a powerful component of a video synthesis system is its ability to achieve modulation over the density
of a pattern.  This patches takes the H+V ramp mix from Visual Cortex and multiplies its frequency to create a diamond texture with 32
diamonds, each nested inside the other.  The Staircase’s three outputs are patched to Red, Green and Blue to create a colorized version of
the pattern.
Output to display.
Staircase outs
sent to RGB ins on
Visual Cortex.
COMPLEX COLORIZED PATTERN GENERATION
Further exercises and experiments to explore using this patch as a starting point:
Patch the RGB connections in different orders to achieve variant color palettes.
Instead of the H+V ramp mix, use external video as the input source to Staircase.
Apply voltage control to frequency.  Alternate ramp generator outputs (from Cortex) and external VCOs make great sources.
Apply voltage control to phase.  Flip the first harmonics switch up as a start point (others centered.) Play with switch settings.
In a more complex patch, insert Staircase into the signal path before a voltage control input, and use it as a weird VCA (with extra
effects!)
With two Staircase modules, insert another processor in a processing chain between the two.  Navigator’s rotation feature is especial-
ly interesting in this use-case.
H+V ramp mix
sent to source
input on Staircase.
By patching an output of Staircase to the Pedestal CV input of Prismatic Ray, you can gain access to all of its output waveshape
slopes as well as mixing with its internal VCO as a modulator.
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

LZX-SC-URC
Written by Lars Larsen
Illustrated by Dave Larsen
First Printing, Aug 2017
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
10HP
WIDTH
32mm
DEPTH
70mA
70mA
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
Staircase works wonderfully as a
waveshaping expander to a video
oscillator such as Prismatic Ray.  By
processing one of Prismatic Ray’s
waveshape outputs, it can multiply the
oscillator’s frequency and create
additional outputs at fixed harmonic ratios.
+
TIPS & TECHNIQUES
    Staircase is one of the most versatile
and exciting modules in our system.
Revisit it with any possible input signal
you have access to, it is designed to
make just about anything more
geometrically complex.
    Use Staircase to process horizontal
and vertical ramp signals at various
points along your shape generation
patches, and then use the stage
outputs to modulate the shape patch.
MADE IN PORTLAND, OR USA
STAIRCASE
USER REFERENCE CARD

Stage 5
+ OFF -
+ OFF -
+ OFF -
+ OFF -
+ OFF -
Stage 4
Stage 1
Stage 2
Stage 3
Phase +/-1V
VC level
VC fine tune
VC coupling
VC input
+/-
+/-
+/-10%
PHASE
INPUTS
VC input 0-1V FS
0-1V FS
0-1V FS
Frequency 0-X32
/2 (Stage 4)
1V DC
1V DC
1V DC
/1 (Stage 5)
Source
/4 (Stage 3)
VC level
FREQUENCY
OUTPUTS
CONTROLS & CONNECTIONS SIGNAL PATH BLOCK DIAGRAM
AC DC
VC coupling AC DC
FIRST STEPS
   Patch any kind of grayscale waveform or video into the Source
input.  The H+V ramp mix from Visual Cortex is a great signal to
start with, but don’t forget to experiment!
   Set all controls and switches to the positions shown in the
frontpanel image to the left.
   View the /1 (Stage 5) output using your video output module.
   Adjust the Frequency control clockwise and counterclockwise
to multiply the repetitions of the input waveform.
   Switch the Stage 1 switch up and play with the Phase control.
Experiment with different combinations of Stage switch settings.
   Patch the three different stage outputs to different color
channels to use Staircase as a colorizer.
VIDEO WA VESHAPING
Waveshapers have always been a function on the fringe of the
norm in audio synthesizers, most often included as integrated
functions of Voltage Controlled Oscillators.  Staircase is a wide
bandwidth waveshaper that, in visual terms, functions as a
multi-stage image solarizer with continuous control.
Voltage
Controlled
Amplifier
Doubler
Doubler
Doubler
Doubler
Doubler
Mix
FREQUENCY
SIG IN
VC IN
Mix
PHASE
