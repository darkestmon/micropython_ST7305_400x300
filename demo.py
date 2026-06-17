import time, random
from machine import Pin, SPI
from st7305viper import RLCD42

spi = SPI(1, baudrate=500000, polarity=0, phase=0,
          sck=Pin(11), mosi=Pin(12))

cs = Pin(40, Pin.OUT, value=1)
dc = Pin(5, Pin.OUT, value=1)
rst = Pin(41, Pin.OUT, value=1)

lcd = RLCD42(spi, cs, dc, rst)
lcd.fill(0)

for i in range(40):
    lcd.text(str((i+1)%10), i*10, 0, 1)
    lcd.text(str(i+1), 0, i*10, 1)
    
for i in range(20):
    text = str(random.randint(0, 1000000))
    lcd.text(text, 170, 150, 1)
    lcd.refresh()
    time.sleep_ms(30)
    lcd.text(text, 170, 150, 0)
    
time.sleep(3)

lcd.fill(0)

article = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam cursus at turpis vel ullamcorper. Cras fringilla nulla vitae leo auctor suscipit ut non risus. Nullam eleifend hendrerit ultricies. Morbi vel neque sagittis, gravida justo vitae, molestie lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut vehicula, nunc non eleifend vulputate, lorem eros sollicitudin neque, eu mollis magna tellus a libero. Cras et lobortis nulla, quis pulvinar lectus. In finibus tristique ex, quis dapibus arcu tincidunt mattis. Curabitur justo felis, venenatis nec viverra id, posuere sed tortor. Cras mattis nisi a turpis dictum, et iaculis diam volutpat. Integer ultrices posuere dolor, et dapibus orci lobortis vel. Duis convallis, purus at convallis vulputate, mi nibh venenatis arcu, in varius nunc dui sollicitudin eros. Donec in magna facilisis, fringilla ex id, bibendum magna. Praesent pretium felis arcu, vel lobortis nulla condimentum a. Cras posuere nibh faucibus lacus tempor, id vulputate mauris convallis. Quisque accumsan erat quis ipsum tempus semper. Duis dignissim vel dui sed molestie. Phasellus lacus augue, congue sed odio ut, euismod posuere orci. Etiam et leo ac felis luctus tempor eget id massa. In lacinia, tortor sed semper fringilla, lorem mi congue elit, vel sagittis lorem dui ac ipsum. Vestibulum egestas arcu lorem, viverra blandit metus fermentum in. Praesent nibh sem, aliquet quis tincidunt vel, cursus ut diam. Nunc ut pharetra ligula. Sed pharetra nulla enim, sed laoreet mi sagittis vel. Curabitur dictum leo vulputate, ultrices dolor non, rutrum mauris. Morbi pharetra risus feugiat justo suscipit molestie. Praesent eget suscipit sem. Proin sed arcu tellus. Aliquam venenatis ligula vel ultricies eleifend. Curabitur nec nulla nec sem vestibulum venenatis. Vivamus eget libero consectetur, ornare nunc sed, mollis velit. Duis consectetur neque vitae cursus posuere. Suspendisse id velit quis arcu mattis bibendum in ut metus. Sed mauris est, hendrerit at pulvinar nec, euismod sit amet erat. Donec interdum tortor ut egestas ultricies. Ut consequat sapien urna, ac mattis velit porta convallis. Cras ac mauris auctor, ullamcorper odio a, semper libero. Ut lacinia porttitor ultrices. Proin ornare risus in lacus congue efficitur. Sed ullamcorper neque in rhoncus bibendum. In commodo sem in ligula imperdiet, accumsan lacinia neque bibendum. Ut ornare pretium nisl ac congue. Ut fringilla elit convallis est feugiat, vestibulum vestibulum nunc maximus. Donec purus risus, egestas ac tortor quis, iaculis convallis augue. Suspendisse ut arcu quis ex sagittis pretium. Quisque quis sem eu ipsum feugiat ultricies sed nec neque. In vitae sollicitudin orci, a volutpat quam. Fusce euismod interdum nunc et euismod. Sed vitae vehicula arcu. Aenean nisi lorem, fermentum ut tortor et, aliquam placerat odio. Suspendisse potenti. Pellentesque rhoncus eleifend hendrerit. Ut egestas pharetra turpis quis placerat. Ut dignissim pharetra sem, nec consectetur ipsum pretium ac. Ut volutpat consequat ligula, in varius quam imperdiet vel."

for i in range(30):
    lcd.text(article[i*50:(i*50)+50], 0, i*10, 1)
lcd.refresh()
