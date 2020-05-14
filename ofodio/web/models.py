from django.db import models
import hashlib

DEF_PATH = 'files/'

GENRE = (
    ('none', 'بدون دسته بندی'),
    ('action', 'اکشن'),
    ('historical', 'تاریخی'),
    ('horror', 'ترسناک'),
    ('crime', 'جنایی'),
    ('war', 'جنگی'),
    ('family', 'خانوادگی'),
    ('news', 'خبری'),
    ('drama', 'درام'),
    ('mysterious', 'راز آلود'),
    ('biography', 'زندگی نامه'),
    ('science_fiction', 'علمی-تخیلی'),
    ('fantasy', 'فانتزی'),
    ('comedy', 'کمدی'),
    ('short', 'کوتاه'),
    ('adventure', 'ماجراجویی'),
    ('documentary', 'مستند'),
    ('musical', 'موزیکال'),
    ('thriller', 'هیجان انگیز'),
    ('sport', 'ورزشی'),
    ('western', 'وسترن'),
)

class Movie(models.Model):
    def movie_name_to_database(name, hashstr):
        name = str(name)
        hashstr = str(hashstr)
        import sqlite3
        con = sqlite3.connect('movie_names.sqlite3')
        c = con.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS movies(name TEXT, hash TEXT)')
        c.execute('INSERT INTO movies VALUES("%s", "%s")'%(name, hashstr))
        con.commit()
        con.close()

    
    _hash = hashlib.sha256

    name = models.CharField(max_length = 150)
    pub_date = models.DateField('date published')
    director = models.CharField(max_length = 150)
    country = models.CharField(max_length = 50)
    language = models.CharField(max_length = 50)
    length = models.CharField(max_length = 8)
    genre = models.CharField(max_length=20, choices=GENRE, default='بدون دسته بندی')
    rank = models.FloatField(default=0)
    summary = models.CharField(max_length=200)
    hashstr = _hash('{}-{}'.format(str(name), str(pub_date)).encode('utf-8')).hexdigest()
    movie_path = DEF_PATH + hashstr
    cover = models.ImageField(blank=False, null=True, upload_to=movie_path)

    movie_name_to_database(name, hashstr)
    # print("#############" + str(name) +"###########")


    def __str__ (self):
        return str(self.name) + ' - ' + str(self.pub_date.year)

    
