stationary={"pencil":5,"pencil box":55,"eraser packet":100,"eraser":5,"crayons":100}

after_filtering=[k for k,v in stationary.items() if v>50]

print(after_filtering)