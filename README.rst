pandoc-img-glob
===============

``pandoc-img-glob`` is a `panflute`_ `pandoc`_ `filter`_.

In multi file and GitHub stored markdown projects, many images are
specified relative to their documents. For example consider the
following `document tree <example>`__:

::

    example
    |-- section1
    |   |-- image1.png
    |   `-- section1.md
    |-- section2
    |   |-- images
    |   |   |-- image3.png
    |   |   `-- image2.png
    |   `-- section2.md
    `-- Makefile

Assuming the ``Makefile`` would compile my full book, it might look like
this:

.. code-block:: Makefile

    book:
    	pandoc -o book.pdf section*/*.md

And in ``section1.md`` there would be a line referencing ``image1.png``,
etc. This is often used because then the GitHub preview looks awesome!
However, pandoc has no way of telling where files came from, so it loses
track of image references, resulting in errors like this:

::

    [pandoc warning] Could not find image `image1.png', skipping...
    [pandoc warning] Could not find image `images/image2.png', skipping...
    [pandoc warning] Could not find image `images/image3.png', skipping...

``pandoc-img-glob`` solves this problem by just searching recursivly
through the path find images matching the given filenames and providing
pandoc (and pandoc only) with the absolute paths. This allows for both:
Beautiful pdfs and GitHub previews using the updated Makefile.

.. code-block:: Makefile

    fixedbook:
    	pandoc --filter pandoc-img-glob -o book.pdf section*/*.md

However, this filter becomes slow if you have very deep and complex
file trees, and if you have multiple images with the same name, it
will just silently use the first it finds.

Installation
------------

Just use pip to install it from `pypi`_

.. code-block:: shell

    pip install pandoc-img-glob


.. _`filter`: https://pandoc.org/scripting.html
.. _`pandoc`: https://pandoc.org/index.html
.. _`panflute`: http://scorreia.com/software/panflute/index.html
.. _`pypi`: https://pypi.python.org/pypi/pandoc-img-glob
