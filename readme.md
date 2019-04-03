This is an ongoing piece of work translating the Connectivity Algorithm into Python. The algorithm is a
 adapted from <i>Discrete Mathematics for Computing</i>, by Rod Haggarty.

Let G = (V,E) be a graph. The algorithm computes the value of c = c(G), the number of connected components of G:

```
begin
   V' := V; 
   c := 0;
   while V' != empty do
      begin
         Choose y member of V'
         Find all vertices joined to y by some path<br/>
         Remove these vertices and y from V' and corresponding edges from E;
         c := c + 1
      end
end
```

This algorithm hasn't been unit tested (it's coming) or put through the ringer, so read at your own peril.

