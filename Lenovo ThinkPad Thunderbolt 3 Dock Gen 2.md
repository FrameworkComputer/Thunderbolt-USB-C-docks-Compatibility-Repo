# Thunderbolt/USB-C docks  Compatibility with Linux Framework Laptop 13

## General Information

- **Thunderbolt/USB-C docks Model**: 40AN0135US
- **Manufacturer**: Lenovo
- **Number of Ports**: 
  - 2x Display Port (up to 3840 x 2160 / 60Hz)
  - 2x HDMI, 1x RJ45 1GB Ethernet
  - 1x 3.5mm audio jack (headphone + microphone)
  - 4x USB 3.1 Gen 2 (10 Gbps)
  - 1x USB-C Thunderbolt 3
  - 135W or 65W power supply
  - 230W or 170W power supply
- **USB Version**: USB 3.1 Gen2
- **Date Tested**: 11-AUG-2021
- **Tester**: @Foxtrek_64, @gms, @nathaniel_graham

## System Information

- **Linux Distribution**: Fedora 39
- **Kernel Version**: [Enter kernel version (e.g., 6.8.0-35-generic)]
- **Desktop Environment**: GNOME, Plasma

## Compatibility Details

- **Plug-and-Play Functionality**: Yes
- **Power Delivery**: Yes
- **Data Transfer Speed**: 1Gbps ethernet
- **Supported Devices**: 
  - [List supported devices connected via the hub, e.g., mouse, keyboard, external hard drive, etc.]

## Identified Issues

- **Issue 1**: Indicator LEDs and power button do not integrate with Framework Laptop on Fedora 37.
  - **Description**: The dock does not give power on status of the laptop, nor does the power button work, when running Fedora 37. Please verify whether this issue persists on later versions of Fedora.
  - **Workaround/Fix**: Unknown.
  - **Logs/Errors**: 
    ```plaintext
    [Include relevant log entries or error messages]
    ```

- **Issue 2**: DisplayPort functionality is unstable on Fedora 39.
  - **Description**: Powering on the laptop with the dock plugged in causes the monitors to not receive signal, even  though the displays are recognized in xrandr and wayland.
  - **Workaround/Fix**: Unknown.
  - **Logs/Errors**: 
    ```plaintext
    [Include relevant log entries or error messages]
    ```


## Troubleshooting Tips

1. **Check dmesg Logs**:
    ```bash
    dmesg | grep -i usb
    ```

2. **Verify USB Devices**:
    ```bash
    lsusb
    ```

3. **Inspect Power Settings**:
    ```bash
    upower -i /org/freedesktop/UPower/devices/usb_device_[DeviceID]
    ```

4. **Kernel Module Management**:
    ```bash
    sudo modprobe [module_name]
    ```

## Additional Notes

- **Firmware Updates**: [Any information on firmware updates for the USB hub]
- **Links and Resources**: 
  - [Official product page](#)
  - [Linux community discussions](#)
  - [Driver downloads](#)

## Conclusion

- **Overall Compatibility**: [Summarize the overall compatibility of the USB hub with Linux]
- **Final Remarks**: [Any additional comments or recommendations]

---

*This document is a part of the Thunderbolt/USB-C docks Compatibility with Linux Framework Laptop 13 Database. Contributions are welcome!*
