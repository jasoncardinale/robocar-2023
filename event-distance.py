import time

MAX_STEER_LEFT = 0
MAX_STEER_RIGHT = 180
LANE_WEIGHT = 0.5
OBSTACLE_WEIGHT = 0.9

def sensors():
    pass


def calculateSteering(leftLaneVal, rightLaneVal, obstacleVal):
    # Determine how off centered 
    laneDeviation = (leftLaneVal - rightLaneVal)

    # Calculate weighted sum of lane deviation and obstacle avoidance
    steeringAngle = (LANE_WEIGHT * laneDeviation) + (OBSTACLE_WEIGHT * obstacleVal)

    # Convert steering angle to servo angle (0 to 180)
    servo_angle = MAX_STEER_LEFT + ((MAX_STEER_RIGHT - MAX_STEER_LEFT) / 2) + (steeringAngle * ((MAX_STEER_RIGHT - MAX_STEER_LEFT) / 2))
