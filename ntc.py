import inkex
import argparse
from inkex.elements import TextElement
import colorsys

class NTCColorExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--hex_checkbox", type=inkex.Boolean, default=True, help="Tampilkan HEX")
        pars.add_argument("--rgb_checkbox", type=inkex.Boolean, default=True, help="Tampilkan RGB")
        pars.add_argument("--cmyk_checkbox", type=inkex.Boolean, default=False, help="Tampilkan CMYK")
        pars.add_argument("--hsl_checkbox", type=inkex.Boolean, default=False, help="Tampilkan HSL")
        pars.add_argument("--hsv_checkbox", type=inkex.Boolean, default=False, help="Tampilkan HSV")

    def effect(self):
        hex_enabled = self.options.hex_checkbox
        rgb_enabled = self.options.rgb_checkbox
        cmyk_enabled = self.options.cmyk_checkbox
        hsl_enabled = self.options.hsl_checkbox
        hsv_enabled = self.options.hsv_checkbox

        if not self.svg.selected:
            inkex.errormsg("Tidak ada objek yang dipilih. Silakan pilih objek terlebih dahulu.")
            return

        for element in self.svg.selection:
            try:
                fill_color = element.style.get('fill')
                if not fill_color or fill_color in ['none', 'transparent']:
                    fill_color = '#000000'  # Fallback to black
                hex_code = fill_color.upper()

                r = int(hex_code[1:3], 16)
                g = int(hex_code[3:5], 16)
                b = int(hex_code[5:7], 16)
                rgb_code = f"R: {r} G: {g} B: {b}"

                c = 1 - r / 255
                m = 1 - g / 255
                y = 1 - b / 255
                k = min(c, m, y)
                if k < 1:
                    c = (c - k) / (1 - k)
                    m = (m - k) / (1 - k)
                    y = (y - k) / (1 - k)
                cmyk_code = f"C: {c*100:.2f}% M: {m*100:.2f}% Y: {y*100:.2f}% K: {k*100:.2f}%"

                r_norm = r / 255.0
                g_norm = g / 255.0
                b_norm = b / 255.0
                h, s, l = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)
                hsl_code = f"H: {h*360:.2f}° S: {s*100:.2f}% L: {l*100:.2f}%"

                hsv_code = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
                hsv_code = f"H: {hsv_code[0]*360:.2f}° S: {hsv_code[1]*100:.2f}% V: {hsv_code[2]*100:.2f}%"

                bbox = element.bounding_box()

                x_position = bbox.right + 10  
                y_position = bbox.top + 5  

                group = inkex.Group()

                if hex_enabled:
                    text_hex = TextElement()
                    text_hex.text = f"{hex_code}"
                    text_hex.style = {'font-size': '4.75px;', 'fill': '#000000'}
                    text_hex.set('x', str(x_position))
                    text_hex.set('y', str(y_position))
                    group.append(text_hex)

                if rgb_enabled:
                    text_rgb = TextElement()
                    text_rgb.text = f"{rgb_code}"
                    text_rgb.style = {'font-size': '4.75px;', 'fill': '#000000'}
                    text_rgb.set('x', str(x_position))
                    text_rgb.set('y', str(y_position + 10))  # text gap
                    group.append(text_rgb)

                if cmyk_enabled:
                    text_cmyk = TextElement()
                    text_cmyk.text = f"{cmyk_code}"
                    text_cmyk.style = {'font-size': '4.75px;', 'fill': '#000000'}
                    text_cmyk.set('x', str(x_position))
                    text_cmyk.set('y', str(y_position + 20)) 
                    group.append(text_cmyk)

                if hsl_enabled:
                    text_hsl = TextElement()
                    text_hsl.text = f"{hsl_code}"
                    text_hsl.style = {'font-size': '4.75px;', 'fill': '#000000'}
                    text_hsl.set('x', str(x_position))
                    text_hsl.set('y', str(y_position + 30))
                    group.append(text_hsl)

                if hsv_enabled:
                    text_hsv = TextElement()
                    text_hsv.text = f"{hsv_code}"
                    text_hsv.style = {'font-size': '4.75px;', 'fill': '#000000'}
                    text_hsv.set('x', str(x_position))
                    text_hsv.set('y', str(y_position + 40)) 
                    group.append(text_hsv)

                self.svg.append(group)

            except Exception as e:
                inkex.errormsg(f"Kesalahan saat menambahkan teks: {e}")

if __name__ == '__main__':
    NTCColorExtension().run()
