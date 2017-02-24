"""pandoc-img-glob is a panflute pandoc filter to recursively search for images
and adjust their paths to be found even in multifile projects."""

import glob

import panflute as pf

__version__ = '0.1.0'


def prepare(doc):
    pass


def action(elem, doc):
    if isinstance(elem, pf.Image):
        hits = glob.glob('**/{}'.format(elem.url), recursive=True)
        if len(hits) < 1:
            return None
        elem.url = hits[0]


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc)


if __name__ == '__main__':
    main()
