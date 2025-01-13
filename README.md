# NTC - Inkscape Extension

NTC is an Inkscape extension that generates color information (HEX, RGB, CMYK, HSL, HSV) for a selected object. 

## Installation
1. Download the files `ntc.py` and `ntc.inx`.
2. Copy both files to the `extensions` directory in Inkscape's configuration folder:
   - **Linux**: `~/.config/inkscape/extensions/`
   - **Windows**: `%APPDATA%\inkscape\extensions\`
3. Restart Inkscape.


## Usage
1. Select object (supported types: path, rect, or ellipse).
2. Access the menu **Extensions > Generate > NTC**.
3. Check the color formats you wish to generate.
4. Click **Apply**.

## Notes
- This extension supports only `path`, `rect`, and `ellipse` objects. Other types will display an error message.
- Ensure the object’s color is not a gradient or pattern for accurate results.


## Disclaimer 
We don't guarantee anything about this tool/extension, so please use it at your own risk. We can't give 24/7 support if you have a problem when using Magibox. 

If you feel that this tool has helped you to create, feel free to donate a cup of coffee on the [Support Dev](https://saweria.co/raniaamina) :")
