# Visual Cortex (Expedition series)

Source: lzxindustries/lzxdocs — official LZX documentation PDFs. Extracted text (diagrams/panel art not included).

## Basic Patches

BY ELIZABETH KAY LARSEN
VERSION 1.0 – DECEMBER 10TH  2014

CORTEX BASICS 00. DEFAULT SETTINGS
CORTEX BASICS 01. VIDEO INPUT & OUTPUT
CORTEX BASICS 02. MANUAL TRANSITIONS
CORTEX BASICS 03. TRIGGERED TRANSITIONS
CORTEX BASICS 04. AUTOMATED TRANSITIONS
CORTEX BASICS 05. RGB OFFSET
CORTEX BASICS 06. RGB GAIN
CORTEX BASICS 07. MATTE GENERATION
CORTEX BASICS 08. MATTE COLOURIZER
CORTEX BASICS 09. SPECTRUM COLOURIZER
CORTEX BASICS 10. LUMA KEYING
CORTEX BASICS 11. WIPE & SHAPE GENERATION
CORTEX BASICS 12. LINEAR COMPOSITING
CORTEX BASICS 13. SOLARIZE & NEGATIVE EFFECTS

CORTEX BASICS 00. DEF AULT SETTINGS
Before beginning your patching, install the module in your EuroRack case as described in the Technical Manual.  Then, set all the controls and switches to the positions shown below.
Video Camera with
Component (YPbPr) Output
patched to Input Decoder
Output Encoder patched to
Television Display with
Composite Video Input
Input Decoder RGB outs patched to
Compositor Channel A inputs
Make sure the lock LED lights up!
If there’s no response from the
lock LED after connecting your
camera, check that the
“Genlock Source” switch on the
rear of the module is set to
“Decoder.”
A DVD player or other video
 source will also do the job.
Slider is in its leftmost position.
CORTEX BASICS 01. VIDEO INPUT & OUTPUT
What you’ll need:
- A camera or DVD player with
Component (YPbPr) video outputs.
- A video display, such as a television.
- RCA cables designed for video. Triple
cables designed for Component video
are nice to have.
- Some 3.5mm patch cables of
various lengths.
In this patch, we’ll connect an external video source, such as a Camera or DVD player, and a video display.
Move the slider left and right to crossfade between Channel A (the video source)
and Channel B (black, because there is no input to Channel B.)
The control voltage being generated
by the Animation & Key Generator
is automatically connected to the
Composite input of the Colourizer &
Compositor section here.  Inserting
a cable into the Composite jack will
cancel this default connection.
This type of automatic connection
is usually referred to as a “switched”
or “normalled” connection.  It is
insinuated by the dotted line between
input and output.
CORTEX BASICS 02. MANUAL TRANSITIONS
Rotate the in and out controls clockwise
to increase the amount of lagged
response when you move the slider.
Try each knob halfway up to start.
As you move the slider quickly left
or right, the transition will slowly
follow your movements.
In this patch, we’ll learn how to fade the input video source to black, by using the Animation & Key Generator section’s slider to control the Colourizer & Compositor section.
Leave the slider in its leftmost or rightmost position to start.
Moving the slider towards the center will decrease the output range.
CORTEX BASICS 03. TRIGGERED TRANSITIONS
The Out control will change the speed of
the transition from B to A.
The In control will change the speed of
the transition from A to B.
Press the pushbutton to trigger a
transition! Each time this button is
pressed, the slider position is inverted
(or returned to a non-inverted state.)
This toggling behavior is known in
electronics terms as a flip-flop.
A clock or gate signal (or any voltage)
may be connected to the trigger input
jack.  When the input rises past the
threshold voltage (0.5V), the
pushbutton action is triggered.

