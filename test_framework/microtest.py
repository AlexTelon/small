import sys
import os
import importlib.util

if __name__ == '__main__':
    files = (file for file in set(sys.argv) if file.endswith('.py'))

    for file in files:
        # Import the module
        module_name = os.path.basename(file).replace('.py', '')
        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Run the tests
        for name in dir(module):
            if not callable(getattr(module, name)):
                continue
            if name.startswith('test_'):

                print('Running', name)
                getattr(module, name)()
