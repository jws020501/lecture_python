import math #math라는 모듈을 가져온다는 뜻입니다 math는 수학과 관련된 함수와 상수가 있는 모듈입니다
import math as m #math 모듈을 m이라는 이름으로 가져온다는 뜻입니다. 
from math import pi #math 모듈에서 pi라는 상수만 가져온다는 뜻입니다.
from math import pi as p #math 모듈에서 pi라는 상수를 가져와서 p라는 이름으로 바꾼다는 뜻입니다.
print(math.pi)
print(m.pi)
print(pi)
print(p)

#전부 파이를 출력하는 코드입니다.
#3.141592653589793
#다 같은 값을 가지지만 방식이 다릅니다.
