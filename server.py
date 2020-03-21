import graph

def main():
    game = graph.graph()
    print("---------------------")
    for v in game.vertices:
        print(f"Neighbors of {v}:", end=" ")
        for neighbor in game.vertices[v]:
            print(neighbor, end=" ")
        print()
        for neighbor in game.vertices[v]:
            print(game.weights[v][neighbor], end=" ")
        print()

    print("---------------------")



if __name__ == "__main__":
    main()
