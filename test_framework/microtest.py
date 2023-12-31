import sys
import os
import importlib.util
import inspect

def get_tests(module):
    return [f for name, f in inspect.getmembers(module, inspect.isfunction) if name.startswith('test_')]

def module(file):
    match os.path.basename(file).split('.py'):
        case (module_name, ''):
            spec = importlib.util.spec_from_file_location(module_name, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module

def evaluate_test(test):
    try:
        test()
        return True
    except AssertionError as e:
        print(f"'{test.__name__}' failed: {e}")
        return False

if __name__ == '__main__':
    modules = map(module, set(sys.argv[1:]))
    tests = [test for module in modules for test in get_tests(module)]
    passed = sum(map(evaluate_test, tests))
    print(f'{passed}/{len(tests)} tests passing')