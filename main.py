import graph

def main():
    game = graph.graph()
    print("---------------------")
    for v in game.vertices:
        print(f"Neighbors of {v}:", end=" ")
        for neigh in game.vertices[v]:
            print(neigh, end=" ")
        print()
    print("---------------------")



if __name__ == "__main__":
    main()