Hint: Send this a pulse from your
audio sequencer, to generate
transitions synchronized to music!
In this patch, we’ll learn how to trigger automatic translations from Channel A to Channel B, and back again -- as well as vary the speed of the transitions.
The slider has a special function while in Cycle mode.  It controls the amplitude of the output waveform.
In the center position, the output is at 100% gain.  Moving the slider to the left will decrease this gain to 0%.
Moving the slider to the right will increase the gain.
Hint: Higher gain values will create a “rise” ... “pause” ... “fall” .. “pause” type of response.
CORTEX BASICS 04. AUTOMA TED TRANSITIONS
The Out control will change the
speed of the falling voltage.
In Cycle mode, the pushbutton and
trigger input will reset the output
waveform to zero.
Hint: This allows you to synchronize
automated transitions with the start
of a sequencer or similar device.
Turn Cycle mode on by flipping
this switch to its up position!
In Cycle mode, the output will
bounce back and forth without
any need for manual triggering or
slider control.
1V
0V
The In control will change the
speed of the rising voltage.
1V
0V
In this patch, we’ll learn how the Animation & Key Generator section’s Cycle mode works, and how to use it to create automatically cycling transitions.
Turn the Mix-to-Channel A switch on, in its up position.
Doing this means that the outputs of the RGB knobs
will be added to the Channel A RGB inputs.
Before starting this patch, reset everything to positions found in CORTEX BASICS 01. VIDEO INPUT & OUTPUT.
Don’t forget what you’ve learned about generating transitions, however!  Revisit those techniques as you explore the rest of these patches.
CORTEX BASICS 05. RGB OFFSET
Rotating the RGB controls clockwise from center
will add to the brightness of the color channels in question.
Rotating the RGB controls counter-clockwise from center
will subtract from the brightness of the color channels in question.
In this patch we’ll use the Colourizer & Compositor’s red, green and blue controls to adjust the color balance of the Channel A input by adding or subtracting an offset voltage.
Set the Composite mode switch to the
upper position, Multiply.  In this mode
the values of Channel A are multiplied
by the values of Channel B.  In this
particular configuration, that means
the RGB controls will function to
set the color levels of the incoming
video feed.
CORTEX BASICS 06. RGB GAIN & INVERSION
Rotating the RGB controls clockwise from center
will increase the contrast of the color channels in question.
Rotating the RGB controls counter-clockwise from center
will increase the contrast of the color channels in question,
and also subtract them.  Since the signal is now below black,
you won’t see it.  But it’s still there... keep that in mind later,
when we’re discussing the solarize effect.
In this patch we’ll use the Colourizer & Compositor’s red, green and blue controls to adjust the gain and inversion of each color channel of the video input.
Turn the Mix-to-Channel B switch on, and make sure the
Mix-to-Channel A switch is now off.  This means we’ll have the
camera input on Channel A, and the RGB control values on Channel B.
Set the Composite mode back to its
center position (fade mode.)
CORTEX BASICS 07. MA TTE GENERA TION
Rotating the RGB controls clockwise from center
will increase the brightness of the color channel in question.
In this patch we’ll use the Colourizer & Compositor’s red, green and blue controls to create a flat color field.
Turn the Mix-to-Channel B switch on, and make sure the
Mix-to-Channel A switch is now off.  This means Channel B
will consist of the RGB control outputs.
Slider in rightmost position (Channel B.)
Elaborating on this patch:
With the video input reconnected, you
can fade the video source to the matte
color, instead of just fading out to black.
CORTEX BASICS 08. MA TTE COLOURIZER
Rotating the RGB controls clockwise from center
will increase the brightness of the color channel in question,
only this time, we are controlling the level of the Coulourize
input signal, and not a static offset value.
In this patch we’ll use the Colourizer & Compositor’s red, green and blue controls to mix a monochrome video source to our desired color.
We are using the Luma output from
the input decoder in this patch.
The Luma signal represents the
brightness of the input source only,
and ignores any information about
color hue or saturation.  In other
words, it is the black & white version
of the input video.
CORTEX BASICS 09. SPECTRUM COLOURIZER
Rotating the RGB controls clockwise from center
will increase the brightness of the color values split by the Spectrum function.,
and then add them to Channel B.
In this patch we’ll use the Colourizer & Compositor’s red, green and blue controls to map the grayscale values of a video signal to red, green and blue color channels.
Turn the Spectrum mode on by
setting this switch to its up position.
In Spectrum mode, the grayscale
values of the Colourize input signal
are split into the different colors.
This means that the brightest values
of the input signal become red.
The middle gray values become green.
And the darkest values become blue.
Since there are no hard edges
between the color transitions,
this process in video art is known
“linear colourization.”
CORTEX BASICS 10. LUMA KEYING
In this patch we’ll use the key function of the Animation & Key Generator section to generate a luma key, and use that key to switch in the source video.
Patch the Luma signal to the input of
The Animation & Key Generator
section, and set the key mode switch
to its up position (positive key.)
In this mode, when the grayscale
values of the input signal are below the
keying threshold set by the slider, the
key will be off (channel A selected.)
When the grayscale values of the input
signal are ABOVE the keying threshold,
the key will be off (channel B selected.)
The slider now controls the keying threshold.
P.S. Don’t forget to try negative
key mode as well!
CORTEX BASICS 11. WIPE & SHAPE GENERA TION
In this patch we’ll use the key function with waveforms from the Ramp Generator, to generate wipe and key shapes.
This patch functions the same
as the luma keying patch,
only we are going to use
video waveforms from the
Ramp Generator section as our
source image.
Try all four outputs from the
Ramp Generator, and play with
all the switch settings to see
their differences.
Hint: If you have a basic mixer
module in your synthesizer, try
mixing the ramp outputs with audio
sources to generate modulation before
patching them to the key input.
P.S. Don’t forget to try negative
key mode as well!
CORTEX BASICS 12. LINEAR COMPOSITING
In this patch, we’ll play with the Ramp Generator outputs, patching them into the Colourizer & Compositor to get complex color gradients and linear transition masks.
This patch is more about exploring
possibilities.  Try patching outputs
from the Ramp Generator section
to ANY of the inputs in the
Colourizer & Compositor section.
Play with the Mix switches,
Spectrum, and Composite modes
as you explore.
We’ll examine advanced compositing
techniques in future guides, but
that shouldn’t stop you from
exploring.(Pssst!  Find out what this
signal looks like.  It’s neat.)
By adding negative color offsets to the input channel,
you are able to push the outputs below black.  When
Solarize mode is engaged, the voltages going below black
will be re-inverted, appearing as part of the image again.
This is great for psychedelic color effects.
Before starting this patch, reset everything to positions found in CORTEX BASICS 05. RGB OFFSET.
CORTEX BASICS 13. SOLARIZE & NEGA TIVE EFFECTS
In this patch we’ll try out the two output effect modes in the Colourizer & Compositor sections: Solarize, and Negative.  This concludes our series of basic patch techniques.
The Negative effect is simple.
It subtracts all color values from
their maximum value, inverting them.
Black becomes white, white becomes
black.  Dark red becomes light red,
etc.
The Solarize switch creates an
effect similar to photographic
solarization.  Color channel values
below black (such as when a signal
is subtracted from zero), will
be inverted, becoming positive again.
In electronics terms, this process
is called full wave rectification.
This, combined with the Spectrum
function, are the primary tools
for psychedelic colour mixing using
the Visual Cortex.

