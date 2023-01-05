
class LateEarlyBar(object):

    def render(self, display, seconds_ahead, start_x, start_y, width):
        height = 10
        bar_width = 2
        space = 1
        center_x = start_x + width // 2
        center_y = start_y + height // 2
        
        # Left bars 
        display.fill_rectangle(start_x, start_y, bar_width, 2)
        for index in range(1,13):
            display.fill_rectangle(start_x + ((bar_width + space) * index), start_y, bar_width, ((height - 6) + (index // 2)))
        
        # Center circle 
        display.fill_ellipse(center_x, center_y, 2, 5)
        
        # Right bars
        right_bar_start_x = start_x + (width - bar_width) + 1
      
        display.fill_rectangle(right_bar_start_x, start_y, bar_width, height)
        for index in range(1,13):
            display.fill_rectangle(right_bar_start_x - ((bar_width + space) * index), start_y, bar_width, height)
       