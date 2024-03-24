import os
import urllib.request

def install_packages():
    os.system("sudo pacman -Sy --noconfirm qtile git neofetch feh")

def download_wallpaper():
    # URL для скачивания обоев
    wallpaper_url = "https://download1527.mediafire.com/kqk8m6867grgy8eXkBFKmtoaGuSw9WMluTsU15fujBLRyRAmppFDL4pxnnC_FjwGldJmOTzF-NN86CSVADX25VT5bK9sRsiw0h06B8qF5aeXwhRKnd7-u8rF3bytL8SEDrFg_IbeyzMmtuHw3MNHVxRt8wGHHc6Qwvq-iT_--hYg/nopykyoghdbbwjc/wallpaper.jpg"
    # Путь для сохранения обоев
    wallpaper_path = os.path.expanduser("~/wallpaper.jpg")
    urllib.request.urlretrieve(wallpaper_url, wallpaper_path)

def enable_autostart():
    autostart_file = os.path.expanduser("~/.config/qtile/config.py")
    autostart_commands = [
        "os.system('feh --bg-scale ~/wallpaper.jpg &')",
        "os.system('polybar &')"
    ]
    with open(autostart_file, "a") as f:
        f.write("\n")
        for command in autostart_commands:
            f.write(command + "\n")

def main():
    install_packages()
    download_wallpaper()
    enable_autostart()

if __name__ == "__main__":
    main()
