# Program 2 emulating circuits
# This program solves for the outputs of the different types of gates
# Daniel Jaffe
# Date Last Modified: 6/5/24

# Parent Gate class
class Gate:
    def __init__(self, input1):
        self._input1 = input1

    def get_input1(self):
        return self._input1

    def set_input1(self, input1):
        self._input1 = input1

    input1 = property(get_input1, set_input1)

    def evaluate(self):
        return 0

    def __str__(self):
        return str(self.evaluate())


# And Gate
class AND_Gate(Gate):
    def __init__(self, input1, input2):
        super().__init__(input1)
        self._input2 = input2

    def get_inputs2(self):
        return self._input2

    def set_inputs2(self, input2):
        self._input2 = input2

    input2 = property(get_inputs2, set_inputs2)

    def evaluate(self):
        if self.input1 == 1 and self.input2 == 1:
            return 1
        else:
            return 0


# Or Gate
class OR_Gate(Gate):
    def __init__(self, input1, input2):
        super().__init__(input1)
        self._input2 = input2

    def get_inputs2(self):
        return self._input2

    def set_inputs2(self, input2):
        self._input2 = input2

    input2 = property(get_inputs2, set_inputs2)

    def evaluate(self):
        if self._input1 == 1 or self._input2 == 1:
            return 1
        else:
            return 0


# Not Gate
class not_Gate(Gate):
    def __init__(self, input1):
        super().__init__(input1)

    def evaluate(self):
        if self._input1 == 1:
            return 0
        if self._input1 == 0:
            return 1


# And truth table subroutine
def and_truth_table(and_gate_inputs):
    # Basic And Gate
    print("AND Gate")
    print("A B OUT")
    for Gate in and_gate_inputs:
        print(Gate.input1, Gate.input2, Gate.evaluate())


# OR truth table subroutine
def or_truth_table(or_gate_inputs):
    # Basic And Gate
    print("OR Gate")
    print("A B OUT")
    for Gate in or_gate_inputs:
        print(Gate.input1, Gate.input2, Gate.evaluate())


# NOT truth table subroutine
def not_truth_table(not_gate_inputs):
    # Basic And Gate
    print("NOT Gate")
    print("A OUT")
    for Gate in not_gate_inputs:
        print(Gate.input1, Gate.evaluate())


# NAND truth table subroutine
def nand_truth_table(and_gate_inputs):
    print("NAND Gate")
    print("A B OUT")
    for Gate in and_gate_inputs:
        print(Gate.input1, Gate.input2, not_Gate(Gate.evaluate()))


# Circuits drawing 1
def circuit_drawing_1(circuit_drawing_inputs):
    print("Circuit Drawing 1")
    print("A B C OUT")
    for input in circuit_drawing_inputs:
        # a and b
        a_and_b = (AND_Gate(input[0], input[1])).evaluate()
        # Not c
        not_c = not_Gate(input[2]).evaluate()
        # (a and b) or not c
        final_product = (OR_Gate(a_and_b, not_c)).evaluate()
        print(input[0], input[1], input[2], final_product)


def circuit_drawing_2(circuit_drawing_inputs):
    print("Circuit Drawing 2")
    print("p q r OUT")
    for input in circuit_drawing_inputs:
        # p and q
        p_and_q = (AND_Gate(input[0], input[1])).evaluate()
        # not(p and q)
        not_p_and_q = not_Gate(p_and_q).evaluate()
        # p and r
        p_and_r = (AND_Gate(input[0], input[2])).evaluate()
        # Not r
        not_r = not_Gate(input[2]).evaluate()
        # not(p and q) or (p and r)
        not_p_and_q_or_p_and_r = (OR_Gate(not_p_and_q, p_and_r)).evaluate()
        # Final Product
        final_product = AND_Gate(not_p_and_q_or_p_and_r, not_r).evaluate()
        print(input[0], input[1], input[2], final_product)


# Main program
# Inputs
and_gate_inputs = [AND_Gate(0, 0), AND_Gate(0, 1), AND_Gate(1, 0), AND_Gate(1, 1)]
or_gate_inputs = [OR_Gate(0, 0), OR_Gate(0, 1), OR_Gate(1, 0), OR_Gate(1, 1)]
not_gate_inputs = [not_Gate(0), not_Gate(1), not_Gate(0), not_Gate(1)]
circuit_drawing_inputs = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

# Retrieving from subroutine
and_truth_table(and_gate_inputs)
or_truth_table(or_gate_inputs)
not_truth_table(not_gate_inputs)
nand_truth_table(and_gate_inputs)
circuit_drawing_1(circuit_drawing_inputs)
circuit_drawing_2(circuit_drawing_inputs)
