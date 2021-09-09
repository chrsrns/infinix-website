# Generated by Django 3.2.5 on 2021-08-14 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('web_api', '0001_squashed_0002_revision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameblogpage',
            name='album_image',
        ),
        migrations.RemoveField(
            model_name='gameblogpage',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gameblogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='gameblogpagecarouselimages',
            name='carousel_image',
        ),
        migrations.RemoveField(
            model_name='gameblogpagecarouselimages',
            name='page',
        ),
        migrations.RemoveField(
            model_name='gameindexpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gameindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='gamesblogauthororderable',
            name='author',
        ),
        migrations.RemoveField(
            model_name='gamesblogauthororderable',
            name='page',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_cta_link_page',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='AlbumItems',
        ),
        migrations.DeleteModel(
            name='GameBlogPage',
        ),
        migrations.DeleteModel(
            name='GameBlogPageCarouselImages',
        ),
        migrations.DeleteModel(
            name='GameIndexPage',
        ),
        migrations.DeleteModel(
            name='GamesBlogAuthorOrderable',
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]