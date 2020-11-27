# 가능
'''
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()
'''

'''
# 불가능. 이 경우 game 디렉터리의 모듈 혹은 game 디렉터리의 __init__.py 에 정의된 것만 참조 가능하다.
import game 
game.sound.echo.echo_test()

# 불가능. import a.b.c 에서 마지막 항목인 c는 반드시 모듈 또는 패키지여야 함.
import game.sound.echo.echo_test
'''

'''
# __init__.py의 용도
from game.sound import *
echo.echo_test()
# 결과 : name 'echo' is not defined.
# 특정 디렉터리 모듈을 *을 사용하여 import 할땐 다음과 같이 해당 디렉터리의 __init__.py파일에 __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해주어야한다.
# __all__ = ['echo'] . __all__이 의미하는 것 : sound 디렉터리ㅔㅇ서 * 기호를 사용해 import 할 경우 이곳에 정의된 echo모듈만 import된다는 의미
# from game.sound.echo import * 는 __all__과 상관없이 무조건 import 됨!. 이렇게 __all__과 상관없이 무조건 import되는 경우는 from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우이다.
'''

# from ..sound.echo import echo_test == from game.sound.echo import echo_test
# .. -> 부모 디렉터리 , . -> 현재 디렉터리

from game.graphic.render import render_test
render_test()

