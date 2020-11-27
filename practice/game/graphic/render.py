# 만약 디렉터리의 reder.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶으면?
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()