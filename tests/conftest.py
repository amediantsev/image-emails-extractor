import os
import sys
from pathlib import Path

import pytest

package_root = os.path.join(Path(__file__).parent.parent.resolve())
sys.path.append(package_root)


@pytest.fixture
def get_test_abspath():
    def f(fixture_path):
        return os.path.join(f"{package_root}/{fixture_path}")

    return f
