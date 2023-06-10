# class AudioFile:
#     def __init__(a, filename):
#         if not filename.endswith(a.ext):
#             raise Exception("invalid file format")
#         a.filename = filename
# class MP3File(AudioFile):
#     ext = "mp3"
#     def play(a):
#         print("playing {} as mp3".format(a.filename))
# class WavFile(AudioFile):
#     ext = "wav"
#     def play (a):
#         print("playing {} as wav".format(a))
# class oggFile(AudioFile):
#     ext = "ogg"
#     def play (a):
#         print("playing {} as ogg".format(a))
# class FlacFile:
#     def __init__(a,filename):
#         if not filename.endswith(".flac"):
#             raise Exception("invalid file format")
#         a. filename = filename
#     def play (a):
#             print("playing {} as flac".format(a))






class  Person:
    def __init__(a,name,age):
        a.name = name
        a.age = age
    def description(a):
        print("hello my name is " + a.name,a.age'and my olid')
pk = Person("ali" ,99)
pk.description ()


class Car(object):
    def __init__(a,modile,color,campany,speed_limit):
        a.modile = modile
        a.color = color
        a.campany = campany
        a.speed_limit = speed_limit
    def Details (a):
        print("Car Details",a.modile,a.color,a.campany,a.speed_limit)
hirofe = Car("AZ3","rad","Hirofe",200)
hirofe.Details()