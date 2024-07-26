def Strongest_Extension(class_name, extensions):
    
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

#<test>

def test():
    assert Strongest_Extension("MyClass", ["my_extension", "MyExtension", "myExtension", "MYExtension"]) == "MyClass.MYExtension"
    assert Strongest_Extension("MyClass", ["my_extension", "myExtension"]) == "MyClass.myExtension"
    assert Strongest_Extension("MyClass", ["my_extension", "MyExtension", "myExtension"]) == "MyClass.MyExtension"
#</test>
