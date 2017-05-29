def pytest_addoption(parser):
    parser.addoption("--grid_ip", action="store",
            help="grid hub IP address")
