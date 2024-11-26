import os
import sys

if __name__ == "__main__":
    exit_code = os.system('python3 -m hikka --no-web --root')
    sys.exit(exit_code)
