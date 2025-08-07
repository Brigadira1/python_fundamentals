def shortest_with_base_case(make_recursive_call: bool) -> None:
    print(f"shortest_with_base_case({make_recursive_call}) called")

    if not make_recursive_call:
        print("Returning from the base case.")
        return
    else:
        shortest_with_base_case(False)
        print("Returning from the recursive case.")
        return

print("Calling shortest_with_base_case False)")
shortest_with_base_case(False)
print()
print("Calling shortest_with_base_case(True)")
shortest_with_base_case(True)
