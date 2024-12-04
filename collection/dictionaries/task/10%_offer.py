stationary={"pencil":5,"pencil box":55,"eraser packet":100,"eraser":5,"crayons":100}

offer={name:(v*10)//100 for name,v in stationary.items()}

print(offer)