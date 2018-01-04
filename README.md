# pytest-json
## Some python web-frameworks real tests

Tests are made with **ab** utility with **100** level of concurrency, **10k** requests.

**ab -c 100 -n 10000 http://127.0.0.1:8080/**

Hardware are used: Thinkpad X240, i5-4300U, 8Gb of RAM

There is some results:

* **aiohttp + json** - longest - **53ms**, average - **43ms**, **2315 rps**
* **aiohttp + json + uvloop** - longest - **39ms**, average - **28ms**, **3485 rps**
* **aiohttp + ujson** - longest - **53ms**, average - **42ms**, **2338 rps**
* **aiohttp + ujson + uvloop** - longest - **39ms**, average - **25ms**, **3860 rps**

## Conclusions
* There is no difference between **json** and **ujson** on small dicts
* But usage of **ujson** with **uvloop** can give you extra perfomance (around 400rps for this case)
* Usage of **uvloop** can give you about x2 boost for free