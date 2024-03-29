import json
import os
import urllib.request
from datetime import datetime
from time import sleep
from django.core.files.images import ImageFile

from ISP_FTP.settings import BASE_DIR, MEDIA_ROOT

from etc_files import read_url, take_name, getMovieDatabyName, getMovieDatabyID
from movies.models import Movies


def down_image(url, title):
    full_path = MEDIA_ROOT+"/imagesFromIMDBtemp"+"/"+title+".jpg"
    urllib.request.urlretrieve(url, full_path)
    return title+".jpg"


def stripForFileName(st):
    result = ""
    for c in st:
        if c != ":" and c != "*" and c != "?" and c != "<" and c != ">" and c != "|" and c != "/" and c != "\\":
            result += c

    return result

def createMovie(m):
    global m_obj
    img = m['photo']
    del m['photo']

    try:
        m_obj = Movies.objects.create(**m)
    except:
        time = datetime.now()
        errorFile = open("Error_Data.txt")
        errorFile.write("\n TIME " + str(time) + " *** " + m + "\n")
        errorFile.close()

    timer = 0

    while not os.path.isfile(img) or timer > 10:
        sleep(2)
        timer += 1

    try:
        img_obj = open(img, "rb")
        img_file = ImageFile(img_obj)
        m_obj.photo.save(m['name'], img_file, save=True)
        img_obj.close()
    except:
        img_obj = open("coverNotFound.png", "rb")
        img_file = ImageFile(img_obj)
        m_obj.photo.save(m['name'], img_file, save=True)
        img_obj.close()




def get_movie(directory):
    global m_obj
    data_list = read_url(directory)

    for x in data_list[0]:
        name = take_name(x)
        movie_data = getMovieDatabyName(name)
        if movie_data is False:
            error_data = {
                'error': 'Movie not found in IMDB by name'
            }
            dddd = {
                "video": x,
                "manual": False,
                "imdb_found": False
            }
            Movies.objects.create(**dddd)

        else:
            model_data = {"name": movie_data[0], "video": x, "year": movie_data[1]}
            da = movie_data[2]
            s = ", ".join(da)
            # s = json.dumps(da)
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
            createMovie(m)


def get_movie_file(video, name):
    movie_data = getMovieDatabyName(name)

    if movie_data is False:
        error_data = {
            'error': 'Movie not found in IMDB by name'
        }
        dddd = {
            "video": video,
            "manual": False,
            "imdb_found": False
        }
        Movies.objects.create(**dddd)

    else:
        model_data = {"name": movie_data[0], "video": video, "year": movie_data[1]}
        da = movie_data[2]
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
        createMovie(m)


# d = get_movie("http://moviepoka.com/data/disk2/Hollywood_2009/Adventures%20With%20Purpose%20New%20Zealand%20%282009%29/")[0]


