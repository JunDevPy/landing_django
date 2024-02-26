from django.db import models

import datetime
from django.db import models


# from django.utils import timezone

# MenuHeader - Верхнее меню
class MenuNavHeader(models.Model):
    item_name = models.CharField('Наименование', max_length=50)
    item_href = models.CharField('Атрибут HREF', max_length=300)
    alt_item = models.CharField('Атрибут ALT', max_length=50)
    disable_item = models.BooleanField('Отключить блок')

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Основное меню (NavBar)'


# SeoHeader - СЕО настройки для сайта
class SeoHeader(models.Model):
    title = models.CharField('Title', max_length=250)
    description_site = models.CharField('Description', max_length=160)
    h1_text_1 = models.CharField('Первый заголовок h1', max_length=100)
    h1_text_2 = models.CharField('Второй заголовок h1', max_length=100)
    h2_text = models.CharField('h2 заголовок', max_length=100)
    text_button = models.CharField('Текст кнопки', max_length=30)
    href_text = models.CharField('Текст ссылки', max_length=30)
    favicon = models.ImageField('FAV иконка', upload_to="static/images")
    logo_main = models.ImageField('Логотип сайта', upload_to="static/images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основные параметры сайта'
        verbose_name_plural = 'SEO настройки'


# HowToDoIt - Секция как получить консультацию
class HowToDoIt(models.Model):
    h4_Block = models.CharField('Заголовок блока', max_length=250)
    h4_step1 = models.CharField('h4 блока ШАГ 1', max_length=50)
    h4_step2 = models.CharField('h4 блока ШАГ 2', max_length=50)
    h4_step3 = models.CharField('h4 блока ШАГ 3', max_length=50)
    step_1_text = models.CharField('Шаг 1 текст', max_length=250)
    step_2_text = models.CharField('Шаг 2 текст', max_length=250)
    step_3_text = models.CharField('Шаг 3 текст', max_length=250)
    disable_blok = models.BooleanField('Отключить блок')

    def __str__(self):
        return self.h4_Block

    class Meta:
        verbose_name = 'Схема работы'
        verbose_name_plural = 'Секция "Схема работы"'


# Service - Секция Наши услуги
class Services(models.Model):
    h3_block_header = models.CharField('Заголовок блока', max_length=250)
    h4_text_block = models.TextField('Текст блока')
    disable_service = models.BooleanField('Отключить блок')

    def __str__(self):
        return self.h3_block_header

    class Meta:
        verbose_name = 'Наши услуги'
        verbose_name_plural = 'Секция "Наши услуги"'


# Expert - Специалисты (модель специалиста)
class Experts(models.Model):
    expert_name = models.CharField('Имя специалиста', max_length=100)
    expert_special = models.CharField('Специализация', max_length=250)
    expert_logo = models.ImageField('Фото спеца', upload_to="static/images/expert")
    expert_text = models.TextField('Текст описания')
    tel = models.CharField('Номер телефона', max_length=11)
    whatsapp = models.CharField('Whatsapp', max_length=11)
    viber = models.CharField('Viber', max_length=11)
    instagram = models.CharField('insta', max_length=250)
    TikTok = models.CharField('TikTok', max_length=250)
    # date_added = models.DateTimeField('Дата добавления')
    disable_expert = models.BooleanField('Отключить специалиста')

    def __str__(self):
        return self.expert_name

    class Meta:
        verbose_name = 'Специалиста'
        verbose_name_plural = 'Специалисты'

    # def was_published_recently(selfs):
    # return self.date_activate_sp >= (timezone.now() - datetime.timedelta(days = 30))


# Video - Секция интересные видео
class ParametersVideosBlock(models.Model):  # Настройки секции (всего блока)
    h4_block_header = models.CharField('Заголовок блока', max_length=250)
    h5_text_block = models.TextField('Текст блока')
    disable_videos = models.BooleanField('Отключить блок')

    def __str__(self):
        return self.h4_block_header

    class Meta:
        verbose_name = 'Интересное видео'
        verbose_name_plural = 'Секция "Интересные Видео"'


class ListVideos(models.Model):  # Добавление и настройки непосредственно роликов
    name_frame = models.CharField('Наименование для админки', max_length=200)
    src_frame = models.CharField('Ссылка на видео', max_length=500)
    width_frame = models.CharField('Ширина фрейма', max_length=300)
    height_frame = models.CharField('Высота фрейма', max_length=50)
    disable_frame = models.BooleanField('Убрать из подборки(отключить)')
    description_frame = models.CharField('Описание к видео', max_length=300)

    def __str__(self):
        return self.name_frame

    class Meta:
        verbose_name = 'Ролик'
        verbose_name_plural = 'Интересные Видео (Ролики)'


# Reviews - Секция ОТЗЫВЫ
class ParametersReviewsBlock(models.Model):
    h3_header = models.CharField('Заголовок блока', max_length=250)
    description_text = models.TextField('Описание блока')
    disable_reviews = models.BooleanField('Отключить отзывы полностью')

    def __str__(self):
        return self.h3_header

    class Meta:
        verbose_name = 'Настроить секцию'
        verbose_name_plural = 'Секция "Отзывы" основные настройки'


class ListReviews(models.Model):  # Модель текстовых отзывов
    name_reviews = models.CharField('Имя', max_length=50)
    expert_logo = models.ImageField('Аватарка', upload_to="{% static 'images/reviews' %}")
    text_reviews = models.CharField('Отзыв', max_length=300)
    event_reviews = models.CharField('Событие', max_length=100)
    disable_reviews = models.BooleanField('Отключить отзыв')

    def __str__(self):
        return f"{self.name_reviews} --- {self.text_reviews} --- {self.event_reviews}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ListVideoReviews(models.Model):  # Модель видео отзывов
    number_slide = models.CharField('Порядковый номер', max_length=1)
    src_slide = models.CharField('Ссылка на видео', max_length=300)
    active_slide = models.BooleanField('Показывать первым')
    disable_slide = models.BooleanField('Убрать из подборки')

    def __str__(self):
        return self.number_slide, self.src_slide, self.active_slide, self.disable_slide

    class Meta:
        verbose_name = 'Видео отзыв'
        verbose_name_plural = 'Видео отзывы'


# Maps - Секция карты
class Maps(models.Model):
    h3_header = models.CharField('Заголовок блока', max_length=30)
    city_name = models.CharField('Город', max_length=30)
    city_href = models.CharField('Сссылка на город', max_length=250)
    adress_name = models.CharField('Адрес', max_length=120)
    adress_text = models.CharField('Сссылка на адрес', max_length=250)
    iframe_code = models.TextField('Код iframe')
    disable_maps = models.BooleanField('Отключить блок')

    def __str__(self):
        return self.h3_header, self.adress_name

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Секция "Карты"'


# Footer - Секция Футер Сайта


class Footer(models.Model):
    email_city = models.EmailField('e-mail', max_length=100)
    adress_city = models.CharField('Адрес', max_length=120)
    disable_maps = models.BooleanField('Отключить блок')

    def __str__(self):
        return f"{self.email_city} --- {self.adress_city}"

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Секция "Footer"'

# Pars - модель модуля парсинга
#
# class pars_master(models.Model):
#     master_name = models.CharField('Имя специалиста', max_length=100)
#     master_special = models.CharField('Навыки', max_length=250)
#     master_avatar = models.ImageField('Фото', upload_to="{% static 'images/team' %}")
#     master_description = models.TextField('Волшебный текст')
#     master_tel = models.CharField('Номер телефона', max_length=11)
#     master_whatsapp = models.CharField('Whatsapp', max_length=11)
#     master_viber = models.CharField('Viber', max_length=11)
#     master_instagram = models.CharField('insta', max_length=250)
#     disable_block = models.BooleanField('Скрыть из выборки')
#
#     def __str__(self):
#         return self.name_sp
#
#     class Meta:
#         verbose_name = 'pars_master'
#         verbose_name_plural = 'pars_master'
