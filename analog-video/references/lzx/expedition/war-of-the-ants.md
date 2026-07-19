# War Of The Ants (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## User Reference Card

ONE YEAR
WARRANTY
WAR OF THE
ANTS SPECS
16HP
WIDTH
45mm
DEPTH
110mA
100mA
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
LZX-TX-URC
Written & Illustrated by Lars Larsen
First Printing, June 2017
©2017 LZX Industries LLC
YOUR NEXT MODULE?
+
TIPS & TECHNIQUES
    Patch the Animation output to one of
the filter VC inputs, for low frequency
modulation of blurring and edge
enhancement.
    Feed external video into the H and V
inputs simultaneously to create a 2D
noise filter effect on the Texture output.
    Freak out your parents by patching
the noise into their television so they
think it’s tuner static, and modulate it
with a hidden microphone.
MADE IN PORTLAND, OR USA
WAR OF THE ANTS
USER REFERENCE CARD
War Of The Ants is a texture generation
instrument.  In a creative context, texture is
typically used to add visual variation along
the contours of a shape or figure.  A shape
figure like Shapechanger is a natural pair
to War Of The Ants, with much potential
for cross-modulation.
SYNC
OUT
Power down the EuroRack case and unplug it from the wall.
Connect the provided EuroRack power cable to your module and
then to your EuroRack power bus board as shown.  Use an RCA
cable to connect video sync from your system’s video synchro-
nization source to one of the Sync I/O jacks as shown below.
If War Of The Ant’s Sync I/O jacks are
used to send sync to another module,
turn the TERMINATE switch down (off.)
If War Of The Ants is the last module in
the sync chain, turn the TERMINATE
switch up (on.)
Mount the module in your case using
the mounting screws provided by your
case’s manufacturer.
INSTALLATION
Mounting screw.
SYNC
IN
-12V
0V
+12V
+5V
GATE
CV
Red stripe
to -12V.
Power cable.
SYNC
I/O
SYNC
I/O
RCA cable connects sync output from system’s video sync generator
(or daisy chained module) to sync input on rear of module.
TERMINATE

CONTROLS & CONNECTIONS SIGNAL PATH BLOCK DIAGRAM
RANDOM ANIMATOR
Speed
LED indicator AC DC
Depth
HORIZONTAL FILTER
Cutoff frequency
Mode
VC coupling AC DC
VC input 0-1V FS
VC level +/-
HP LP
Input 0-1V FS
Output 1V DC
CONFORMING TEXTURE TO A 2D OBJECT
FIRST STEPS
   Set all controls and switches to the default settings shown on
the frontpanel illustration to the left.
   Patch the Texture output jack to your video output module. This
is a mix of all the processing elements inside the module.
   Explore the controls to see how they effect the output across
three different spectral domains: animation, vertical, and
horizontal.
   Next, explore the other outputs and try modulating the three
voltage controlled parameters.
VERTICAL FILTER
Cutoff frequency
Mode
VC coupling AC DC
VC input 0-1V FS
VC level +/-
HP LP
Input 0-1V FS
Output 1V DC
NOISE GENERATOR
Saturation
Mode
VC coupling AC DC
VC input 0-1V FS
VC level +/-
COMPRESS CLIP
Output 1V DC
Density
Output 1V DC
TEXTURE MIX
Output 1V DC
Mix
DENSITY
Noise
Generator
Mix
H FREQENCY
Horizontal
VC Filter
Mix
V FREQENCY
Vertical
VC Filter
Sample &
Hold
Processor
Mix
   A 2D figure is created by a mix of horizontal and vertical
waveforms.  Visual Cortex’s H, V, and H+V outputs are a good
example of horizontal and vertical waveforms, and a mix of them.
These components make excellent modulation sources for War
Of The Ants.
   Shape generator modules like Shapechanger have a more
complex signal path that allow detailed control over the resulting
shape, and provide separate outputs for the shape and its
horizontal and vertical components.
   Patch the horizontal and vertical components of your shape,
whatever their source, into the horizontal and vertical filter VC
inputs on War of the Ants. Patch the H and V mix, or a variation of
it, into the Density VC input.   Adjust the VC level controls for the
desired look.
   Use a mixer module such as Color Chords, Passage, or Bridge,
to combine the Texture output with the H and V mixed shape.
