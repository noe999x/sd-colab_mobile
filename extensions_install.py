
#module
import base64
import os
import urllib.request
from time import sleep
from IPython.display import clear_output

### -warna-font
H = '\033[1;32m'
D = '\033[0m'
B = '\033[1;34m'
M = '\033[1;31m'

###-decode_base64
sysai = base64.b64decode(("d2VidWk=").encode('ascii')).decode('ascii')
print(f"{H}Menginstall extensions!...{D}")

###-import extensions
!curl -Lo AUTOMATIC1111-mobile.rar https://huggingface.co/21sysai/AUTOMATIC1111-mobile/resolve/main/AUTOMATIC1111-mobile.zip
!unzip /content/AUTOMATIC1111-mobile.rar
!git clone https://github.com/Bing-su/sd-$sysai-tunnels /content/AUTOMATIC1111-mobile/extensions/sd-tunnels
!git clone https://github.com/noe999x/sd-$sysai-controlnet /content/AUTOMATIC1111-mobile/extensions/sd-controlnet
!git clone https://github.com/fkunn1326/openpose-editor /content/AUTOMATIC1111-mobile/extensions/openpose-editor
!git clone https://github.com/hnmr293/posex /content/AUTOMATIC1111-mobile/extensions/posex
!git clone https://github.com/DominikDoom/a1111-sd-$sysai-tagcomplete /content/AUTOMATIC1111-mobile/extensions/sd-tagcomplete
!git clone https://github.com/hako-mikan/sd-$sysai-supermerger /content/AUTOMATIC1111-mobile/extensions/sd-supermerger
!git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 /content/AUTOMATIC1111-mobile/extensions/ultimate-upscale-for-automatic1111
!git clone https://github.com/KohakuBlueleaf/a1111-sd-$sysai-locon /content/AUTOMATIC1111-mobile/extensions/sd-locon
!mkdir /content/AUTOMATIC1111-mobile/models/ESRGAN
!curl -Lo /content/AUTOMATIC1111-mobile/extensions/microsoftexcel-images-browser.zip https://github.com/noe999x/sd-$sysai/raw/main/microsoftexcel-images-browser.zip
!curl -Lo /content/AUTOMATIC1111-mobile/embeddings/embeddings.zip https://github.com/noe999x/sd-$sysai/raw/main/embeddings.zip
!curl -Lo /content/AUTOMATIC1111-mobile/models/ESRGAN/upscalers.zip https://huggingface.co/21sysai/upscalers/resolve/main/upscalers.zip
%cd /content/AUTOMATIC1111-mobile/extensions
!unzip /content/AUTOMATIC1111-mobile/extensions/microsoftexcel-images-browser.zip
%cd /content/AUTOMATIC1111-mobile/embeddings
!unzip /content/AUTOMATIC1111-mobile/embeddings/embeddings.zip
%cd /content/AUTOMATIC1111-mobile/models/ESRGAN
!unzip /content/AUTOMATIC1111-mobile/models/ESRGAN/upscalers.zip
clear_output()

###-deleted zip
print(f"{M}Menghapus file sampah...{D}")
!rm /content/AUTOMATIC1111-mobile.rar
!rm /content/AUTOMATIC1111-mobile/models/ESRGAN/upscalers.zip
!rm /content/AUTOMATIC1111-mobile/embeddings/embeddings.zip
!rm /content/AUTOMATIC1111-mobile/extensions/microsoftexcel-images-browser.zip
sleep(2)
%cd /content
clear_output()

print(f"{H}Menginstall model default...{D}")
###-default model
!curl -Lo /content/AUTOMATIC1111-mobile/models/Stable-diffusion/majicMIX_realisticv5.safetensors https://civitai.com/api/download/models/82446
clear_output()
print(f"{H}Instalasi selesai...", f"\n{B}Lanjutkan proses berikutnya.{D}")
