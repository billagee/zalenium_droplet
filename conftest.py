def pytest_addoption(parser):
    parser.addoption("--hub_host", action="store",
            help="grid hub IP or hostname")
