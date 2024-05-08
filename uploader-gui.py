# Author : Keagan Lueck
# Date   : 2023-09-06
# A graphical user interface to make my picture uploading simpler!
import os
import datetime
import tkinter
from datetime import date
from PIL import Image
from PIL.ExifTags import TAGS
from tkinter import PhotoImage




root = tkinter.Tk()
print('Upload photos via GUI')
root.title('Picture Uploader')
root.geometry('285x200')

root.configure(bg="#0b0c10")

appImg = PhotoImage(file='keaganlueck.com(streampi).png')
root.iconphoto(False, appImg)

def tempTxt(e):
   txtInp.delete(0,"end")
def tempTxt1(e):
   txtInp1.delete(0,"end")
   
#lbl = tkinter.Label(root, text="Enter image path:", fg="#999")
txtInp = tkinter.Entry(root, fg="#45a29e", width=45)
txtInp.insert(0, "Image path:")
txtInp.bind("<FocusIn>", tempTxt)
#lbl1 = tkinter.Label(root, text="Caption:", fg="#999")
txtInp1 = tkinter.Entry(root, fg="#45a29e", width=45)
txtInp1.insert(0, "Caption:")
txtInp1.bind("<FocusIn>", tempTxt1)

#lbl.grid(padx=5, pady=5)
#lbl1.grid(padx=5, pady=5)
txtInp.grid(padx=5, pady=5)
txtInp1.grid(padx=5, pady=5)


