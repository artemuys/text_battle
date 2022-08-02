
import combat_logic
import input_mapper
from threading import Thread

if __name__ == '__main__':
    Thread(target = combat_logic.mainloop).start()
    Thread(target=input_mapper.input_logic).start()


