class REDGREENBLUEADT:
    def __init__(self, size = 12):
        self.size = size  # set initial size of the array to 12, TimeComplexity: O(1)
        self.stack = [None] * size  # Create a list with index but no elements/none , TimeComplexity: O(size)
        self.red_top = -1  # Red stack starts at -1, empty, TimeComplexity: O(1)
        self.green_top = self.size // 3 - 1  # Green starts after red top which is 3, TimeComplexity: O(1)
        self.blue_top = 2 * (self.size // 3) - 1  # Blue starts after green top which is 7, TimeComplexity: O(1)

    def expand_array(self):
        self.size += 3 #size(12 or N)+3, TimeComplexity: O(1)
        self.stack.insert(self.red_top + 1, None)  # add empty at top of red, TimeComplexity: O(1)
        self.stack.insert(self.green_top + 1, None)  # add empty at top of green, TimeComplexity: O(1)
        self.stack.insert(self.blue_top + 1, None)  # add empty at top of blue, TimeComplexity: O(1)
        self.red_top += 1# TimeComplexity: O(1)
        self.green_top += 1# TimeComplexity: O(1)
        self.blue_top += 1# TimeComplexity: O(1)

    def push_red(self, item):
        if self.red_top + 1 == self.size // 3:  # If red stack is full, TimeComplexity: O(1)
            self.expand_array()  # call expand array when nessasary, TimeComplexity: O(1)
        self.red_top += 1  # increase red stack index by 1, TimeComplexity: O(1)
        self.stack[self.red_top] = item  # Place the item at the top of the red stack, TimeComplexity: O(1)

    def push_green(self, item):
        if self.green_top + 1 == (2 * (self.size // 3)):  # If green stack is full, TimeComplexity: O(1)
            self.expand_array()  # call expand array when nessasary, TimeComplexity: O(1)
        self.green_top += 1  # increase green stack index by 1, TimeComplexity: O(1)
        self.stack[self.green_top] = item  # Place the item at the top of the green stack, TimeComplexity: O(1)

    def push_blue(self, item):
        if self.blue_top + 1 == self.size:  # If blue stack is full, TimeComplexity: O(1)
            self.expand_array()  # call expand array when nessasary, TimeComplexity: O(1)
        self.blue_top += 1  # increase blue stack index by 1, TimeComplexity: O(1)
        self.stack[self.blue_top] = item  # Place the item at the top of the blue stack, TimeComplexity: O(1)

    def pop_red(self):
        if self.red_top == -1:  # Check if the red stack is empty so it doesnt remove nothing , TimeComplexity: O(1)
            raise IndexError('Red empty')
        item = self.stack[self.red_top]  # Get the item at the top of the red stack , TimeComplexity: O(1)
        self.red_top -= 1  # -1 index since top was removed, TimeComplexity: O(1)
        return item  # Return removed item, TimeComplexity: O(1)

    def pop_green(self):
        if self.green_top == self.size // 3 - 1:  # Check if the green stack is empty so it doesnt remove nothing , TimeComplexity: O(1)
            raise IndexError('Green empty')
        item = self.stack[self.green_top]  # get the item at the top of the green stack, TimeComplexity: O(1)
        self.green_top -= 1  # -1 index since top was removed, TimeComplexity: O(1)
        return item  # Return removed item, TimeComplexity: O(1)

    def pop_blue(self):
        if self.blue_top == 2 * (self.size // 3) - 1:  # Check if the green stack is empty so it doesnt remove nothing, TimeComplexity: O(1)
            raise IndexError('Blue empty')
        item = self.stack[self.blue_top]  # Get the item at the top of the blue stack, TimeComplexity: O(1)
        self.blue_top -= 1  # -1 index since top was removed, TimeComplexity: O(1)
        return item  # Return removed item

    def peek_red(self):
        if self.red_top == -1:  # check first so it doesnt return nothing , TimeComplexity: O(1)
            raise IndexError('Red empty')
        return self.stack[self.red_top]  #return top of red, TimeComplexity: O(1)

    def peek_green(self):
        if self.green_top == self.size // 3 - 1:  # check first so it doesnt return nothing, TimeComplexity: O(1)
            raise IndexError('Green empty')
        return self.stack[self.green_top]  #return top of green, TimeComplexity: O(1)

    def peek_blue(self):
        if self.blue_top == 2 * (self.size // 3) - 1:  # check first so it doesnt return nothing, TimeComplexity: O(1)
            raise IndexError('Blue empty')
        return self.stack[self.blue_top]  #return top of blue, TimeComplexity: O(1)

    def size_red(self):
        return self.red_top + 1  #array starts at 0 so need + 1, TimeComplexity: O(1)

    def size_green(self):
        return self.green_top - (self.size // 3 - 1)  #array size divided by 3 minus 1 - index of green top, TimeComplexity: O(1)

    def size_blue(self):
        return self.blue_top - (2 * (self.size // 3) - 1)  #array size divide by 3 minus 1 * 2 minus index of green top, TimeComplexity: O(1)

    def is_empty_red(self):
        return self.red_top == -1  # -1 means array is empty for red array, red starts at -1, TimeComplexity: O(1)

    def is_empty_green(self):
        return self.green_top == self.size // 3 - 1  # Return bool if array starting at 3, TimeComplexity: O(1)

    def is_empty_blue(self):
        return self.blue_top == 2 * (self.size // 3) - 1  #Return bool if array starting at 7, TimeComplexity: O(1)
