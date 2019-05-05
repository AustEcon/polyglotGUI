Polyglot: Bitcoin protocols made easy
=====================================
Documentation: https://austecon.github.io/polyglot/
Powered by BitSV: https://github.com/AustEcon/bitsv
Powered by Polyglot

Polyglot Mission
----------------

Is to lower barriers to entry for everybody and make metanet FUN!

* Is it just going to be for uploading files?

    - No I have much bigger plans for this.
    - This library is designed to be the easiest way for anybody to interface with all of the various, growing bitcoin metanet protocols.

    Data Carriage:

    - B:// (for multimedia up to 100kb) - https://github.com/unwriter/B
    - BCAT:// (for multimedia up to 310mb uncompressed, 110GB with nested gzip) - https://bcat.bico.media/

    Endpoints:

    - bottle browser (https://bottle.bitdb.network/) (native metanet) browser and urls for mainstream browsers / 3rd party servers:

        - B:// (ref. by txid)
        - C:// (ref. by sha256 hash of content)
        - D:// (ref. by dynamic state - linked to identity system)

    Identity Systems:

    - AIP (https://github.com/BitcoinFiles/AUTHOR_IDENTITY_PROTOCOL)
    - other identity protocols (e.g. Ryan X. Charles of Money Button will be announcing one at CoinGeek)

    Other protocols

    - MAP protocol for linking all kinds of different protocols together (powerful)
    - A.N.N.E. protocol by Mr Scatmann - https://medium.com/@bsmith12251960/a-n-n-e-the-alpha-testing-begins-545f809c6129 (eagerly awaited)


* A PyQt5 GUI will accompany this library to lower barriers to entry even further to non-technical folk https://github.com/AustEcon/polyglotGUI


What needs fixing
-----------------

- This README and many other things...

----------------------------

Examples
--------

- Code examples...


Features (Planned)
------------------

- B:// (for multimedia up to 100kb) - https://github.com/unwriter/B
- BCAT:// (for multimedia up to 310mb uncompressed, 110GB with nested gzip) - https://bcat.bico.media/
- Bottle (https://bottle.bitdb.network/) (native metanet) refs and mainstream urls for:

	- B:// (ref. by txid)
	- C:// (ref. by sha256 hash of content)
	- D:// (ref. by dynamic state - linked to identity system)
- AIP (https://github.com/BitcoinFiles/AUTHOR_IDENTITY_PROTOCOL)
- other ID protocols (e.g. Ryan X. Charles of Money Button has been working hard on this area)
- MAP protocol for linking all kinds of different protocols together (powerful)
- A.N.N.E. protocol by Mr Scatmann - https://medium.com/@bsmith12251960/a-n-n-e-the-alpha-testing-begins-545f809c6129

Installation
------------

Polyglot is distributed on `PyPI` as a universal wheel and is available on Linux/macOS
and Windows and supports Python 3.5+. ``pip`` >= 8.1.2 is required.

.. code-block:: bash

    $ pip install polyglot # pip3 if pip is Python 2 on your system.

Documentation
-------------
Docs are hosted by Github Pages and are automatically built and published by Travis after every successful commit to Polyglot's master branch.


Credits
-------


Donate
--------
- Made by $AustEcon (Handcash handle)
