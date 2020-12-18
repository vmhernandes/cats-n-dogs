import os
import shutil


def split_imgs(original):
    list_all = os.listdir(original)
    list_cats = []
    list_dogs = []

    for arquivo in list_all:
        if arquivo.startswith('cat'):
            list_cats.append(original+arquivo)
        if arquivo.startswith('dog'):
            list_dogs.append(original+arquivo)
    
    return list_cats, list_dogs

original = 'train/'

list_cats, list_dogs = split_imgs(original)

list_test = list_cats[:100] + list_dogs[:100]

list_treino_cat = list_cats[100:10100]
list_treino_dog = list_dogs[100:10100]

list_validacao_cat = list_cats[10100:]
list_validacao_dog = list_cats[10100:]


f_treino = 'dataset/treino/'
f_teste = 'dataset/teste/'
f_validacao = 'dataset/validacao/'
f_cat = 'cat/'
f_dog = 'dog/'

for image in list_test:
    shutil.copy2(image, f_teste)


for image in list_treino_cat:
    shutil.copy2(image, f_treino+f_cat)

for image in list_validacao_cat:
    shutil.copy2(image, f_validacao+f_cat)


for image in list_treino_dog:
    shutil.copy2(image, f_treino+f_dog)

for image in list_validacao_dog:
    shutil.copy2(image, f_validacao+f_dog)