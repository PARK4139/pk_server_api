import sqlite3
import time

conn = sqlite3.connect("state.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS state (id INTEGER PRIMARY KEY, previous_state TEXT, last_change_time REAL)")
conn.commit()

def get_previous_state():
    cursor.execute("SELECT previous_state, last_change_time FROM state WHERE id = 1")
    row = cursor.fetchone()
    return row if row else (None, time.time())

def save_state(new_state):
    cursor.execute("INSERT OR REPLACE INTO state (id, previous_state, last_change_time) VALUES (1, ?, ?)",
                   (str(new_state), time.time()))
    conn.commit()

previous_state, last_change_time = get_previous_state()
milliseconds_for_speed_control = 100

while True:
    current_state = (state_running, state_loading, state_loaded, state_playing)
    if current_state != previous_state:
        previous_state = current_state
        last_change_time = time.time()
        milliseconds_for_speed_control = 100
        save_state(current_state)
    else:
        if time.time() - last_change_time >= 2:
            milliseconds_for_speed_control = min(milliseconds_for_speed_control + 10, 500)

    time.sleep(milliseconds_for_speed_control / 1000.0)
