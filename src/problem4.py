"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Jun Fan.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------

    p = Pig(100)
    print('TEST 1')
    print('-----------------------------------')
    print('expected weight: 100')
    print('actual weight:', p.weight)
    print('-----------------------------------')
    print('expected get_weight: 100')
    print('actual get_weight:', p.get_weight())

    p.eat(100)
    print('-----------------------------------')
    print('expected weight after eat: 200')
    print('actual weight after eat:', p.get_weight())

    p.eat_for_a_year()
    print('-----------------------------------')
    print('expected weight after eat a year:', 200 + 366 * 365 / 2)
    print('actual weight after eat a year:', p.get_weight())

    k = Pig(300)
    print('-----------------------------------')
    print('expected heavier pig:', 'this pig')
    print('actual heavier pig:', p.heavier_pig(k))

    q = Pig(300)
    print('-----------------------------------')
    print('expected heavier pig:', 'same weight')
    print('actual heavier pig:', k.heavier_pig(q))

    q = Pig(100)
    print('-----------------------------------')
    print('expected heavier pig:', 'other pig')
    print('actual heavier pig:', q.heavier_pig(k))

    i = k.new_pig(q)
    print('-----------------------------------')
    print('expected weight: 300')
    print('actual weight:', i.weight)


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        self.weight = weight
        # DONE: Implement and test this method.

    def get_weight(self):
        """ Returns this Pig's weight. """
        return self.weight
        # DONE: Implement and test this method.

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        self.weight = self.weight + pounds_of_slop
        # DONE: Implement and test this method.

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        for k in range(365):
            self.eat(k + 1)
        # DONE: Implement and test this method.

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        if self.weight > other_pig.get_weight():
            return 'this pig'
        if self.weight < other_pig.get_weight():
            return 'other pig'
        if self.weight == other_pig.get_weight():
            return 'same weight'
        # DONE: Implement and test this method.

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        if self.weight >= other_pig.get_weight():
            return Pig(self.weight)
        if self.weight < other_pig.get_weight():
            return Pig(other_pig.get_weight)
        # DONE: Implement and test this method.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
