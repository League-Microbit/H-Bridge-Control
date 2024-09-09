pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)

def on_forever():
    for n in range(1000000):
        i = n % 4
        v = [(1,0),(1,0),(1,0),(1,0)][i]

        pins.digital_write_pin(DigitalPin.P0, v[0])
        pins.digital_write_pin(DigitalPin.P1, v[1])
        basic.pause(1)

#basic.forever(on_forever)
