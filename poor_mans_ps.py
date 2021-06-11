"""
Poor Man's Photoshop
CSE110 W07/8 Milestone
Author: Nathan Johnston
Purpose: Interpolate a background image onto a foreground image
"""
from PIL import Image
# print('The image library has loaded correctly')


def Photoshop(foreground, background, new_name='new_images/new_image'):
    """ make a new image, combining two other images, back- and foreground """
    # make new img
    image_new = Image.new("RGB", foreground.size)

    # get old pixels
    pixels_background = background.load()
    pixels_foreground = foreground.load()
    pixels_new = image_new.load()

    # get image size
    widthf, heightf = foreground.size

    # for each x pixel and y pixel, inefficient: O(n**2)
    for pixel_x in range(widthf):
        for pixel_y in range(heightf):
            # print(f'{pixel_x}, {pixel_y}')

            # get pixel rbg values
            r, g, b = pixels_foreground[pixel_x, pixel_y]

            # if foreground is green enough, replace it
            if r <= 115 and g >= 140 and b <= 115:
                # replace with background_img
                pixels_new[pixel_x,
                           pixel_y] = pixels_background[pixel_x, pixel_y]
            else:
                pixels_new[pixel_x, pixel_y] = (r, g, b)

    # save and quit
    image_new.save(f'{new_name}.jpg')

    # display the image
    image_new.show()


def prompt_background():
    """ Prompt user for one of seven image choices to be used for the background, returns image and image name  """
    inputting = True
    print('\nChoose a background image:\nbeach\ndesert\nearth\nfield\nforest\nsnowscape\nsunset')
    while inputting:
        img_name = input(': ')
        try:
            img = Image.open(f'images/{img_name}.jpg')
            inputting = False
        except:
            print('It seems you may have misspelled your choice. Try again.')
    return img, img_name


def prompt_foreground():
    """ Prompt user for one of seven image choices to be used for the foreground, returns image and image name """
    inputting = True
    # for choosing images in an /images/ folder off the current directory (like how the author uses this)
    print('\nChoose a foreground image:\nboat\ncactus\ncat\ncat_small\nharvester\nhiker\npenguin\nspaceshuttle')
    while inputting:
        img_name = input(': ')
        try:
            img = Image.open(f'images/{img_name}.jpg')
            inputting = False
        except:
            print('It seems you may have misspelled your choice. Try again.')

    return img, img_name


def prompt_file(location):
    """ prompt user for filepath of foreground/backgound image """
    # free range version:
    inputting = True
    while inputting:
        img_file = input(f'\nWhat is the file path of the {location} image?  ')
        try:
            img = Image.open(f'{img_file}')
            inputting = False
        except:
            print('It seems you may have misspelled your choice. Try again.')

    return img


def prompt_save_location():
    """ asks where to save the new image """
    save_file = input('Where should the new_image be saved? ')
    file_name = input('What should it be called? ')
    return save_file, file_name


def main():
    """ Get the user's foreground and background image choices, then put them together in Not-Photoshop """
    print('Welcome to PyShop! "The poor man\'s Photoshop!"')

    # determine where the images to manipulate are stored for the user
    print('\nAre the pictures to edit in the .\\images folder or somewhere else?\n1. .\\images\n2. Somewhere else')
    img_location = input(': ')

    if img_location == '1':
        # debug choices
        foreground_img, forename = prompt_foreground()
        background_img, backname = prompt_background()
        Photoshop(foreground_img, background_img,
                  f'new_images/{forename}_{backname}')
    else:
        # production choices
        foreground_img = prompt_file('foreground')
        background_img = prompt_file('background')
        save, filepath = prompt_save_location()
        Photoshop(foreground_img, background_img, f'{save}/{filepath}')


if __name__ == '__main__':
    main()
