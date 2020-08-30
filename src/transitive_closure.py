import sys
from random import Random

from pyspark.sql import SparkSession

numEdges = 200
numVertices = 100
rand = Random(42)


def generateGraph():
    edges = set()
    while len(edges) < numEdges:
        src = rand.randrange(0, numVertices)
        dst = rand.randrange(0, numVertices)
        if src != dst:
            edges.add((src, dst))
    return edges


if __name__ == "__main__":
    """
    Usage: transitive_closure [partitions]
    """
    spark = SparkSession.builder.appName("PythonTransitiveClosure").getOrCreate()

    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    tc = spark.sparkContext.parallelize(generateGraph(), partitions).cache()

    # Linear transitive closure: each round grows paths by one edge,
    # by joining the graph's edges with the already-discovered paths.
    # e.g. join the path (y, z) from the TC with the edge (x, y) from
    # the graph to obtain the path (x, z).

    # Because join() joins on keys, the edges are stored in reversed order.
    edges = tc.map(lambda x_y: (x_y[1], x_y[0]))

    oldCount = 0
    nextCount = tc.count()
    while True:
        oldCount = nextCount
        # Perform the join, obtaining an RDD of (y, (z, x)) pairs,
        # then project the result to obtain the new (x, z) paths.
        new_edges = tc.join(edges).map(lambda __a_b: (__a_b[1][1], __a_b[1][0]))
        tc = tc.union(new_edges).distinct().cache()
        nextCount = tc.count()
        if nextCount == oldCount:
            break

    print("TC has %i edges" % tc.count())

    spark.stop()