## Technical Manual

BY ELIZABETH KAY LARSEN
VERSION 1.1 – DECEMBER 9TH 2014

TABLE OF CONTENTS
DEAR VIDEO ARTIST .......................................................................................................................................................................................................................................... 3
TECHNICAL SPECIFICATIONS ................................................................................................................................................................................................................... 4
MODULE INSTALLATION .............................................................................................................................................................................................................................. 4
VIDEO SYNC CONNECTIONS ....................................................................................................................................................................................................................... 5
SYNC GENERATOR ................................................................................................................................................................................................................................................ 6
RAMP GENERATOR ............................................................................................................................................................................................................................................ 7
ANIMATION &  KEY GENERATOR ....................................................................................................................................................................................................... 8
COLOURIZER & COMPOSITOR ................................................................................................................................................................................................................. 9
INPUT DECODER ..................................................................................................................................................................................................................................................... 10
OUTPUT ENCODER................................................................................................................................................................................................................................................. 11
EXPANSION & PROGRAMMING HEADERS .......................................................................................................................................................................... 12
WARRANTY .................................................................................................................................................................................................................................................................  13

DEAR VIDEO ARTIST
Our world moves rapidly at the pace of progress – ravenous for the highest definition, the largest display,
and the fastest data transfers. In our hunger for new technology, we have left behind a vast expanse of
unexplored dimensions and forsaken possibilities.
But not you, Video Artist. You’re looking in a different direction. Not ahead, not behind, but parallel. You
are a pilot, prepared to man the controls of a time machine.
Your video synthesizer is a retro-futuristic vessel outfitted to explore faraway vistas from the era of
analogue television. From your seat in the cockpit you will unveil prismatic motions, expose mesmerizing
geometries, and witness hypnotic entities never before seen. Swimming behind the diffused warmth of
the cathode ray glow, living images linger, waiting for you.  It takes guts to do what you do – many will say
your path is absurd.
Thank you, Video Artist, for supporting our continuing efforts at LZX Industries to create new tools and
workflows for the timeless medium of analogue video synthesis. Visual Cortex marks a new generation of
our products, encapsulating several years of obsessed development and prototyping. While Visual Cortex
forms the foundation of a modular system, it is also a powerful tool on its own – everything you need to
learn the basics of video synthesis is right here.
Our work would not be possible without the pioneers of video art in the 1960s, 1970s and 1980s. Thes e
wonderful human beings cast the first rays that continue to inform and inspire us, and we owe them our
gratitude: Bill Etra, Bill Hearne, Daniel Sandin, Dave Jones, Denise Gallant, Eric Siegel, Jim Wiseman,
Nam June Paik, Kim Ryrie, Peter Vogel, Phil Morton, Richard Monkhouse, Rob Schafer, Sherry Hocking
& Ralph Hocking, Shuya Abe, Stephen Beck, Stephen Jones, Steve Rutt, Steina & Woody Vasulka and
countless others. With our work, we endeavor to continue the legacy of these visionaries and their tools.
All of us here at LZX Industries send our love and excitement to you and your companions … we’re
counting on you, Video Artist. We can’t wait to see what you discover out there.
Over and out,
Elizabeth Kay Larsen
December 9th, 2014

