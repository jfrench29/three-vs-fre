from pathlib import Path
from PIL import Image, ImageOps
import pillow_heif, qrcode, qrcode.image.svg, json
pillow_heif.register_heif_opener()
root=Path(__file__).resolve().parents[1]
photos={'hero':'20241006_204803407_iOS.jpg','early-days':'20180518_010458848_iOS.jpg','cup':'20190412_173413033_iOS.heic','clubhouse':'20190412_230436612_iOS.heic','koozie':'20231011_175005146_iOS.heic','celebration':'20231014_222114217_iOS.heic'}
for name,source in photos.items():
 im=ImageOps.exif_transpose(Image.open(root/source)).convert('RGB'); im.thumbnail((1800,1800)); im.save(root/'site/assets'/f'{name}.webp','WEBP',quality=85)
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=24,border=4)
qr.add_data('https://fredesucksatgolf.com');qr.make(fit=True)
qr.make_image(fill_color='black',back_color='white').save(root/'print/frede-qr.png')
qr.make_image(image_factory=qrcode.image.svg.SvgPathFillImage).save(root/'print/frede-qr.svg')
print('Images optimized; QR matrix',len(qr.get_matrix()),'modules including quiet zone')

for photo in json.loads((root/"scripts/archive-photos.json").read_text()):
 im=ImageOps.exif_transpose(Image.open(root/photo["source"])).convert("RGB")
 im.thumbnail((1600,1600))
 im.save(root/"site/assets"/photo["output"], "WEBP", quality=83)
