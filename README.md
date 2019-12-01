# RabbitPie
Proof-of-Concept Bash Bunny Emulator on Raspberry Pi Zero W Hardware

Adapted from iStickToIt tutorial (http://www.isticktoit.net/?p=1383) and Linux Kernel USB Gadget Documentation (https://www.kernel.org/doc/Documentation/usb/gadget_configfs.txt)

KB0.py, written by Neil Austion, simplifies a lot of the usual hex code slinging required for HID devices, at the expense of violating a ton of Python conventions. You'll get over it, though.

gremlin.py is adapted from a Bash Bunny script, also written by Neil Austin, to annoy students who forget to lock their computers before taking breaks. RabbitPie doesn't do Ducky Script yet, but I'll write a parser when I get bored enough.

NOTES: if you're connecting your RPi0W to your computer through a USB port, then SSHing into it, there's a good chance you've configured the g_ether module in /boot/cmdline.txt, and if you're anything like me, you've spent way too much time wondering why Linux refuses to load hidg0, despite the fact that you've followed all of the instructions to the letter. Do yourself a favor; make sure you can access your RPi0W over wifi, then remove g_ether from /boot/cmdline.txt.

Now think about the possibilities of a wireless connection to a Bash Bunny at 1/10 the cost. As an instructor, I'm thinking 'bad-ass presentation clicker', but you probably have other ideas.

Anyway, this is very much a work in progress.
