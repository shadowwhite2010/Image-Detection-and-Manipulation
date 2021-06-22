from PIL import Image

def blend_img(alp):
    with Image.open("C:/Users\DELL\OneDrive\Pictures/sup1.jpg") as im1:
        with Image.open("C:/Users\DELL\OneDrive\Pictures/spi1.jpg") as im2:
            im2 = im2.resize((im1.size[0], im1.size[1]), Image.ANTIALIAS)
            imgr = Image.blend(im1, im2, alp)
    imgr.save("D:/books\google_hash\piloow_prac/blend.png")
# im1 = Image.open("C:\Users\DELL\OneDrive\Pictures/sup1.jpg")
# im2 = 

def lin_gradi():
    img = Image.linear_gradient("R")
    img.save("D:/books\google_hash\piloow_prac/lin_grdR.png")

def red_gradi():
    img = Image.radial_gradient("L")
    img.save("D:/books\google_hash\piloow_prac/red_grd.png")


def cmpst():
    with Image.open("C:/Users\DELL\OneDrive\Pictures/sup1.jpg") as im1:
        with Image.open("C:/Users\DELL\OneDrive\Pictures/test111.jpg") as im2:
            with Image.open("D:/books\google_hash\piloow_prac/red_grd.png") as msk:
                im2 = im2.resize((im1.size[0], im1.size[1]), Image.ANTIALIAS)
                msk = msk.resize((im1.size[0], im1.size[1]), Image.ANTIALIAS)
                imgr = Image.composite(im1, im2, msk)
    imgr.save("D:/books\google_hash\piloow_prac/cmpst.png")

def mandel():
    # with Image.open("D:/books\google_hash\piloow_prac\cmpst.png") as im1:
    im1 = Image.effect_mandelbrot((600, 600), (0, 0, 300, 300), 2)
    im1.save("D:/books\google_hash\piloow_prac/m_b.png")
        
def main():
    # lin_gradi()
    # red_gradi()
    # cmpst()
    mandel()
    # return

if __name__=="__main__":
    main()



