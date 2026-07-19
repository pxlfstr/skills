# Doorway (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## Owners Manual

DOORWAY
OWNER’S MANUAL
OVER, UnDER & THRU
Key generators are the bread and butter of creativity in video and imaging systems.  From the alpha channel compositing and matte
control of modern software packages back to the primitive wipe generators of broadcast consoles, keys are the thing.  Doorway is very
exciting for me because it is tuned specifically for fully controllable shape and line generation, and complex combinatorial joining of
multiple keys together.  Through multiple Doorways, a complex 2D figure can be generated and composited together from simple
horizontal and vertical ramp generators.
My focus going into designing the Expedition series modules has been to embrace what makes analog video processing unique and
irreplaceable: continuous, linear functions.   It only makes sense that the series’ signature key generator module should be a soft keyer.
Doorway’s key is generated through high gain amplification of the input signal around a threshold point.  Unlike a hard key generator,
there is no comparator, digital logic, or on/off state in the binary sense.  The edge of the key itself, and its softness/width, are composed
of the input signal itself with it’s contrast blown way out of proportion to the typical brightness scale.
Likewise, rather than an inversion/negative key function or output, this positive and negative spaces of the key can be set to any
grayscale value, or external sources can be inserted.  This allows the joining of multiple keys together in various alpha compositing
modes: over, under, in, XOR, etc.
I’m excited to see what you find on the other side of this Doorway.
Lars Larsen
November, 2016
814 SE 14th Ave.
Portland, OR 97214
USA
Creative tools for video synthesis
and analog image processing.
DOORWAY
OWNER’S MANUAL
Written by Lars Larsen
Published November, 2016.
LZX-DW-OM-V1.0
FEATURES
TABLE OF CONTENTS
SPECIFICATIONS
USER CONTROLS & CONNECTIONS
BLOCK DIAGRAM
MANUFACTURER WARRANTY 6
EXAMPLE PATCHES 5
INSTALLATION 4
Doorway is a linear video key generator and compositor, also known as a soft keyer.  A typical video key is generated using a comparator
circuit, where the ouput is a binary state: on or off.  Doorway instead achieves key generation via high gain amplification and clipping of the
input source.  The edge of the resulting key is therefore composed of a variable percentage of the input signal, centered around the thresh-
old point.
FEATURES
Voltage controlled threshold across the full input range. Video rate modulation paths allow displacement of the threshold by another
shape or image source.
Voltage controlled gain amplifies input signal up to a gain of X64, enabling a continuous sweep from fully soft to fully hard edge.
Foreground and background level controls and signal inputs allow the negative and positive space of the resulting key to be set to any
grayscale level, or be filled with external signals.  This aids the compositing of multiple shapes and patterns.
Outline mode switches a full wave rectifier into the signal path.  In this mode, gain controls the width of the outline rather than the
softness of the key's edge.
AC/DC input coupling switches and inverting level attenuators on  voltage control inputs.
SPECIFICATIONS
EuroRack Synthesizer Module
10HP
1.25 inches (31.75 mm)
80mA
80mA
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
Background offset control.  This control sets a grayscale level to be
applied to the negative space of the output key.  Fully counter-clock-
wise, the level is set to 0V (black.)  Fully clockwise, the level is set to 1V
(white.)
Foreground offset control. Functions as (1) but for the positive space of
the output key.
Threshold offset control.  This control sets the center of the grayscale
level at which the input source is amplified into the output key.  Fully
counter-clockwise, the threshold value is -0.1V.  Fully clockwise, the
threshold value is 1.1V.
Gain offset control.  This controls the gain of the input source around its
threshold value, effectively setting the width or softness of the output
key’s edges.  Fully counter-clockwise, the gain is 1X (fully soft edge).
Fully clockwise, the gain is 64X (very hard edge.)
Voltage control AC/DC coupling switches.  In AC mode, slow moving
voltages are removed from the input signal and only high frequency
content remains.
Outline/Solid mode switch.  When in its downward position, the key
generator functions normally.  When in its upward position, key values
above white will be inverted.  This creates a window around the thresh-
old voltage, allowing just the outline of the key to pass through.
USER CONTROLS & CONNECTIONS
Threshold external voltage control input. 0-1V DC full scale. The depth of
modulation is set by the associated inverting level control (4).
Primary source signal input for frequency multiplier. 0-1V DC expected.9
Gain external voltage control input. 0-1V DC full scale.  The depth of modulation is set by the associated inverting level control (4).10
Background external input.  The signal input into this jack will add to the brightness set by the background offset control (1).  This
allows an external key, pattern, or other source, to be inserted into the negative space of the output key. 0-1V DC expected.
Inverting level controls.  These controls set the depth of external voltage
control modulation applied to the associated parameter.  In their center
positions, the output is 0.  Adjusted clockwise from center, the signal is
added to the associated parameter.  Adjusted counter-clockwise, the
signal is subtracted.
Key output.  0-1V DC level.12
Foreground external input.  Functions as (11) but for the positive space of the output key. 0-1V DC expected.13
BLOCK DIAGRAM
Source In Difference
Amplifier
High Gain
VCA
Key Out
Threshold Control Gain Control
Outline
Function
Output
Compositor
Foreground/Background
Controls & Inputs
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
Key generators in an video environment are a vital function.  They can take a gradient like horizontal and vertical ramps and turn them into
hard edged wipes and shapes.  They can take an external video source and identify positive and negative space used for luma keying or
chroma keying techniques.  In this patch, we explore simple wipe generation: creating a diamond shape which can have its size and edge
width separately controlled.  After you patch this up, play with the threshold and gain controls.
Output to display.
Key out sent to
RGB in on
Visual Cortex.
SHAPE GENERATOR WITH SIZE & EDGE SOFTNESS CONTROL
Further exercises and experiments to explore using this patch as a starting point:
Try different ramp switch settings on the Visual Cortex to generate a circle, diamond, star, or triangle.
Instead of the H+V ramp mix, use external video as the input source to Doorway to generate a luma key.
Apply voltage control to threshold.  Alternate ramp generator outputs (from Cortex) and external VCOs make great sources.
Apply voltage control to gain.  Alternate ramp generator outputs (from Cortex) and external VCOs make great sources.
Flip the outline mode switch and see how it effects the output with and without modulation.
Play with the foreground/background level controls.  Set them opposite the image shown to generate a negative key.  Insert different
ramps, mixes, and video sources into the foreground and background input jacks.
H+V ramp mix
sent to source
input on Doorway.
Instead of patching the key into one channel of the Cortex, use it to control the whole Cortex compositor by patching it into the Coloriz-
er & Compositor section’s VC input jack.  Use the Cortex’s animation control section’s output to control the Threshold of Doorway.
Use a vertical ramp as a source (Cortex switches centered.)  Switch Doorway to outline mode.   Turn up gain.  You will see a single
vertical line.  Modulate threshold of Doorway with an external audio source to get an oscilloscope style audiovisualization display.
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
