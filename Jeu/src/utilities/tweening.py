from p5 import millis
progressions = []

class AddLinearInterpolation:
    def __init__(self,A:float,B:float,alpha:float) -> None:
        self.A = A
        self.B = B
        self.alpha = alpha
        self.progression = A
        self.finished = False
        self.state = "inactive"
        interpolations.append(self)
    def update(self):
        if self.state == "playing":
            A = self.progression
            if round(A,3) != self.B:
                B = self.B
                self.progression = (A + (B - A) * self.alpha)
            elif self.state != "completed":
                self.state = "completed"
        return self.progression
    def play(self):
        self.state = "playing"
    def reset(self):
        self.state = "inactive"
        self.finished = False
        self.progression = self.A
    def destroy(self):
        interpolations.pop(interpolations.index(self))
        del self

interpolations = []

class AddProgression:
    def __init__(self,delta:float,func) -> None:
        """Delta est le temps en milisecondes à dépasser pour avant que la fonction ne s'éxécute."""
        self.tick = millis()
        self.goal = millis() + delta * 1000
        self.time_spent = 0
        self.func = func
        progressions.append(self)
    def update_progression(self):
        self.tick = millis()
        self.time_spent = self.goal - self.tick
        if self.tick >= self.goal:
            self.func()
            progressions.pop(progressions.index(self))
            del self

def draw_update():
    for i in interpolations:
        i.update()