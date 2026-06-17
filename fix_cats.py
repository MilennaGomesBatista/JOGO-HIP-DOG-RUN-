from PIL import Image
import os
import glob

def color_dist(c1, c2):
    return max(abs(c1[0]-c2[0]), abs(c1[1]-c2[1]), abs(c1[2]-c2[2]))

def remove_bg_bfs(img_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    pixels = img.load()

    # Coleta a cor dos 4 cantos para ter uma média da cor de fundo real
    corners = [pixels[0,0], pixels[w-1,0], pixels[0,h-1], pixels[w-1,h-1]]
    # Assume que a cor do canto superior esquerdo é a do fundo dominante
    bg_color = pixels[0, 0]

    visited = set()
    queue = []

    # Adiciona todas as bordas na fila inicial
    for x in range(w):
        queue.append((x, 0))
        queue.append((x, h-1))
    for y in range(h):
        queue.append((0, y))
        queue.append((w-1, y))

    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        r, g, b, a = pixels[x, y]
        if a == 0: # Já transparente
            pass
        elif color_dist((r, g, b), bg_color[:3]) < 45: # Tolerância de variação de cor
            pixels[x, y] = (255, 255, 255, 0)
            
            # Adiciona vizinhos
            if x > 0: queue.append((x-1, y))
            if x < w-1: queue.append((x+1, y))
            if y > 0: queue.append((x, y-1))
            if y < h-1: queue.append((x, y+1))

    img.save(img_path, "PNG")
    print(f"Removed background for {img_path}")

def process_dir(dir_path):
    files = glob.glob(os.path.join(dir_path, "*.png"))
    for f in files:
        try:
            remove_bg_bfs(f)
        except Exception as e:
            print("Error on", f, e)

process_dir(r"c:\JOGO-HIP-DOG-RUN-\sprite\gato-andando")
process_dir(r"c:\JOGO-HIP-DOG-RUN-\sprite\gato-assustado")
