def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arithmetic_problems = []
    top_operands = []
    bottom_operands = []
    operators = []
    answers = []
    format_width = []

    for problem in problems:
        problem = problem.split(" ")
        # split breaks problems into a list
        # problem[0] represents top_operands,  problem[1] represents operators ,problem[2] represents bottom_operands
        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."
        top_operands.append(problem[0])
        bottom_operands.append(problem[2])

        if max(len(problem[0]), len(problem[2])) > 4:
            return "Error: Numbers cannot be more than four digits."
        # format_width is stored in a list to make a direct call for formatting each problem
        format_width.append(max(len(problem[0]), len(problem[2])) + 2)

        if problem[1] == "-":
            answers.append(int(problem[0]) - int(problem[2]))
            operators.append("-")
        elif problem[1] == "+":
            answers.append(str(int(problem[0]) + int(problem[2])))
            operators.append("+")
        else:
            return "Error: Operator must be '+' or '-'."

    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []

    # loop to arrange individual rows
    for i in range(len(problems)):
        top_row.append(top_operands[i].rjust(format_width[i]))
        bottom_row.append(
            operators[i] + " " + bottom_operands[i].rjust(format_width[i] - 2)
        )
        dash_row.append("-" * (format_width[i]))
        answer_row.append(str(answers[i]).rjust(format_width[i]))

    # joining rows to format the problems horizontally
    arithmetic_problems.append("    ".join(top_row))
    arithmetic_problems.append("    ".join(bottom_row))
    arithmetic_problems.append("    ".join(dash_row))

    if show_answers:
        arithmetic_problems.append("    ".join(answer_row))

    return "\n".join(arithmetic_problems)


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
