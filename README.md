# math-genealogy-graph

Generate a DOT file containing a mathematician's genealogy using data from the [Mathematics Genealogy Project](https://www.mathgenealogy.org/).

## Example

Carl Friedrich Gauß has Mathematics Genealogy Project identifier 18231.
You can verify this by searching for him on their website (see https://www.mathgenealogy.org/id.php?id=18231).
To produce his graph, run the following:

```shell
./math-genealogy-graph.py 18231 > graph.dot
```

You can feed the [resulting file](https://raw.githubusercontent.com/parsiad/math-genealogy-graph/main/18231.dot) to [Graphviz](https://graphviz.org) to produce an image like the one below.
If you do not have Graphviz installed on your machine, you can instead copy the contents of `graph.dot` to a tool like [Graphviz Online](https://dreampuf.github.io/GraphvizOnline/) and have them render it for you.

[![alt text](https://raw.githubusercontent.com/parsiad/math-genealogy-graph/main/18231.svg)](https://raw.githubusercontent.com/parsiad/math-genealogy-graph/main/18231.svg)
