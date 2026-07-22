person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
import importlib

try:
    mymodule = importlib.import_module("mymodule")
except ImportError:
    class mymodule:
        @staticmethod
        def greeting(name):
            print(f"Hello {name}")

mymodule.greeting("Jonathan")