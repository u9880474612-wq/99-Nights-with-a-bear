class TimeSystem:
    def __init__(self):
        self.time = 0  # 0-2400 (represents 0:00 to 24:00)
        self.days = 0
        self.speed = 10  # Minutes pass per frame
        
    def update(self):
        self.time += self.speed
        if self.time >= 2400:
            self.time = 0
            self.days += 1
    
    def is_night(self):
        # Night is from 20:00 (2000) to 6:00 (600)
        return self.time >= 2000 or self.time < 600
    
    def is_morning(self):
        return 600 <= self.time < 1200
    
    def is_afternoon(self):
        return 1200 <= self.time < 1800
    
    def is_evening(self):
        return 1800 <= self.time < 2000
    
    def get_time_string(self):
        hours = self.time // 100
        minutes = self.time % 100
        return f"{hours:02d}:{minutes:02d}"
    
    def skip_night(self):
        # Skip to morning (6:00)
        self.time = 600
        self.days += 1
    
    def get_day_phase(self):
        if self.is_night():
            return "Night (Dangerous!)"
        elif self.is_morning():
            return "Morning (Safe)"
        elif self.is_afternoon():
            return "Afternoon (Safe)"
        else:
            return "Evening (Getting Dark)"
