# Curtain (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## Owners Manual

CURTAIN
OWNER’S MANUAL
Enhance!
Designed to increase the contrast of the edges of objects, analog video enhancers have a history dating back to early medical and
military imaging systems.   Doctors have used video enhancers to analyze x-rays, and NASA has used them to process some of the first
electronic images of space and the moon.  In contemporary times, circuits such as the Curtain module have been replaced by sophisti-
cated high resolution digital image processing, but the visual appeal of time-constant based processing of analog signals remains.
Our Triple Video Multimode Filter module was our first prototype of a video rate, fully voltage controlled filter design.  After patching this
module in countless ways and thorough study of vintage processors such as the FOR-A IV530 Contour Synthesizer, the signal path for
an updated design became clear.  Curtain integrates a high pass VCF and a voltage-controlled output mixer which sums the filter output
with its original input (or an alternate source.)  Since subtracting a high pass output from its input yields a low pass, modulating the
inverting/non-inverting depth of the high pass filter into this mix allows one to go from sharpening to blur all on a continuous voltage
control.  In this sense Curtain controls not only the time constant of the analog processing effect, but also its depth in the output mix.
I am excited to see how you use this new filter design in concert with the other linear processors of the Expedition series to add curves,
illusions of depth, and feedback.
Lars Larsen
November, 2016
814 SE 14th Ave.
Portland, OR 97214
USA
Creative tools for video synthesis
and analog image processing.
CURTAIN
OWNER’S MANUAL
Written by Lars Larsen
Published November, 2016.
LZX-CN-OM-V1.0
FEATURES
TABLE OF CONTENTS
SPECIFICATIONS
USER CONTROLS & CONNECTIONS
BLOCK DIAGRAM
MANUFACTURER WARRANTY 6
EXAMPLE PATCHES 5
INSTALLATION 4
Curtain is a video edge processor designed for sharpening, blurring, and outline extraction.  Comprised of a wideband voltage controlled
filter and multiplier, it is similar to tools used for X-Ray analysis in the era of analog graphics.  Curtain is equally useful for processing video
images as it is for adding dimensionality and contours to shapes and patterns.
FEATURES
Voltage controlled filter with 1:100 continuous tuning ratio allows a full sweep from thin to wide time constants.  Three range settings
cover a cutoff range from 100Hz to 5MHz.
Switchable rectifier allows selection of positive rising edges and falling negative edges, both edges positive, rising edge only, or falling
edge only.
Voltage controlled depth allows a continuous sweep of filter output amplitude and inversion.  This enables settings from blur to
sharpen on a single modulation channel.
Separate inputs for the filter and output mix allow edge processing from once source and output mixing with another. Dedicated filter
and mix outputs allow further external processing.
All signal and control paths perform at high frequency, video rate modulation speeds.
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
AC/DC input coupling switches and inverting level attenuators on  voltage control inputs.
Shape mode selection switch (4 positions.)  This switch selects option-
al post-processing for the high pass filter.  In its initial setting (shown)
the high pass filter output is unaffected.  In its second setting, falling
edge spikes are inverted so that both rising and falling edges are positive
voltages.  In the third setting, only rising edges pass through.  In the
fourth setting, only inverted falling edges pass through.
Inverting level control for the mix input jack.  This control sets the level
of the mix input which is added or subtracted from the mix output.
Center is the 0 position. Clockwise from center, and the mix input is
added to the mix output.  Counter-clockwise from center, and the mix
input is subtracted.
Width offset control.  This control sets the cutoff frequency of the high
pass filter.  In visual terms, it changes the width of the edge to be
processed. Fully counter-clockwise, and the cutoff frequency is at its
minimum value (large edge width.) Fully clockwise, and the cutoff
frequency is at its maximum value (small edge width.)
Depth offset control.  This control sets the level and inversion of the high
pass filter to be mixed into the mix output.  Center is the 0 position.
Clockwise from center, and the filter output is added to the mix output.
Counter-clockwise from center, and the filter output is subtracted.
Voltage control AC/DC coupling switches.  In AC mode, slow moving
voltages are removed from the input signal and only high frequency
content remains.
Frequency range switch for high pass filter.  This 3-position switch
selects the cutoff frequency range for the high pass filter.  In it’s leftmost
position, the filter is in the upper end of the audio/vertical range.  In it’s
middle position, cutoff extends from the beginning of the horizontal
range to its middle point (somewhat thin lines.)  In the rightmost
position, the range extends to the upper limits of video bandwidth.
USER CONTROLS & CONNECTIONS
Width external voltage control input. 0-1V DC full scale. The depth of modulation is set by the associated inverting level control (4).8
Primary signal input for the high pass filter. 0-1V DC expected.  When the mix input (12) is unpatched, the signal input to the filter input
jack will be automatically connected to the mix input (12) as well.
Depth external voltage control input. 0-1V DC full scale.  The depth of modulation is set by the associated inverting level control (4).10
Direct output from the high pass filter, +/-1V DC variable output.   Use this for extending the processing chain to include feedback or
other components.
Inverting level controls.  These controls set the depth of external voltage
control modulation applied to the associated parameter.  In their center
positions, the output is 0.  Adjusted clockwise from center, the signal is
added to the associated parameter.  Adjusted counter-clockwise, the
signal is subtracted.
Mix input. 0-1V DC expected.  When the mix input is unpatched, the signal input to the filter input jack (9) will be automatically
connected to the mix input as well. The depth of of the mixed signal is set by the associated inverting level control (2).
Mix output.  0-1V DC full scale.  This is the primary output of this module, and includes a mix of the high pass filter input and the signal
at the mix input.
BLOCK DIAGRAM
Filter In High Pass
VCF Rectifier Filter Out
Width & Range
Controls
Shape Mode
Selection
4 Quadrant
Multiplier
Depth Control
Mix In
Mix Out
Mix Level
Control
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
Analog sharpen and blur processing can be applied to both external image processing and shape/pattern sculpting techniques.  Applied to
the output of a flat (hard key) generator as demonstrated in this patch, it allows one to sculpt contours onto a flat surface, creating a more
textured or three dimensional object.
Output to display.
Mix out sent to
Composite VC in on
Visual Cortex.
SHAPE GENERATOR EDGE SHARPENING & BLUR CONTROL
Further exercises and experiments to explore using this patch as a starting point:
Play with width, depth, and mix level controls to get a feel for how they interact.  Try the different range and shape mode settings.
Instead of the key generated by the H+V ramp mix, use external video as the input source to Curtain.
Apply voltage control to width.  Ramp generator outputs (from Cortex) and external VCOs make great sources.
Apply voltage control to depth.  Ramp generator outputs (from Cortex) and external VCOs make great sources.
Try using other shapes and key generator outputs as modulation sources or mix inputs.
Mix a variable amount of the filter output into the signal being sent to the filter input, to generate feedback ringing and repetitions.
Passage is a good module to use as a utility mixer.
H+V ramp mix
sent to Cortex
Key generator in.
Cortex key gen
sent to Curtain
filter/mix inputs.
Try patching the filter and mix outputs to separate colors.
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
