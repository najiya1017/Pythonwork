
value={"item1":10,"item2":-30,"item3":-26,"item4":1}

absolute_values={k:v if v>=0 else -v for k,v in value.items()}

print(absolute_values)