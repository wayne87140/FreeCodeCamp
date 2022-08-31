import random
from copy import copy

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)
        self.init_content = copy(self.contents)
               
    def draw(self, amount_to_draw):
        if len(self.contents) == 0:
            self.contents = self.init_content
        if amount_to_draw >= len(self.contents):
            removed_balls = self.contents.copy()
            self.contents = []
            return removed_balls
        # print(self.contents)
        removed_balls = random.sample(self.contents, amount_to_draw)
        for ball in removed_balls:
            self.contents.remove(ball)      
        return removed_balls
    
    def reset(self):
        self.contents = copy(self.init_content)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_get_expected_balls = 0
    
    for _ in range(num_experiments):
        copy_expected_balls = copy(expected_balls)
        hat.reset()
        # print(hat.contents)
        removed_balls = hat.draw(num_balls_drawn)
        # print(removed_balls)
        for ball in removed_balls:
            if ((curr_ball_amount := copy_expected_balls.get(ball))
                and (curr_ball_amount >0)):
                copy_expected_balls[ball] -=1
        # print(copy_expected_balls.values(), '\n\n')
        if not any(copy_expected_balls.values()):
            times_get_expected_balls += 1

    return (times_get_expected_balls / num_experiments)

    
if __name__ == '__main__':


    random.seed(95)
    hat = Hat(blue=4, red=2, green=6)
    # print(hat.draw(4))
    # hat.reset()
    # print(hat.contents)
    # print(hat.draw(4))
    # print(hat.draw(6))
    # print(hat.draw(6))
    probability = experiment(
        hat=hat,
        expected_balls={"blue": 2,
                        "red": 1},
        num_balls_drawn=4,
        num_experiments=8)
    print("Probability:", probability)