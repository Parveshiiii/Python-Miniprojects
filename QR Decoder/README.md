# Barcode & QR Code Decoder

## Overview
This Python script decodes barcodes and QR codes from image files using the `pyzbar` and `Pillow` libraries.  
It extracts and prints the embedded data from any supported code format in the image.

## Features
- Supports decoding of both QR codes and various barcode formats.
- Uses `pyzbar` for decoding and `Pillow` for image handling.
- Outputs decoded data in UTF-8 format.

## Requirements
- Python 3.x
- [pyzbar](https://pypi.org/project/pyzbar/)
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies:
```bash
pip install pyzbar Pillow
