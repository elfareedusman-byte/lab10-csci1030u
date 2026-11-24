# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


from collections import deque


def eval_rpn(tokens):
    # Outline:
    # Use a list as a stack to store numbers.
    # For each token, if it is an operator (+, -, *, /), pop the top two numbers
    # (note: first popped is right operand b, second popped is left operand a),
    # apply the operation (using int(a / b) for division), and push the result back.
    # Otherwise, convert the token to int and push it. Return the final stack item.
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]


def decode_string(s):
    # Outline:
    # Use a stack to store (previous_string, repeat_count) pairs when entering '['.
    # Track current_str and current_num as we scan characters.
    # On digits, build current_num. On '[', push (current_str, current_num) and reset both.
    # On ']', pop (prev_str, k) and set current_str = prev_str + current_str * k.
    # On letters, append to current_str. Return current_str at the end.
    stack = []
    current_str = ""
    current_num = 0
    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif ch == "]":
            prev_str, repeat_count = stack.pop()
            current_str = prev_str + current_str * repeat_count
        else:
            current_str += ch
    return current_str


def daily_temperatures(temps):
    # Outline:
    # Initialize an answer list of 0s the same length as temps, and an empty stack
    # to hold indices of days still waiting for a warmer temperature.
    # For each day i and temp t, while the stack isn't empty and t > temps[stack[-1]],
    # pop the earlier index prev_i and set ans[prev_i] = i - prev_i.
    # Push i onto the stack and return ans.
    ans = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            prev_i = stack.pop()
            ans[prev_i] = i - prev_i
        stack.append(i)
    return ans


def num_islands(grid):
    # Outline:
    # Handle empty grid edge case. Track visited cells in a set and count islands.
    # Loop through every cell (r, c). Whenever we find an unvisited '1', increment
    # island count and run BFS using a deque to mark all connected '1's (up, down,
    # left, right) as visited. Return the total island count.
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                queue = deque([(r, c)])
                visited.add((r, c))
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
    return islands


if __name__ == "__main__":
    main()
