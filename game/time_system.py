class TimeSystem:
    def __init__(self):
        self.ticks = 0
        self.days = 0
        self.hours = 6  # Start at 6 AM
        self.ticks_per_hour = 60  # Game ticks per hour
        self.total_hours = 0
    
    def update(self):
        self.ticks += 1
        if self.ticks >= self.ticks_per_hour:
            self.ticks = 0
            self.hours += 1
            self.total_hours += 1
            
            if self.hours >= 24:
                self.hours = 0
                self.days += 1
    
    def is_night(self):
        return self.hours >= 20 or self.hours < 6
    
    def advance_day(self):
        self.hours = 6
        self.days += 1
        self.ticks = 0
    
    def get_time_string(self):
        return f"Day {self.days + 1}: {self.hours:02d}:00"
