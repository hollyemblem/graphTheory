graph = {"a": ["c"],
         "b": ["c"],
         "c": ["a", "b"],
         "d": [],
         "e": [],
         "f": [],
         "h": [],
         "j": []
         }


# go through graph and get key values
# get connected values, e.g. c
# move to connected value and delete the variables associated with this connected value
#
counter = 0

for key in list(graph):
    if ((graph.get(key, ""))):
        variables = (graph.get(key, ""))
        if variables:
            for i in variables:
                variables_set_two = ((graph.get(i, "")))
                if variables_set_two:
                    counter = counter + 1
                    for v in variables_set_two:
                        try:
                            graph.pop(v)
                        except Exception:
                            pass
                    try:
                        graph.pop(i)
                    except Exception:
                        pass
                try:
                    graph.pop(key)
                except Exception:

                    pass

print(len(graph) + counter)