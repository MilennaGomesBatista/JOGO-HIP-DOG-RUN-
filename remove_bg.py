from PIL import Image
import os
import glob

def remove_background(img_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    # Assumindo fundo branco ou quase branco
    for item in datas:
        if item[0] > 230 and item[1] > 230 and item[2] > 230:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(img_path, "PNG")

def process_dir(dir_path):
    files = glob.glob(os.path.join(dir_path, "*.png"))
    for f in files:
        try:
            remove_background(f)
            print("Processed", f)
        except Exception as e:
            print("Error on", f, e)

process_dir(r"c:\JOGO-HIP-DOG-RUN-\sprite\gato-andando")
process_dir(r"c:\JOGO-HIP-DOG-RUN-\sprite\gato-assustado")