Acknowledgments

Product Design & Development Elizabeth Larsen, Edward Leckie
Assembly Technicians Jonah Lange, Heather Larsen, David Townsend, Saschenka Lopez
Manufacturing & Distribution Joshua Holley, Rico Loverde, Paul Baker, Sarah Holley, Anna Sitko, and
everyone else at Darkplace Manufacturing in Portland, Oregon
Additional Graphic Design  Adam Fuchs, Hannes Pasqualini – Papernoise
Special Thanks Johnny Woods, Jennifer Juniper Stratford, Sam Newell, Nick Bartoletti, Jason
Nanna, Tommy DOG Prinz, Jordan Bartee, Dan Green, Aaron White, Marcus
Webb, Todd Larsen, Paul Baker, Chad Allen, Malcolm Elijah Welbourne,
Stephi Duckula, Scott Jaeger, Chris King, David Wagenbach, Shawn Cleary,
Kylie Frame, Alex Peverett, Paul Millar and countless others

TECHNICAL SPECIFICATIONS
Mechanical

Width 26HP, 5.2 inches
Height 3U EuroRack Standard
Mounting Depth 1.75 inches
Power Connector 16-pin Male IDC Connector
Included Accessories (4) M3 x 6mm Mounting Screws, (1) 16-pin EuroRack Standard Power Cable

