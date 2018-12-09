# -*- coding: utf-8 -*-
"""
--- Day 7: The Sum of Its Parts ---

You find yourself standing on a snow-covered coastline; apparently, you landed a little off course.
The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be
trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating
a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak;
you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator?
"Those clothes don't look very warm; take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment.
You see, believe it or not, this box contains something that will solve all of Santa's transportation problems -
at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read
whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!"
They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others
can begin (your puzzle input). Each step is designated by a single letter.
For example, suppose you have the following instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.

Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----

Your first goal is to determine the order in which the steps should be completed. If more than one step is ready,
choose the step which is first alphabetically. In this example, the steps would be completed as follows:

Only C is available, and so it is done first. Next, both A and F are available.
A is first alphabetically, so it is done next. Then, even though F was available earlier, steps B and D are
now also available, and B is the first alphabetically of the three. After that, only D and F are available.
E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
F is the only choice, so it is done next.
Finally, E is completed.

So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?

"""

from collections import defaultdict


def organize_instructions(instruction_raw: list) -> dict:
    """
    Generates a dictionary of Instruction KEY: [Instruction Blocking VALUE(s)]

    Arguments (list): Raw string of instruction data
    """

    formatted = defaultdict(list)
    for line in instruction_raw:
        words = line.split()
        formatted[words[1]].append(words[7])

    return formatted


def get_instruction_dependencies(instructions: dict) -> tuple:
    """
    Collects all blocked and unblocked values in dictionary and stores them in a list to parse in order later

    Arguments:
        instructions (dict): Organized instructions
    """
    blocked = []
    for blockers in instructions.values():
        blocked += blockers
    unblocked = [x for x in list(instructions.keys()) if x not in blocked]
    return blocked, unblocked


def get_instruction_order(instructions: dict) -> str:
    """
    Determines the order of which the steps are to be completed, keeping alphabetical order in check if
    more than one step is ready.

    Arguments:
        instructions (dict): Organized instructions
    """
    order = []
    blocked, unblocked = get_instruction_dependencies(instructions)
    while bool(unblocked):
        completed = min(unblocked)
        for i in instructions[completed]:
            if i in blocked:
                blocked.remove(i)
            if i not in blocked:
                unblocked.append(i)
        unblocked.remove(completed)
        order.append(completed)
    return ''.join(order)


def get_time_with_workers(instructions: dict, max_elf_helpers: int, time_delay: int) -> int:
    """
    Calculates how long the instructions would take to execute with maximum number of elf helpers.

    Arguments:
        instructions (dict): Organized instructions
        max_elf_helpers (int): Maximum number of elves available to help
        time_delay (int): Time offset for each step duration
    """
    elves = time = 0
    completed = list()
    completion_dict = defaultdict(list)
    blocked, unblocked = get_instruction_dependencies(instructions)
    time_to_complete = 0

    while blocked or unblocked:
        if time in completion_dict:
            for j in completion_dict[time]:
                for i in instructions[j]:
                    if i in blocked:
                        blocked.remove(i)
                    if i not in blocked:
                        unblocked.append(i)
                        elves -= 1
                completed.append(j)
        for i in range(len(unblocked)):
            if elves < max_elf_helpers and unblocked:
                elves += 1
                step = min(unblocked)
                time_to_complete = (ord(min(unblocked).lower()) - 96 + time_delay) + time
                completion_dict[time_to_complete].append(step)
                unblocked.remove(step)
        time += 1
    return time_to_complete


if __name__ == "__main__":

    # Import each instruction as a list value
    instruction_list = organize_instructions(open("puzzle_inputs/input_day_7.txt", 'r').readlines())

    print(get_instruction_order(instruction_list),
          get_time_with_workers(instruction_list, 5, 60))
