from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('KDE Plasma', ProfileType.DesktopEnv, description='')

	@property
	@override
	def packages(self) -> list[str]:
		return [
			"plasma-meta",
			"konsole",
			"kate",
			"dolphin",
			"ark",
			"plasma-workspace",
      		"bluedevil",
      		"breeze-gtk",
      		"dolphin-plugins",
      		"ffmpegthumbs",
      		"fwupd",
      		"gwenview",
      		"kde-cli-tools",
      		"kde-gtk-config",
      		"kdeconnect",
      		"kdegraphics-thumbnailers",
      		"kdenetwork-filesharing",
      		"kdeplasma-addons",
      		"kgamma",
      		"kimageformats",
      		"kinfocenter",
      		"kio-admin",
      		"kio-extras",
      		"kio-fuse",
      		"kscreen",
      		"kwallet-pam",
      		"kwayland-integration",
      		"libappindicator-gtk3",
      		"maliit-keyboard",
      		"okular",
      		"plasma-browser-integration",
      		"plasma-desktop",
      		"plasma-disks",
      		"plasma-firewall",
      		"plasma-nm",
      		"plasma-pa",
      		"plasma-systemmonitor",
      		"powerdevil",
      		"print-manager",
      		"sddm-kcm",
      		"spectacle",
      		"xdg-desktop-portal-kde",
      		"xsettingsd",
      		"xwaylandvideobridge",
      		"partitionmanager",
			"isoimagewriter"
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Sddm
