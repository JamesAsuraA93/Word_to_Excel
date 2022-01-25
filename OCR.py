import os


def text_from_image_file(image_name, lang):
    os.system('tesseract {} temp -l {}'.format(image_name, lang))
    try:
        read = open('temp' + '.txt', 'r', encoding='utf-8').read()
    except:
        read = open('temp' + '.txt', 'r', encoding='utf-8').read()
    os.remove('temp.txt')
    return read


if __name__ == '__main__':
    print(text_from_image_file("pics/testpic.png", "tha"))
