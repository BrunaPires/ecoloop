from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    return jsonify(f"Ola, {nome}!")

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    num1 = dados.get('num1', 0)
    num2 = dados.get('num2', 0)
    try:
        resultado = float(num1) + float(num2)
        return jsonify({"resultado": resultado})
    except (ValueError, TypeError):
        return jsonify({"erro": "Valores inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)
