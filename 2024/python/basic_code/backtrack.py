def backtrack(cnadidate):
    if find_solution(cnadidate):
        output(candidate)
        return

    for next_candidate in list_of_candidates:
        if is_vaild(next_candidate):
            place(next_candidate)
            backtrack(next_candidate)
            remove(next_candidate)