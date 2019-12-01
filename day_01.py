# -*- coding: utf-8 -*-
"""
### Day 1: The Tyranny of the Rocket Equation ###

--- Part One ---

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed
for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

--- Part Two ---

During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence.
Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.
However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative
fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing
really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated
as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583+11192+3728+1240+411+135+43+12+2 = 50346.

What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the
mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

"""


def _get_fuel_required(mass: int) -> int:
    """
    Algorithm provided to calculate fuel based on mass
    :param int mass: Mass to be lifted
    :return: Fuel required to lift mass
    """
    return (mass // 3) - 2


def fuel_counter_upper(modules):
    module_fuel_sum = 0
    actual_fuel_sum = 0

    for mass in modules:
        current_fuel = _get_fuel_required(int(mass))
        module_fuel_sum += current_fuel

        while current_fuel > 0:
            actual_fuel_sum += current_fuel
            current_fuel = _get_fuel_required(current_fuel)

    return module_fuel_sum, actual_fuel_sum


if __name__ == "__main__":
    with open("puzzle_inputs/input_day_01.txt", 'r') as data:
        module_sum, actual_sum = fuel_counter_upper(data)
        print("Part One:", module_sum, "Part Two:", actual_sum)
