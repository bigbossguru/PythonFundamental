from typing import Callable

def general(volume: float, message: str) -> Callable[..., None]:

    def too_loud() -> str:
        msg: str = message.upper() + '!!!'
        return msg
    
    def too_silent() -> str:
        msg: str = message.lower() + '...'
        return msg
    
    if volume > 0.5:
        return too_loud
    else:
        return too_silent

if __name__ == "__main__":
    VOLUME: float = 0.3

    print(general(VOLUME, 'play music')())