# Tamriel Trade Centre - macOS shell version

This is mac shell version for https://us.tamrieltradecentre.com

It only follows instructions from TTC official page `https://us.tamrieltradecentre.com/pc/Trade/WebClient` , nothing special here.

Need to run up this script before start up Elder Scroll Online

## install

1. create folder `bin` in /Users/yourname/
2. download all files and put them under /Users/yourname/bin
```bash
mkdir -p ~/bin
cd ~/bin
wget https://github.com/kelvinjjwong/tamrieltradecentre-mac-shell/archive/refs/heads/main.zip -O ttc.zip
unzip ttc.zip -d ./
mv tamrieltradecentre-mac-shell-main/* .
rm -rf tamrieltradecentre-mac-shell-main/
rm -f ttc.zip
``` 

3. grant executable permission to these files by using below commands in console:
```bash
cd ~/bin
chmod +x ttc
chmod +x ttc-auto
chmod +x ttc-upload
```

4. run `ttc-auto` each time before running ESO. Or you could create a shortcut icon for it in macOS desktop somewhere

## install for ttc-upload

1. install Google Chrome browser
2. install python, recommend use `brew install python` or you can download pkg file from `https://www.python.org/downloads/`
3. ensure `python` can be located in environment variable `$PATH`, you can verifiy by using `python --version`

- `ttc-upload` is included in `ttc-auto` already.
- this script will launch a Chrome browser window/tab and access TTC web client `https://us.tamrieltradecentre.com/pc/Trade/WebClient` to upload the LUA file automatically if the file has changes. 

#Tested with macOS 14 Sonama, Chrome 126.0 and Python 3.12#

## known issue

### THIRD_PARTY_NOTICES.chromedriver - Exec format error - undetected_chromedriver

Refer to: https://stackoverflow.com/questions/78806812/third-party-notices-chromedriver-exec-format-error-undetected-chromedriver

```bash
source ttc-upload-env/bin/activate

rm -rf ~/.wdm
pip uninstall webdriver-manager
pip install webdriver-manager

pip freeze > ttc-upload-python-env.txt
deactivate
```