def post():
        filePath = txtInp.get()
        fileName = os.path.basename(filePath)

        fileDateCreate = os.path.getmtime(filePath)
        creationDate = datetime.datetime.fromtimestamp(fileDateCreate)
        justDate = creationDate.strftime('%Y-%m-%d')  # trimmed down
        print(justDate)

        head, sep, tail = fileName.partition('.')

        image_file = Image.open(filePath)
        image_file.save(head + '-cover.jpg', quality=10)
        exifdata = image_file.getexif()
    # IN PROGRESS
    # exif = {
    # PIL.ExifTags.TAGS[k]: v
    # for k, v in exifdata.items()
    # if k in PIL.ExifTags.TAGS
    # }
    # print(exif)
    # print(image_file.size)
    # print(exifdata.get(271))
    # looping through all the tags present in exifdata
    # for tagid in exifdata:
    # getting the tag name instead of tag id
    # tagname = TAGS.get(tagid, tagid)
    # passing the tagid to get its respective value
    # value = exifdata.get(tagid)
    # printing the final result
    # print(f"{tagname:25}: {value}")

        print(fileName)
        caption = txtInp1.get()
        print(caption)
        title = justDate
        print(title)
        takenOn = "Coolpix S8000"  # input("What was this photo taken on? : ")

        image = Image.open(fileName)
        #print(image.model)

         
        allPhotos = open("all-photos.html", "a")
        allPhotos.write('<html>')
        allPhotos.close()

        gallery = open("pics-gallery.html", "a")
        gallery.write('<html>')
        allPhotos.close()

        library = open("photo-library.html", "a")
        library.write('<html>')
        library.close()

        output = '<a href=''"' + head + '.html"''>'\
            '\n<figure class="gallery-frame">'\
            '\n<img class="gallery-img" src="' + head + '-cover.jpg" alt="symbol image" title="' + title + '">'\
            '\n<figcaption>' + caption + '</figcaption>'\
            '\n</figure></a>'
        libraryOutput = '{imgSrc:' + "'" + fileName + "'" + ','\
                          'caption:' + "'" + caption + "',"\
                          'date:' + "'" + title + "',"\
                          'camera:' + "'" + takenOn + "'},"
                          

        #print(libraryOutput)

        with open("all-photos.html", 'r+') as f:  # r+ does the work of rw
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith('<!--Below here-->'):
                    lines[i] = lines[i].strip() + '\n' + output + '\n'
            f.seek(0)
            for line in lines:
                f.write(line)

        with open("pics-gallery.html", 'r+') as f:  # r+ does the work of rw
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith('<!--Below here-->'):
                    lines[i] = lines[i].strip() + '\n' + output + '\n'
            f.seek(0)
            for line in lines:
                f.write(line)
        with open("photo-library.html", 'r+') as f:  # r+ does the work of rw
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith('//below'):
                    lines[i] = lines[i].strip() + '\n' + libraryOutput + '\n'
            f.seek(0)
            for line in lines:
                f.write(line)

        newHyperFile = head + ".html"
        file = open(newHyperFile, 'x')
        file = open(newHyperFile, 'w')

        htmlTemplate = '<html>\
            \n<head>\
            \n<title>' + caption + '</title>\
            \n<meta name="viewport" content="width=device-width, initial-scale=1.0">\
            \n<link rel="preconnect" href="https://fonts.gstatic.com">\
            \n<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap" rel="stylesheet">\
            \n<script src="https://kit.fontawesome.com/aa9d3f27c6.js" crossorigin="anonymous"></script>\
            \n<link rel="shortcut icon" href="title icon transparent backgroud.png" />\
            \n<link rel="stylesheet" href="photo-template.css" />\
            \n<!-- Global site tag (gtag.js) - Google Analytics -->\
            \n<script async src="https://www.googletagmanager.com/gtag/js?id=G-0TPJ01CVND"></script>\
            \n<script>\
            \nwindow.dataLayer = window.dataLayer || [];\
            \nfunction gtag(){dataLayer.push(arguments);}\
            \ngtag(\'js\', new Date());\
            \ngtag(\'config\', \'G-0TPJ01CVND\');\
            \n</script>\
            \n</head>\
            \n<body class="body">\
            \n<div id="page-container">\
            \n<div id="content-wrap">\
            \n<div class="gradient">\
            \n<nav class="navbar" id="navbar">\
            \n<span class="navbar-toggle" id="js-navbar-toggle" onclick="openNav()">\
            \n<i class="fas fa-bars fa-3x" style="color: white;"></i>\
            \n</span>\
            \n<div id="mySidenav" class="sidenav">\
            \n<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>\
            \n<a href="index.html">home</a>\
            \n<a href="#5074300823" style="color: #fff;"><u>photos:</u></a>\
            \n<a href="pics.html" style="text-indent: 4%;">slideshow</a>\
            \n<a href="pics-gallery.html"  style="text-indent: 4%;" id="current">gallery</a>\
            \n<a href="blog.html">blog</a>\
            \n<a href="changelog.html">changelog</a>\
            \n<a href="contact.html">contact</a>\
            \n</div>\
            \n<a href="index.html" class="logo" id="logo"\
                ><img src="keaganlueck.com(streampi).png" width="55px" height="55px"\
                /></a>\
            \n<ul class="main-nav" id="js-menu">\
            \n<li>\
            \n<a href="index.html" class="nav-links">home</a>\
            \n</li>\
            \n<li>\
            \n<div class="dropdown">\
            \n<button class="dropbtn" id="current">pics</button>\
            \n<div class="dropdown-content">\
            \n<a href="pics-gallery.html">Gallery</a>\
            \n<a href="pics.html">Slideshow</a>\
            \n</div>\
            \n</div>\
            \n</li>\
            \n<li>\
            \n<a href="blog.html" class="nav-links">blog</a>\
            \n</li>\
            \n<li>\
            \n<a href="changelog.html" class="nav-links">changelog</a>\
            \n</li>\
            \n<li>\
            \n<a href="blog.html" class="nav-links">contact</a>\
            \n</li>\
            \n</ul>\
            \n<form onsubmit="pressed(event)" id="form">\
            \n<div class="floating-label-input">\
            \n<input type="text" id="jr" autocapitalize="off" placeholder="Search..."/>\
            \n<label id="button" for="jr"></label>\
            \n<!-- Label MUST be after input! -->\
            \n</form>\
            \n</div>\
            \n</nav>\
            \n<recents id="imgNameHeader"></recents>\
            \n<div class="numberOfPics">\
            \n<p id="counter"></p>\
            \n</div>\
            \n<a href="#" onclick="goBack()" class="more"><< back</a>\
            \n<center>\
            \n<div class="flex-container">\
            \n<div class="flex-item-left">\
            \n<img src="' + fileName + '" class="main-pic" id="imgName" title="hover to zoom">\
            \n<div class="description">\
            \n<p class="des-text">' + caption + '</p>\
            \n</div>\
            \n</div>\
            \n<div class="flex-item-right">\
            \n<center style="background-color:#45a29e;"><boxtitle0><b style="background-color:#45a29e;"><u>info</u></b></boxtitle0></center>\
            \n<boxtext0>This photo was taken on <a href="' + justDate + '.html" >' + justDate + '</a> with <a href="' + takenOn + '.html">' + takenOn + '</a></boxtext0>\
            \n<div class="button-parent"><a href="' + fileName + '" download class="downloadBtn">click to save image</a></div> \
            \n</center>\
            \n</ul>\
            \n</div>\
            \n</div>\
            \n<div class="footer" id="footer">\
            \n<center>\
            \n<p class="footer-text">\
                &copy;\
            \n<script>\
                    document.write(new Date().getFullYear());\
                </script>\
                Keagan Lueck<br /> \
                User Interface - v2 Early Release\
                \n</p>\
            \n</center>\
            \n</div>\
            \n<script src="pics-gallery.js"></script>\
            \n</body>\
            \n</html>'

        file.write(htmlTemplate)
        file.close()
        txtInp.delete(0,"end")
        txtInp1.delete(0,"end")
        txtInp.insert(0, "Success!")
        txtInp1.insert(0, "Success!")



btnPost = tkinter.Button(root, text="POST!",
                         fg="#fff", bg="#45a29e", width=25, height=3, command=post)
btnPost.grid(padx=5, pady=5)

root.mainloop()

