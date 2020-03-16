import ffmpy
import os 

from pytube import YouTube
import requests

from bs4 import BeautifulSoup as bs


class VideoToolKits():
    BASE_URL = "https://www.youtube.com/results?search_query"
    def _search(self,keyWord):
        results = requests.get(self.BASE_URL+keyWord)
        alla = bs(results.text).find_all('a',href=True)
        res = set()
        for a in alla:
            if '/watch?' in a['href']:
                res.add(a['href'])

        ct = 0
        for link in list(res)[:-1]:
            print(ct)
            ct += 1
            try:
                yt = YouTube(link)
                try:
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
                except:
                    print("get content failed")
            except:
                print("get sources failed")
                continue
        print("You have fetched {} videos ".format(str(ct)))

    def _convert(self)
        mp4 = []
        ROOT = os.getcwd()
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                if '.mp4' in name:
                    mp4.append([os.path.join(ROOT, name),name])

        runfile = "run.bat"
        openfile = open(runfile,'a')

        for file,name in mp4:
            # file = file.replace(" ","_")
            outfile = "./sample"
            try:
                output = file.strip("mp4") + 'avi'
                ff = ffmpy.FFmpeg(inputs={file: None},outputs={output: None})
                print("construc successed")
                # 
                print(ff.cmd)
                openfile.writelines(ff.cmd + "\n")
                print("Viedeo {} has been converted successfully".format(name))
            except:
                print("convert failed")

        print("Then run 'run.bat' with admin cmd")
        openfile.close()
