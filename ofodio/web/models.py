from django.db import models

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

    name = models.CharField(max_length = 150)
    pub_date = models.DateField('date published')
    director = models.CharField(max_length = 150)
    country = models.CharField(max_length = 50)
    language = models.CharField(max_length = 50)
    length = models.CharField(max_length = 8)
    genre = models.CharField(max_length=20, choices=GENRE, default='بدون دسته بندی')
    rank = models.FloatField(default=0)
    summary = models.CharField(max_length=200)
    path = 'videos/'
    cover = models.ImageField(blank=False, null=True, upload_to=path)
    file= models.FileField(upload_to=path, null=True, verbose_name="")


    def __str__ (self):
        return str(self.name) + ' - ' + str(self.pub_date.year)

    
