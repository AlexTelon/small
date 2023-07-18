import sys
import os
import importlib.util
import inspect

def get_tests(module):
    return [f for name, f in inspect.getmembers(module, inspect.isfunction) if name.startswith('test_')]

def module(file):
    if not file.endswith('.py'):
        return None
    module_name = os.path.basename(file).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

if __name__ == '__main__':
    modules = list(map(module, set(sys.argv[1:])))
    tests = (test for module in modules for test in get_tests(module))
    for test in tests:
        test()