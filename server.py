import graph

from flask import Flask,render_template, request,jsonify,Response

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    game = graph.graph(15)
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
    return render_template("home.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
