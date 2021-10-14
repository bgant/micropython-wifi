from machine import SoftSPI, Pin
import tinypico as TinyPICO
from dotstar import DotStar
from time import sleep_ms

# Configure SPI for controlling the DotStar
# Internally we are using software SPI for this as the pins being used are not hardware SPI pins
spi = SoftSPI(sck=Pin( TinyPICO.DOTSTAR_CLK ), mosi=Pin( TinyPICO.DOTSTAR_DATA ), miso=Pin( TinyPICO.SPI_MISO) ) 
# Create a DotStar instance
dotstar = DotStar(spi, 1, brightness = 0.5 ) # Just one DotStar, half brightness
# Turn on the power to the DotStar
TinyPICO.set_dotstar_power( True )
    
def off():
    dotstar[0] = (0, 0, 0, 10)

def blink(r,g,b,ms=500,i=3):
    for blinks in range (i):
        dotstar[0] = (r, g, b, 0.5)
        sleep_ms(ms)
        dotstar[0] = (0, 0, 0, 10)
        sleep_ms(ms)

def solid(r,g,b):
    dotstar[0] = (r, g, b, 0.5)

