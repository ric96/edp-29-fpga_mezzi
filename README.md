Based on: https://github.com/oprema/Waveshare-E-Ink

# waveshare-e-ink
This is rewrite of Waveshares 2.9 and 1.54 inch e-ink paper display driver
for the Raspberry Pi in python (version 2 and 3). The original source code can be found at:
https://www.waveshare.com/wiki/2.9inch_e-Paper_Module

### Important: [Follow this guide to activate the SPI interface](https://www.96boards.org/documentation/mezzanine/shiratech-fpga/guides/simple-spi-hats.md.html)

### Wiring Plan: E-Ink-Display <-> Raspi Header
```
Display   Raspi   
3.3V      3.3V - Pin 17   
GND       GND  - Pin 20   
DIN       MOSI - Pin 19   
CLK       SCLK - Pin 23   
CS        CE0  - Pin 24   
DC        GPIO 25 - Pin 22   
RST       GPIO 17 - Pin 11   
BUSY      GPIO 24 - Pin 18   
```

### Software to install:
```
sudo apt-get install python3-pip libtiff5-dev libopenjp2-7-dev fonts-freefont-ttf libfreetype6-dev
sudo pip3 install spidev qrcode Image python-dotenv
sudo pip3 pip3 install --force-reinstall --ignore-installed --no-binary :all: Pillow
```
#### Examples:
python3 main.py -> Same as the original from waveshare   
python3 qr-disp.py -> Shows QR-codes   
python3 icons.py -> Font awesome icons and icon names   

<img src="/images/image-2.jpeg" width="650">
<img src="/images/image-3.jpeg" width="650">
