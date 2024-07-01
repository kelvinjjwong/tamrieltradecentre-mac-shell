# Tamriel Trade Centre - macOS shell version

This is mac shell version for https://us.tamrieltradecentre.com

Need to run up this script before start up Elder Scroll Online

## install

1. create folder `bin` in /Users/yourname/
2. download all files and put them under /Users/yourname/bin
3. grant executable permission to these files by using below commands in console:
```bash
cd ~/bin
chmod +x ttc
chmod +x ttc-auto
chmod +x ttc-upload
```
4. run `ttc-auto` each time before running ESO. Or you could create a shortcut icon for it in macOS desktop somewhere

## install for ttc-upload

1. install python, recommend use `brew install python` or you can download pkg file from `https://www.python.org/downloads/`
2. ensure `python` can be located in environment variable `$PATH`, you can verifiy by using `python --version`
3. `ttc-upload` is included in `ttc-auto` already.

#Tested with macOS 14 Sonama and Python 3.12#
