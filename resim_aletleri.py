from PIL import ImageTk, Image

def kareyegenislet(pil_img, background_color):
    width, height = pil_img.size

    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

def genislikal(pil_resim, yukseklik):
    genislik = yukseklik  / pil_resim.height * pil_resim.width
    print(genislik)
    print("gen")
    genislikgen = int(genislik)
    return genislikgen

def hexecevir(hexkod):
    h = hexkod.lstrip('#')
    print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))