Power

+12V Power Consumption 180mA
-12V Power Consumption 230mA

Inputs and Outputs

Internal Signals (3.5mm Jacks) 0-1V, DC Coupled, +/-12V tolerant, high bandwidth
0.5V threshold for trigger inputs
External Signals (RCA & S-Video Jacks) 1V after 75R input termination, AC Coupled, high bandwidth

Video Timing

FORMAT NTSC/480i PAL/576i
H Sync Frequency 15,734KHz 15,625KHz
H Sync Pulsewidth 4.7uS 4.7uS
V Sync Frequency 59.94Hz 50Hz
Frame Clock Frequency 29.97Hz 25Hz
Total Scanlines 525 625
Active Scanlines 480 576
Active Pixels 720 720
Frame Clock Frequency 29.97Hz 25Hz
Total Scanlines 525 625
MODULE INSTALLATION
1. Remove module, mounting screws, and power cable from their packaging.  Visually inspect all pieces
to ensure there is no obvious damage, such as broken connectors.

2. Power down your synthesizer and disconnect the power cable from the wall outlet.

3. Attach the included power cable to the module’s power connector, then connect the other end to the
power distribution bus in your EuroRack synthesizer case as shown below.

4. Position the module on the mounting rails in your EuroRack synthesizer case and screw down all four
mounting screws.  After double checking your connections, power your synthesizer back up.

VIDEO SYNC CONNECTIONS
When dealing with analogue video in a hardware environment, synchronization and timing is very
important.  Any devices with video input and output connections must be synchronized to each other in
order to combine the video signals in the same domain.  One device must serve as the synchronization
master, providing timing references for all the other devices.  Typically, this device is the Visual Cortex.

Connecting Additional Video Synthesizer Modules

Many video synthesizer modules require access to the synchronization signals.  Previous releases by
LZX Industries used a 14-pin IDC cable to distribute these signals.  The Visual Cortex includes an output
header in order to retain compatibility with these modules.  Visual Cortex and future releases will use
standard video connectors to distribute synchronization timing.

Connecting External Video Input And Display Devices

Whenever an external video input is used with the Visual Cortex, one of two conditions must occur:
1) The external device must serve as the master source, slaving the Visual Cortex’s timing to its own.
2) Or, the external device must be genlocked and synchronized to the timing of the Visual Cortex.
Since most video devices do not have a genlock input feature, option 1 will be the most common case.  In
the case of option 1, please ensure that the sync source selection switch on the rear panel (see the Sync
Generator section) is set to “Decoder,” so that synchronization will be derived from the Decoder input
rather than the rear panel sync input.

If additional video inputs are desired, consider purchasing the LZX Color TBC module.  This module
provides composite video decoding and time base correction of an external source, meaning that genlock
is no longer a concern.

SYNC GENERATOR
The Sync Generator section is a broadcast specification video sync generator which can operate in
NTSC/480i or PAL/576i timing formats.  It can provide the master timing reference for an entire video
synthesizer system, and its timing may be synchronized to an external video source.

Frontpanel

A. Sync Format LED Indicators. Indicates NTSC or PAL mode.
B. Sync Lock Status LED Indicator. Green when locked to external sync, red
when external sync is detected but no lock can be achieved.
C. Horizontal sync output jack. A pulse at the beginning of each video scanline.
D. Vertical sync output jack. A pulse at the beginning of each video field.
E. Frame rate clock output jack. A gate is turned on at the beginning of each odd
field (the start of a new frame), and off at the beginning of each even field.
F. Dither pattern output. A dithered pixel texture for shading video objects. The
spatial geometry of the texture is influenced by the selected Ramp Generator
modes.

Rear

