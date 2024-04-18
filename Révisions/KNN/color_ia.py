from knn import knn

data_color = [
    [220, 54, 54, 'rouge'],
    [255, 0, 0, 'rouge'],
    [27, 41, 180, 'bleu'],
    [55, 180, 27, 'vert'],
    [180, 61, 27, 'rouge'],
    [52, 125, 235, 'bleu'],
    [110, 52, 235, 'bleu'],
    [52, 235, 86, 'vert'],
    [52, 235, 223, "bleu"],
    [14, 230, 96, "vert"],
    [200, 0, 0, 'rouge'],
    [0, 200, 0, 'vert'],
    [0, 0, 200, 'bleu'],
    [150, 0, 0, 'rouge'],
    [0, 150, 0, 'vert'],
    [0, 0, 150, 'bleu'],
    [100, 0, 0, 'rouge'],
    [0, 100, 0, 'vert'],
    [0, 0, 100, 'bleu'],
    [50, 0, 0, 'rouge'],
    [0, 50, 0, 'vert'],
    [0, 0, 50, 'bleu'],
    [25, 0, 0, 'rouge'],
    [0, 25, 0, 'vert'],
    [0, 0, 25, 'bleu'],
    [230, 50, 50, 'rouge'],
    [50, 230, 50, 'vert'],
    [50, 50, 230, 'bleu'],
    [200, 100, 100, 'rouge'],
    [100, 200, 100, 'vert'],
    [100, 100, 200, 'bleu'],
    [150, 50, 50, 'rouge'],
    [50, 150, 50, 'vert'],
    [50, 50, 150, 'bleu'],
    [120, 0, 0, 'rouge'],
    [0, 120, 0, 'vert'],
    [0, 0, 120, 'bleu'],
    [180, 0, 0, 'rouge'],
    [0, 180, 0, 'vert'],
    [0, 0, 180, 'bleu'],
    [210, 100, 100, 'rouge'],
    [100, 210, 100, 'vert'],
    [100, 100, 210, 'bleu'],
    [240, 50, 50, 'rouge'],
    [50, 240, 50, 'vert'],
    [50, 50, 240, 'bleu'],
    [255, 100, 100, 'rouge'],
    [100, 255, 100, 'vert'],
    [100, 100, 255, 'bleu'],
    [255, 0, 0, 'rouge'],
    [0, 255, 0, 'vert'],
    [0, 0, 255, 'bleu']
]

test1 = [92, 145, 99]  # * vert
test2 = [76, 158, 203]  # ? bleu
test3 = [221, 143, 110]  # ! rouge


def detection_color(vecteur: list, data: list) -> str:
    # * renvoie une chaine de caractère correspondant à la couleur la plus proche
    # ? vecteur: liste de 3 entiers
    pass
