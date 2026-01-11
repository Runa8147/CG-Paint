import tkinter as tk

# --- SIMPLE BRESENHAM LINE ALGORITHM ---
def draw_line_algorithm(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        # Drawing a 1x1 rectangle to represent a single pixel
        canvas.create_rectangle(x1, y1, x1+1, y1+1, outline="black")
        
        if x1 == x2 and y1 == y2:
            break
            
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# --- COMMAND PROCESSING ---
def handle_command(event):
    cmd = entry.get().strip().lower()
    
    # Expected format: line(x1,y1,x2,y2)
    try:
        if cmd.startswith("line(") and cmd.endswith(")"):
            # Extract numbers between brackets
            content = cmd[5:-1] 
            coords = [int(c.strip()) for c in content.split(',')]
            
            if len(coords) == 4:
                draw_line_algorithm(coords[0], coords[1], coords[2], coords[3])
                print(f"Drawing line from ({coords[0]},{coords[1]}) to ({coords[2]},{coords[3]})")
            else:
                print("Error: Provide exactly 4 coordinates.")
        else:
            print("Unknown command. Use: line(x1,y1,x2,y2)")
            
    except Exception as e:
        print(f"Invalid input: {e}")
    
    entry.delete(0, tk.END)

# --- GUI SETUP ---
root = tk.Tk()
root.title("Simple Line Algorithm")

# Canvas area
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Instruction Label
label = tk.Label(root, text="Enter command: line(x1,y1,x2,y2)")
label.pack()

# Command Input Area
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.bind("<Return>", handle_command) # Press Enter to execute
entry.focus_set()

root.mainloop()