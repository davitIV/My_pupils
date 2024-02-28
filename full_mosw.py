from mosw_dalageba import analyze_mosw_data
from mosw_sheyvana import mosw_sheyvana

k = int(input('press 1 to see mosw_analyze table'))
if k == 1:
    analyze_mosw_data()
k = int(input('press 2 to add mosw in table'))
if k == 2:
    mosw_sheyvana()
