import django
import sys
import os

sys.path.append(os.path.abspath("/home/ilker/repos/borsa/"))
django.setup()

from BasicApp.models import Stock, OHLCV

print(Stock.objects.all())
