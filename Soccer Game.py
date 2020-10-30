"""
Dr. Paul W. Bible
A simple program illustrating pygame
"""
import pygame, sys
from pygame.locals import *
import random


# #def opponent_goal_count():
#     left_random = random.randint(1, 3)
#     middle_random = random.randint(4, 7)
#     # right_random = random.randint(8, 10)
#     # goalie_random = random.randint(-10, 10)
#     # random_keys = [left_random, middle_random, right_random, goalie_random]
#     opponent_goal_counts = 0
#     right_randoms = float(random.randint(8, 10))
#     goalie_randoms = float(random.randint(-10, 10))
#     random_keys = float[1:10]
#     for right_random in range(int(random_keys)):
#         if right_randoms == right_randoms:
#             opponent_goal_counts += 1
#             print(opponent_goal_counts)
#         else:
#             opponent_goal_counts += 1
#             print(opponent_goal_counts)
#             #return opponent_goal_counts
#     opponent_goal_count()


def main():
    # start up pygame
    pygame.init()
    clock = pygame.time.Clock()
    """ color variables"""

    # https://htmlcolorcodes.com
    BG_COLOR = (43, 184, 88)
    GOALIE_COLOR = (251, 175, 53)
    GOAL_COLOR = (255, 255, 255)
    BALL_COLOR = (255, 255, 255)
    PLAYER_COLOR = (0, 43, 93)
    win_width = 500
    win_height = 500

    window = pygame.display.set_mode((win_width, win_height))
    window.fill(BG_COLOR)
    """Goal Variables"""

    goal_square = pygame.Surface((170, 50))
    goal_square.fill(GOAL_COLOR)
    goal_x = 160
    goal_y = 50

    # create some variables to move a circle

    # goal_square.fill(GOAL_COLOR)
    """ Ball Variables """
    ball_win_width = 200
    ball_win_height = 200
    ball_x = 225
    ball_y = 225
    ball_square = pygame.Surface((10, 10))
    ball_square.fill(BALL_COLOR)
    ball_window = pygame.display.set_mode((ball_win_width, ball_win_height))

    # player_sqaure
    "Player Variables"
    player_win_width = 500
    player_win_height = 500
    player_x = 225
    player_y = 245
    player_square = pygame.Surface((10, 10))
    player_square.fill(PLAYER_COLOR)
    player_window = pygame.display.set_mode((player_win_width, player_win_height))
    pressed = []

    "Goalie Variables"
    goalie_win_width = 500
    goalie_win_height = 500
    goalie_x = 245
    goalie_y = 110
    goalie_square = pygame.Surface((10, 10))
    goalie_square.fill(GOAL_COLOR)
    goalie_window = pygame.display.set_mode((goalie_win_width, goalie_win_height))
    # opponent_dict = []
    opponent_goal_count = 0
    player_goal_count = 0
    #################################

    """ User customization  """

    # Jersey_color = input('choose_jersey_color: Yellow, blue, green')
    # Team_name = input('write in team name')
    # Add_add_players = input('write name of player')
    # Add_player_number = input('write player number')
    # Field color = input('choose filed color')

    """ main game loop """

    while True:

        left_random = random.randint(1, 3)
        middle_random = random.randint(4, 7)
        right_random = random.randint(8, 10)
        goalie_random = random.randint(1, 10)
        # random_keys = [left_random, middle_random, right_random, goalie_random]
        # process events for the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed.append(event.key)
            elif event.type == pygame.KEYUP:
                pressed.remove(event.key)
            elif event.type == QUIT:

                # close the window if x is clicked
                pygame.quit()
                sys.exit()

        #################################
        """ Pre-draw processing """
        # random_keys = (-10, 10)
        # for random_keys in range(len(random_keys)):
        if pygame.K_RIGHT in pressed:
            ball_x += 19
            ball_y -= 26
            for goalie_random in range(1, 10, +1):
                if goalie_random == range(8,10):
                    print('right_random_number:', right_random)
                    print('goalie_random_number:', goalie_random)
                    print('miss')
                    opponent_goal_count += 1
                    print('opponent_goal_count:', opponent_goal_count)
                    continue
                else:
                    print('goal')
                    print('right_random_number:', right_random)
                    print('goalie_random_number:', goalie_random)
                    player_goal_count += 1
                    print('player_goal_count:', player_goal_count)
                    continue

            # goalie_x += goalie_random
            # # print('right_random_number:', right_random)
            # # print('goalie_random_number:', goalie_random)
            # if goalie_random == range(right_random):
            #     print('block')
            #     print('right_random_number:', right_random)
            #     print('goalie_random_number:', goalie_random)
            # else:
            #     print('goal')
            #     print('right_random_number:', right_random)
            #     print('goalie_random_number:', goalie_random)

        if pygame.K_LEFT in pressed:
            ball_x -= 18
            ball_y -= 30
            goalie_x += goalie_random + - 10
            print('left_random:', left_random)
            if goalie_random == range(left_random):
                print('block')
                print('right_random_number:', left_random)
                print('goalie_random_number:', goalie_random)
            else:
                print('goal')
                print('right_random_number:', right_random)
                print('goalie_random_number:', goalie_random)

        if pygame.K_UP in pressed:
            ball_y -= 20
            goalie_x += goalie_random + - 10
            print('middle_random:', middle_random)
            if goalie_random == range(middle_random):
                print('block')
                print('right_random_number:', right_random)
                print('goalie_random_number:', goalie_random)
            else:
                print('goal')
                print('right_random_number:', right_random)
                print('goalie_random_number:', goalie_random)

        if pygame.K_DOWN in pressed:
            ball_y -= 20
            goalie_x += goalie_random + - 10
            print('down_random:', middle_random)
        #################################
        # Draw game elements

        # fill background
        window.fill(BG_COLOR)

        # draw character
        pygame.draw.circle(window, BALL_COLOR,
                           (int(win_width), int(win_height)), 10)
        pygame.draw.circle(player_window, PLAYER_COLOR,
                           (int(player_x), int(player_y)), 10)
        pygame.draw.circle(ball_window, BALL_COLOR,
                           (int(ball_x), int(ball_y)), 10)
        pygame.draw.circle(goalie_window, GOALIE_COLOR,
                           (int(goalie_x), int(goalie_y)), 10)

        # draw the goal
        window.blit(goal_square, (goal_x, goal_y))
        window.blit(ball_square, (ball_x, ball_y))
        window.blit(player_square, (player_x, player_y))

        # Post-draw processing
        clock.tick(50)
        pygame.display.flip()

    pygame.quit()


main()
