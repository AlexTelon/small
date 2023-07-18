

# A minimal test framework

Want to mimic the basics of pytest. Finding functions that has test_ in their name, run them and mark tests as failed if they throw and AssertionError

Goal is to make something really short and sweet. 20-50 lines if possible. Make it simple to use with other linux tools so that detailed file discovery for instance could be done by bash expansions rather than the python code if necessary to keep it short.

**Ideas for features:**

* **Test Discovery**: Automatically discover and execute tests based on configurable rules.
* **Test Fixtures**: Define reusable test setup and teardown code.
* **Parameterized Testing**: Write tests with different input values for better coverage.
* **Test Execution Control**: Select, exclude, or order tests based on markers or expressions.
  * Might leave this out and let the user do this using external tools.
* **Test Coverage**: Measure code coverage during test runs.
* **Plugins and Extensions**: We will see.