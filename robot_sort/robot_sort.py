class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def reset(self):
        """
        Resets robot position to item at index zero and picks up first item
        """

        while self.can_move_left() == True:
            self.move_left()

        if self._list[self._position] == None:
            self.swap_item()

        # self.swap_item()


#Understand
    #inputs and outputs
    #input will be a list held in self._list
    #output will be a list in sorted order

    #the input array will need to be rearranged in place (no extra variables) to be returned at the end
    #the robot can only move one slot to the left or right at any given time
    #the robot cannot swap two items at once, if it puts a card down, it will be "holding" None. So this must be accounted for
    #the robot has a light with a boolean value

#Plan
    #implement a bubble-sort-like technique (since bubble sort uses no extra variables and is only concerned with the next item)
    #it will be slightly different than just a normal bubble sort since the robot has its own position separate from the position we might be at inside a loop, and it cannot simply swap two items. It must replace one with None.

    #Normal bubble sort uses a boolean which is flipped when a swap occurs. This way it knows that no more swaps have taken place and it is finished sorting. I will use the robots light as a substitute for this.

    #set the light on and pick up an item for comparison, then move right so we aren't comparing to none
        #check if the item we're holding is greater, less than, or equal to the item we're comparing it to
        #swap them accordingly

        #do this for each item in the array

        #when we have reached the end of the list, reset to 0
        #if we have done no swaps, the light should be on and we exit the loop, sorting complete
        #if we have done at least one swap, the light is still off and we continue through again





    def sort(self):
        """
        Sort the robot's list.
        """

        while self.light_is_on() == False:
            self.set_light_on()
            self.swap_item()
            self.move_right()

            for i in range(len(self._list)-1):                
                #next item is greater than current
                if self.compare_item() == 1:

                    #place greater value in correct spot
                    self.swap_item()
                    #move to empty space and place lower value down
                    self.move_left()
                    self.swap_item()
                    #move back to greater item and pick it up
                    self.move_right()
                    self.swap_item()
                    #a swap has ocurred, so turn light off
                    self.set_light_off()
                    #if this is not the last item continue right
                    if self.can_move_right() == True:
                        self.move_right()
                    #if this is the last value, put it down
                    else: 
                        self.swap_item()

                #next item is less than current
                elif self.compare_item() == -1:
                    if self.can_move_left() == True:
                        #go back to empty space and put down item
                        self.move_left()
                        self.swap_item()
                        #move forward to greater item and pick it up
                        self.move_right()
                        self.swap_item()
                        #it is not the last item continue right
                        if self.can_move_right() == True:
                            self.move_right()
                        #it is the last item, just put it back
                        else:
                            self.swap_item()

                    else:
                        self.swap_item()
                        self.move_right()
                        self.swap_item()

                #next item is the same as current    
                elif self.compare_item() == 0:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    if self.can_move_right() == True:
                        self.move_right()
                    else:
                        self.swap_item()

                elif self.compare_item() == None:
                    self.swap_item()
                    self.set_light_off()
                    
            #reset the robot position back to 0
            self.reset()       

        
        return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [50, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


    