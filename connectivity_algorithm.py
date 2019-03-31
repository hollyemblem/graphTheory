graph = {"a": ["c"],
         "b": ["c", "e", "d"],
         "c": ["a", "b", "e", ],
         "d": ["b"],
         "e": ["c", "b"],
         "f": []
         }


## graph logic pinched from https://www.python-course.eu/graphs_python.php

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges


variable = (generate_edges(graph))

# go through graph and get key values
# get connected values, e.g. c
# move to connected value and delete the variables associated with this connected value
#
counter = 0

for key in list(graph):
    if ((graph.get(key, ""))):
        counter = counter + 1
        variables = (graph.get(key, ""))
        if variables:
            for i in variables:
                variables_set_two = ((graph.get(i, "")))
                if variables_set_two:
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