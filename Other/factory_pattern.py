import sys
from abc import ABC, abstractmethod
from enum import Enum


class Platforms(str, Enum):
    WINDOWS = 'win32'
    LINUX = 'linux'
    MACOS = 'darwin'


class Button(ABC):
    @abstractmethod
    def click(self) -> str:
        pass

    @abstractmethod
    def paint(self) -> str:
        pass

class WindowsButton(Button):
    def click(self) -> str:
        return 'You clicked Windows Button'
        
    def paint(self) -> str:
        return 'You painted Windows Button'

class LinuxButton(Button):
    def click(self) -> str:
        return 'You clicked Linux Button'
        
    def paint(self) -> str:
        return 'You painted Linux Button'

class MacOSButton(Button):
    def click(self) -> str:
        return 'You clicked MacOS Button'
        
    def paint(self) -> str:
        return 'You painted MacOS Button'

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()


def main() -> None:
    if sys.platform == Platforms.WINDOWS:
        print('Your OS is Windows')
        factory = WindowsFactory()
        button = WindowsButton
    elif sys.platform == Platforms.LINUX:
        print('Your OS is Linnux')
        factory = LinuxFactory()
        button = LinuxButton
    elif sys.platform == Platforms.MACOS:
        print('Your OS is MacOS')
        factory = MacOSFactory()
        button = MacOSButton
    else:
        raise NotImplementedError(f"Not implemented for your platform: {sys.platform}")

    button_ = button()
    print(button_.click())
    print(button_.paint())



if __name__ == "__main__":
    main()