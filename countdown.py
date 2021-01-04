import drivers
from time import sleep
from datetime import datetime

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()


def countdown(num_line=1, num_cols=16):
    # Countdown end of the year
    countdown = str(
        datetime(datetime.now().year, 12, 31, 23, 59, 59) - datetime.now()
    ).replace(',', '')
    display.lcd_display_string(countdown[: countdown.find(".")], num_line)


def scrolling_text(text="", start_index=0, num_line=2, num_cols=16):
    end_index = start_index + num_cols
    text_to_print = (
        text[start_index:end_index]
        if end_index < len(text)
        else text[start_index:] + text[: end_index % len(text)]
    )
    display.lcd_display_string(text_to_print, num_line)
    return (start_index + 1) % len(text)


try:
    start_index = 0
    while True:
        countdown()
        start_index = scrolling_text("Inspried by In time movie...", start_index)
        sleep(0.8)

except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+C), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
