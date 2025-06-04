import module1
import module2
module1.fun1()
module1.fun2()
module2.fun1()
module2.fun2()

from module1 import fun1, fun2
fun1()
fun2()
from module2 import fun1, fun2
fun1()
fun2()