from PIL import Image
import os
import glob

def resize_img(img_path):
    try:
        img = Image.open(img_path)
        # Se a largura for maior que 250, redimensionamos
        if img.size[0] > 250:
            wpercent = (250/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((250, hsize), Image.Resampling.LANCZOS)
            img.save(img_path)
            print("Resized", img_path)
    except Exception as e:
        print("Error", e)

def process_dir(dir_path):
    files = glob.glob(os.path.join(dir_path, "*.png"))
    for f in files:
        resize_img(f)

process_dir(r"c:\JOGO-HIP-DOG-RUN-\sprite\gato-andando")
process_dir(r"c:\JOGO-HIP-DOG-RUN-\sprite\gato-assustado")
