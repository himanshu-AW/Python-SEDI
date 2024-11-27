# Namespace is a declarative region that provides a scope to the identifier(variables names, functions name, class names etc). This helps in avoiding naming conflicts spetially  when working with large code basis.
# Scope defines the visibilty with in a program. the LEGB rules determines in which python looks for better.
# Scope of Rule: LEGB rule
# L=>Local:which consisting inside any scope
# E=Encloseing:
# G=Global:modular
# B=Built-in:pre-define names in python
x = 'global'
def outer_fun():
    x="local"
    def inner_fun():
        x='inner'
        print(x)
    inner_fun()
    print(x)
outer_fun()
print(x)

# Why does not have explicit nested namespace like other languages. we can achive a similar effect by module and package.
# example
def func():
    print("execute")

class ABCD:
    def method(self):
        func()
        print("execute")

ob = ABCD()
ob.method()

