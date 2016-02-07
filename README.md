# liblovense

liblovense is a library for controlling Lovense sex toys, such as the
Max, Nora, and Lush. The library allows users to control all aspects
of the toy (vibration/rotation/inflation, depending on the toy), as
well as retrieving information like device type, status, battery
level, and accelerometer readings.

## Usage

Currently, the library consists of a Python module for controlling
Lovense toys. If you need an implementation in a language not
currently supported by liblovense, please
[file an issue on the github tracker](http://github.com/metafetish/liblovense/issues).

All python module code lives in the python/ directory. To install
the library, use either setup.py or pip.

## Protocol Explanation

Lovense toys connect via bluetooth, and then use the Serial Port
Profile (SPP) to communicate with the host. This means that the toys
are exposed as either COM Ports (windows) or tty devices
(posix/bsd/etc). 

Ports for Lovense toys are 9600 baud, 8/N/1.

### Protocol Rules

* Commands and replies are strings, using semicolons to mark their end.
* All commands start with a command identifier word, then possibly
  either specifiers or levels, delimited by colons. e.g. "Vibrate:5;"
  would set vibration to 5.
* Replies are in the context of the command (i.e. sending "Battery;"
  will just return a number, like "85;"), but can still be colon
  delimited lists.

### Command Table

The following is the known command table for all toys. Anything send or received over the serial port is in quotes to denote

| Command         | Description                                                                                                         | Expected Return                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| "DeviceType;"   | Returns toy type (A: Lush, B: Max, C: Nora), Firmware version, and bluetooth MAC address, as a colon delimited list | String, e.g. "C:11:0082059AD3BD;"                                                                    |
| "Battery;"      | Returns battery level of toy                                                                                        | Number, e.g. "85;" meaning 85% battery left                                                          |
| "PowerOff;"     | Powers the device off                                                                                               | "OK;"                                                                                                |
| "Status:1;"     | Shows device status. 2 is "normal"                                                                                  | "2;"                                                                                                 |
| "StartMove:1;"  | Starts accelerometer data stream.                                                                                   | String, that always starts with 'G', followed by 3 16-bit little-endian numbers e.g. "GEF008312ED00" |
| "StopMove:1;"   | Stops accelerometer data stream                                                                                     | "OK;"                                                                                                |
| "RotateChange;" | Changes the direction of rotation for the stimulator on the Nora toy.                                               | "OK;"                                                                                                |
| "Vibrate:x;"    | Sets vibration level for toy. Range seems to be 0-20.                                                               | "OK;"                                                                                                |
| "Rotate:x;"     | Sets rotation speed for Nora toy.                                                                                   | "OK;"                                                                                                |
| "Air:Level:x;"  | Sets absolute air level for Max toy. Range seems to be 0-5;                                                         | "OK;"                                                                                                |
| "Air:In:x;"     | Sets relative inflation level, i.e. if currently inflation level is 3, and "Air:In:1" is sent, will inflate to 4    | "OK;"                                                                                                |
| "Air:Out:x;"    | Sets relative deflation level, i.e. if currently inflation level is 3, and "Air:Out:1" is sent, will inflate to 2   | "OK;"                                                                                                |


## Contributors

* Kyle Machulis <kyle@machul.is>

## Thanks

Thanks to [PenTest Partners](https://www.pentestpartners.com/) for
doing most of the heavy lifting and
[documenting it in their blog](https://www.pentestpartners.com/blog/dicking-around-with-dildos-how-to-drive-a-vibrator-with-realterm/).
This library is mostly just an implementation of the information found
in that post.

## License

tl;dr: BSD License

Copyright (c) 2016, Kyle Machulis
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Kyle Machulis/Nonpolynomial Labs nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY Kyle Machulis ''AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL Kyle Machulis/Nonpolynomial Labs BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE


