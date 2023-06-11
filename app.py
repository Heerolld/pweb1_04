from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de pets
pets = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastro-pets', methods=['GET', 'POST'])
def cadastro_pets():
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        idade = request.form['idade']
        pet = {'nome': nome, 'raca': raca, 'idade': idade}
        pets.append(pet)
        return redirect('/pets')
    return render_template('cadastro_pets.html')

@app.route('/ver-pet/<int:id>')
def ver_pet(id):
    pet = pets[id] if id < len(pets) else None
    return render_template('ver_pet.html', pet=pet)

@app.route('/editar-pet/<int:id>', methods=['GET', 'POST'])
def editar_pet(id):
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        idade = request.form['idade']
        pet = {'nome': nome, 'raca': raca, 'idade': idade}
        if id < len(pets):
            pets[id] = pet
        return redirect('/pets')
    pet = pets[id] if id < len(pets) else None
    return render_template('editar_pet.html', pet=pet, id=id)

@app.route('/excluir-pet/<int:id>')
def excluir_pet(id):
    if id < len(pets):
        del pets[id]
    return redirect('/pets')

@app.route('/pets')
def listar_pets():
    return render_template('listar_pets.html', pets=pets)

if __name__ == '__main__':
    app.run(debug=True)
