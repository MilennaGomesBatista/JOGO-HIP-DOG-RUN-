from PIL import Image
import sys

def remove_checkerboard(path):
    try:
        img = Image.open(path).convert("RGBA")
    except Exception as e:
        print("Error opening image:", e)
        return
        
    pixels = img.load()
    w, h = img.size
    
    visited = set()
    # Start flood fill from all border pixels to be aggressive against the checkerboard
    queue = []
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
        # Calculate how "gray" it is (low difference between channels) and how bright it is
        max_diff = max(abs(r-g), abs(g-b), abs(r-b))
        
        if a == 0 or (max_diff < 40 and r > 100):
            pixels[x, y] = (0, 0, 0, 0)
            if x > 0: queue.append((x-1, y))
            if x < w-1: queue.append((x+1, y))
            if y > 0: queue.append((x, y-1))
            if y < h-1: queue.append((x, y+1))
                
    img.save(path, "PNG")
    print("Background removed successfully")

remove_checkerboard(r"c:\JOGO-HIP-DOG-RUN-\sprite\tronco.png")
