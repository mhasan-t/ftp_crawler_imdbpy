import json
import os
from datetime import datetime
from time import sleep
from django.core.files.images import ImageFile

from ISP_FTP.settings import MEDIA_ROOT
from etc_files import getSeriesDatabyName
from etc_files.get_movies import down_image, stripForFileName
from tv_series.models import TV

from etc_files import read_url_tv, take_name_tv


def createTV(m):
    global tv_obj
    img = m['photo']
    del m['photo']

    try:
        tv_obj = TV.objects.create(**m)
    except:
        time = datetime.now()
        errorFile = open("Error_Data_TV.txt")
        errorFile.write("\n TIME " + str(time) + " *** " + m + "\n")
        errorFile.close()

    timer = 0

    while not os.path.isfile(img) or timer > 10:
        sleep(2)
        timer += 1

    try:
        img_obj = open(img, "rb")
        img_file = ImageFile(img_obj)
        tv_obj.photo.save(m['name'], img_file, save=True)
        img_obj.close()
    except:
        img_obj = open("coverNotFound.png", "rb")
        img_file = ImageFile(img_obj)
        tv_obj.photo.save(m['name'], img_file, save=True)
        img_obj.close()


def get_tv(directory):
    global m_obj
    data_list = read_url_tv(directory)

    for x in data_list[0]:
        name = take_name_tv(x)
        movie_data = getSeriesDatabyName(name)
        if movie_data is False:
            error_data = {
                'error': 'Movie not found in IMDB by name'
            }
            dddd = {
                "dir": x,
                "manual": False,
                "imdb_found": False
            }
            TV.objects.create(**dddd)

        else:
            model_data = {"name": movie_data[0], "dir": x, "year": movie_data[1]}
            da = movie_data[2]
            # s = json.dumps(da)
            s = ", ".join(da)
            model_data["genre"] = s
            model_data["plot"] = movie_data[3]
            model_data["synopsis"] = movie_data[4]
            model_data["cast"] = movie_data[5]
            if movie_data[6] != "":
                downed_image = down_image(movie_data[6], stripForFileName(movie_data[0]))
                model_data["photo"] = MEDIA_ROOT+"/imagesFromIMDBtemp/" +downed_image
            else:
                model_data["photo"] = ""
            model_data["manual"] = False
            model_data["imdb_found"] = True
            model_data["rating"] = movie_data[7]
            model_data["imdbid"] = movie_data[8]

            print("CREATED - ", movie_data[0],"## IMDB ID - ", movie_data[8])
            # print(model_data)
            m = model_data
            createTV(m)


def get_tv_file(video, name):
    movie_data = getSeriesDatabyName(name)

    if movie_data is False:
        error_data = {
            'error': 'Movie not found in IMDB by name'
        }
        dddd = {
            "dir": video,
            "manual": False,
            "imdb_found": False
        }
        TV.objects.create(**dddd)

    else:
        model_data = {"name": movie_data[0], "dir": video, "year": movie_data[1]}
        da = movie_data[2]
        # s = json.dumps(da)
        s = ", ".join(da)
        model_data["genre"] = s
        model_data["plot"] = movie_data[3]
        model_data["synopsis"] = movie_data[4]
        model_data["cast"] = movie_data[5]
        if movie_data[6] != "":
            downed_image = down_image(movie_data[6], stripForFileName(movie_data[0]))
            model_data["photo"] = MEDIA_ROOT + "/imagesFromIMDBtemp/" + downed_image
        else:
            model_data["photo"] = ""
        model_data["manual"] = False
        model_data["imdb_found"] = True
        model_data["rating"] = movie_data[7]
        model_data["imdbid"] = movie_data[8]

        print("CREATED - ", movie_data[0],"## IMDB ID - ", movie_data[8])
        # print(model_data)
        m = model_data
        createTV(m)

