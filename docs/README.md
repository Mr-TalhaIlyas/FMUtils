## Sphinx
```
$ sphinx-quickstart
```
Then enter the project name, author name, version, language etc. and Enter.

Then generate `html` so that you get the file structure 
```
$ make html
// from removing everytin in build
$ make clean html
```
your generate `index.html` will be in `docs/html` dir.

Now we will use the `sphinx-apidoc` command to generate the documantation of our `src` model and put the generated files in `docs` folder.
```
$ sphinx-apidoc -o docs src/

```


Ref:
[YouTube](https://www.youtube.com/watch?v=5s3JvVqwESA&list=LL&index=1&ab_channel=SoumilShah)
