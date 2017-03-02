"""pandoc-img-glob is a panflute pandoc filter to recursively search for images
and adjust their paths to be found even in multifile projects."""

__version__ = '0.1.3'


from .pandoc_img_glob import prepare, action, finalize, main  # noqa