A. Video format selection switch. Selects between NTSC/480i and PAL/576i video formats.
B. External sync source selection switch. Selects between Input Decoder or rear Sync In (C).
C. Sync In jack. A video input for external synchronization.
D. Sync Out jack. A black video output containing only synchronization pulses.
E. 14-pin LZX Sync Distribution Bus output. A 14-pin sync output for providing sync to previous LZX
Industries products which require it.
F. Sync-to-Power Bus selection switch.  When on, these switches send horizontal and vertical sync
pulses to the CV and Gate pins on the 16-pin power connector.

Block Diagram

RAMP GENERATOR
The Ramp Generator section is a dual synchronized waveform generator.  It generates grayscale
gradients in horizontal and vertical outputs, with selectable output waveshapes.  These signals provide
the basis for many shape and pattern generation techniques.

Frontpanel

A. Mirror mode switch. Controls symmetrical mirroring (ramp-to-triangle).

B. Shape mode switch. Controls the waveshape of the outputs.

C. Horizontal waveform output jack.
D. Vertical waveform output jack.
E. Sum output jack. Horizontal and vertical waveforms summed together.
F. Difference output jack. Vertical waveform subtracted from horizontal waveform.

Block Diagram.

Up H & V outputs mirrored
Center No outputs mirrored
Down H output mirrored
Up Logarithmic
Center Linear
Down Exponential

ANIMATION &  KEY GENERATOR
The Animation & Key Generator section is a multi-function control voltage generator, designed
specifically for controlling transitions between two video images.  It can function as a manual controller
with slew, a flip-flop based envelope generator, or a low frequency oscillator. The key function enables a
high-speed comparator, which generates a hard key image suitable for shape generation or luma keying.

Frontpanel

A. Slider control. Action dependent on mode:

B. In time control. Sets the speed at which the output
voltage rises to the target value.
C. Out time control. Sets the speed at which the output
voltage falls to the target value.
D. LED indicators. Two color visual indication of target
value and output voltage.
E. Pushbutton switch. Action dependent on mode:

F. Trigger input jack. On the rising edge of the input signal, the pushbutton (E) action is triggered.
G. Primary Input jack. Function dependent on mode:
Key Modes Off Adds to the target value set by the slider control (A).
Key Modes On Key generator input source.

H. Primary Output jack. Output signal dependent on mode:
Key Modes Off Control voltage output
Key Modes On High speed video logic output, 0V = low, 1V = high

I. Key mode switch. Switches between positive key generator mode on (+KEY), key modes off (center)
and inverted key generator mode on (-KEY.) While key modes are on, the internally generated control
voltages become the key generator threshold.
J. Cycle mode switch. Turns automatic cycling mode on or off.

Block Diagram

Key Modes Off Sets target value 0-1V
Key Modes On Sets output amplitude
Cycle Mode Off  Toggles inversion of target value
Cycle Mode On Resets output waveform

COLOURIZER & COMPOSITOR
The Colourizer & Compositor section is a voltage controlled analogue video mixer.  It features two RGB
input channels, individual RGB controls and several advanced colour processing effects.  We designed
this section to be capable of addressing all the essential colour mixing required for a small to medium
sized modular video synthesis system. The output of this section is sent directly to the Output Encoder .

Frontpanel

A. Channel A RGB input jacks. RGB inputs to Channel A.
B. Channel B RGB input jacks. RGB inputs to Channel B.
C. Composite input jack. Voltage control over the selected
Composite mode (D).
D. Composite mode switch. Selects formula used to
combine Channel A (A) and Channel B (B):

E. RGB colour controls. Clockwise rotation adds the
selected colour, while counterclockwise subtracts.
F. Colourize input jack. Voltage source of the RGB colour controls (E). Connected to 1V by default.
G. Mix A on/off switch. Adds the output of the RGB colour controls (E) to Channel A (A).
H. Mix B on/off switch. Adds the output of the RGB colour controls (E) to Channel B (B).
I. Spectrum on/off switch. Translates the value of the Colourize input (F) to colour channels:

