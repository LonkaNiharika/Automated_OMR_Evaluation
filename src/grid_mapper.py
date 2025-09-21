def map_grid(sheet_image, num_questions=10, num_options=4):
    h, w = sheet_image.shape[:2]

    # Approximate bubble dimensions and spacing (adjust if necessary)
    bubble_w = int(w * 0.05)
    bubble_h = int(h * 0.03)
    start_x = int(w * 0.1)
    start_y = int(h * 0.2)
    y_gap = int(h * 0.08)
    x_gap = int(w * 0.08)

    grid = {}
    for q in range(num_questions):
        grid[q+1] = []
        for o in range(num_options):
            x = start_x + o * x_gap
            y = start_y + q * y_gap
            grid[q+1].append((x, y, bubble_w, bubble_h))
    return grid
