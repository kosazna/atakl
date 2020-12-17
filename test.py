from atakl.utilities import *

dst = Path("C:\\Users\\aznavouridis.k\\Desktop\\AKL_Auto\\log.txt")
dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

d1 = Display("GUI")

d1('kostas')
d1('azna')
d1('IS AWESOME')

text = f"AKL v{AKL_VERSION}\n\n" \
       f"{dt}\n" \
       f"{d1.get_content()}"

with open(dst, 'w') as f:
    f.write(text)