J. Solarize on/off switch. Inverts all color values below 0V.
K. Negative on/off switch. Subtracts all color values from 1V.

Block Diagram

Multiply  (A*B)+((1-B)*VC)
Fade (center) (A*(1-VC))+(B*VC)
Sum A+((-B*(1-VC))+(B*VC))
VC = Composite input signal (C).
0V – 0.5V Red 0%
Green 0% to 100%
Blue 100% to 0%
0.5V – 1V Red 0% to 100%
Green 100% to 0%
Blue 0%

INPUT DECODER
The Input Decoder section is an analogue video input amplifier and colorspace converter.  This section
accepts YPbPr analogue component video, and processes it for patching internally inside a video
synthesis system.  The Y input can be used with Composite video signals if only grayscale operation is
desired.

Frontpanel

A. Component YPbPr input jacks. Component YPbPr video inputs for external
video gear.  If no Component source is available, a Composite (NTSC/PAL CVBS)
signal can be input to the Y jack independently.  In that case, only grayscale video
will be passed to the outputs.
B. Luma output jack. This output is full scale video representing the grayscale
brightness of the source video signal.
C. RGB output jacks. These jacks output the Red, Green & Blue color channels of
the source video feed when a Component YPbPr source is used.

Block Diagram

OUTPUT ENCODER
The Output Encoder section takes the output of the Colourizer & Compositor section, converting
signals inside your video synthesizer into standard video signals which may be displayed and recorded.

Frontpanel

A. Composite video CVBS output jacks. Both jacks output identical video
signals.
B. S-Video Y/C video output jack. Separate luma (Y) and chroma (C) signals to
S-Video format Mini DIN 4 jack.
C. Component YPbPr video output jacks. Component video outputs for the
highest quality full color analogue signal path.

Rear

A. Black Level Adjustment trimmer. Adjusting this trimmer will adjust the
brightness level of all the encoder outputs when calibrating for displays and
recording devices.

Block Diagram

EXPANSION & PROGRAMMING HEADERS
Visual Cortex contains many connectors accessible via the rear of the module.  LZX Industries will not
offer technical support or service for use of these headers, but savvy users may be able to tap into them
and find them useful for custom applications.

Rear

A. JTAG programming header. For uploading firmware to the Xilinx XC2C256.
B. AVRISP programming header. For uploading firmware to the AVR Atmega32A.
C. Video IO connections header 1. For wiring external connectors.
1, 3, 5, 7, 9, 11, 13, 15 GND
2 Output Encoder, S-Video Y Out
4 Output Encoder, S-Video C Out
6 Output Encoder, CVBS Video 1 Out
8 Output Encoder, CVBS Video 2 Out
10 Output Encoder, Component Y Out
12 Output Encoder, Component Pb Out
14 Output Encoder, Component Pr Out

D. Video IO connections header 2. For wiring external connectors.

E. RGB expansion header. Direct access to the RGB channels before encoding.
1, 2, 3, 5, 7, 9, 10, 11,
12, 13, 15
GND
4 Input Decoder, Component Y In
6 Input Decoder, Component Y In
8 Input Decoder, Component Y In
14 Sync Generator, External Sync In
16 Sync Generator, External Sync Out

WARRANTY
This product is covered by LZX Industries’ warranty, for one year following the date of manufacture. This
warranty covers any defect in the manufacturing of this product. This warranty does not cover any
damage or malfunction caused by incorrect use – such as, but not limited to, power cables connected
backwards, excessive voltage levels, or exposure to extreme temperature or moisture levels.
The warranty covers replacement or repair, as decided by LZX Industries. Please contact customer
service via our website (http://www.lzxindustries.net) for a return authorization before sending the module.
The cost of sending a module back for servicing is paid for by the customer.
