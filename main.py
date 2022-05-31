#!/bin/python3
import argparse, configparser, sys
from src.music2video.megaprint import Printer

p = Printer(logging_level=2, show_timestamp=True)
p.p(1, "A sample error message!")
p.p(2, "A sample warning message!")
p.p(3, "A sample info message!")
exit(0)
