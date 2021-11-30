# Production Notes
Images in this directory include [Python](https://www.python.org/) source files and are rendered using the [DrawBot](https://www.drawbot.com/) library.

```bash
pip install git+https://github.com/typemytype/drawbot
python3 nameplate.py
```

After rendering with DrawBot, animated GIFs can be post-processed with [gifsicle](https://www.lcdf.org/gifsicle/) to reduce file size.
``` bash
gifsicle -i width-axis-example-italic.gif -O3 --colors 16 -o animation-compressed.gif
```
