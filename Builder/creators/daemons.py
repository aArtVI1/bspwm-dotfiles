from shell import run


class Daemons:
    @staticmethod
    def enable_all_daemons():
        Daemons.__enable_network_daemon()
        Daemons.__enable_bluetooth_daemon()
        Daemons.__enable_tor_daemon()
        Daemons.__enable_mpd_daemon()
        Daemons.__enable_lightdm_daemon()
        Daemons.__enable_powerprofiles_daemon()

    @staticmethod
    def __enable_mpd_daemon():
        # mpd - пользовательский демон, поэтому запускается без sudo,
        # иначе systemctl --user не может подключиться к сессионной шине D-Bus
        run("systemctl --user enable mpd", "Автозапуск демона mpd")

    @staticmethod
    def __enable_network_daemon():
        run("sudo systemctl enable NetworkManager", "Автозапуск NetworkManager")

    @staticmethod
    def __enable_bluetooth_daemon():
        run("sudo systemctl enable bluetooth.service", "Автозапуск bluetooth.service")
        run("sudo systemctl start bluetooth.service", "Запуск bluetooth.service")

    @staticmethod
    def __enable_tor_daemon():
        run("sudo systemctl enable tor.service", "Автозапуск tor.service")
        run("sudo systemctl start tor.service", "Запуск tor.service")

    @staticmethod
    def __enable_lightdm_daemon():
        run("sudo systemctl enable lightdm.service", "Автозапуск lightdm.service")

    @staticmethod
    def __enable_powerprofiles_daemon():
        run("sudo systemctl enable power-profiles-daemon.service", "Автозапуск power-profiles-daemon.service")
