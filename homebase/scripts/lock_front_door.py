#!/usr/bin/env python
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
# Run imports this way so importing works
from homebase.appliances import lock

if __name__ == '__main__':
    my_front_door = lock.get_first_lock()
