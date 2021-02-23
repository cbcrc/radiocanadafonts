# Production Notes
Images in this directory are rendered with and include [Python](https://www.python.org/) source files made using the [DrawBot](https://www.drawbot.com/) library.

After buiding with DrawBot, animated GIFs are post-processed with [gifsicle](https://www.lcdf.org/gifsicle/).
``` bash
gifsicle -i width-axis-example-italic.gif -O3 --colors 16 -o anim-temp.gif
```
