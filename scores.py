# scores
from datetime import datetime
# Scoringsystem
class Scores:
    def __init__(self, spanscore=0, widerscore=0, stromscore=0,
                 spanwrong=0, widerwrong=0, stromwrong=0):
        self.spanscore = spanscore
        self.widerscore = widerscore
        self.stromscore = stromscore
        self.spanwrong = spanwrong
        self.widerwrong = widerwrong
        self.stromwrong = stromwrong
        self.timestamps = {
            'span richtig': None,
            'wider richtig': None,
            'strom richtig': None,
            'span falsch': None,
            'wider falsch': None,
            'strom falsch': None,
            }
        self.load_scores() 
    def add_span(self, points=1):
        self.spanscore += points
        self.timestamps['span richtig'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_scores()
        return self.spanscore  
    def add_wider(self, points=1):
        self.widerscore += points
        self.timestamps['wider richtig'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_scores()
        return self.widerscore   
    def add_strom(self, points=1):
        self.stromscore += points
        self.timestamps['strom richtig'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_scores()
        return self.stromscore 
    def add_spanwrong(self, points=1):
        self.spanwrong += points
        self.timestamps['span falsch'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_scores()
        return self.spanwrong  
    def add_widerwrong(self, points=1):
        self.widerwrong += points
        self.timestamps['wider falsch'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_scores()
        return self.widerwrong    
    def add_stromwrong(self, points=1):
        self.stromwrong += points
        self.timestamps['strom falsch'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_scores()
        return self.stromwrong   
    def save_scores(self):
        """Save all scores with their names and timestamps to a single file"""
        try:
            with open("scores.txt", "w") as file:
                scores_data = [
                    f"Span richtig: {self.spanscore} | Last Updated: {self.timestamps['span richtig']}",
                    f"Wider richtig: {self.widerscore} | Last Updated: {self.timestamps['wider richtig']}",
                    f"Strom richtig: {self.stromscore} | Last Updated: {self.timestamps['strom richtig']}",
                    f"Span falsch: {self.spanwrong} | Last Updated: {self.timestamps['span falsch']}",
                    f"Wider falsch: {self.widerwrong} | Last Updated: {self.timestamps['wider falsch']}",
                    f"Strom falsch: {self.stromwrong} | Last Updated: {self.timestamps['strom falsch']}"
                ]
                file.write("\n".join(scores_data))
            print("Scores and timestamps saved successfully!")
        except Exception as e:
            print(f"Error saving scores: {e}")   
    def load_scores(self):
        """Load scores and timestamps from file if it exists"""
        try:
            with open("scores.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "Span richtig:" in line:
                        parts = line.split("|")
                        self.spanscore = int(parts[0].split(":")[1].strip())
                        self.timestamps['span richtig'] = parts[1].split(":")[1].strip()
                    elif "Wider richtig:" in line:
                        parts = line.split("|")
                        self.widerscore = int(parts[0].split(":")[1].strip())
                        self.timestamps['wider richtig'] = parts[1].split(":")[1].strip()
                    elif "Strom richtig:" in line:
                        parts = line.split("|")
                        self.stromscore = int(parts[0].split(":")[1].strip())
                        self.timestamps['strom richtig'] = parts[1].split(":")[1].strip()
                    elif "Span falsch:" in line:
                        parts = line.split("|")
                        self.spanwrong = int(parts[0].split(":")[1].strip())
                        self.timestamps['span falsch'] = parts[1].split(":")[1].strip()
                    elif "Wider falsch:" in line:
                        parts = line.split("|")
                        self.widerwrong = int(parts[0].split(":")[1].strip())
                        self.timestamps['wider falsch'] = parts[1].split(":")[1].strip()
                    elif "Strom falsch:" in line:
                        parts = line.split("|")
                        self.stromwrong = int(parts[0].split(":")[1].strip())
                        self.timestamps['strom falsch'] = parts[1].split(":")[1].strip()
                print("Scores and timestamps loaded successfully!")
        except FileNotFoundError:
            print("No saved scores found. Starting with default values.")
        except Exception as e:
            print(f"Error loading scores: {e}")

        