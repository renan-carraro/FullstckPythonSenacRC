from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = """
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Total Fit Academia</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #fff;
        }

        header {
            background-color: #ff5733;
            padding: 20px;
            text-align: center;
        }

        nav ul {
            list-style: none;
            padding: 0;
        }

        nav ul li {
            display: inline;
            margin: 10px;
        }

        nav ul li a {
            color: #fff;
            text-decoration: none;
        }

        section {
            padding: 50px;
            text-align: center;
        }

        .plano {
            display: inline-block;
            background: #333;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: #222;
        }
    </style>
</head>
<body>
    <header>
        <h1>Total Fit Academia</h1>
        <nav>
            <ul>
                <li><a href="#sobre">Sobre</a></li>
                <li><a href="#planos">Planos</a></li>
                <li><a href="#contato">Contato</a></li>
            </ul>
        </nav>
    </header>

    <section id="sobre">
        <h2>Sobre nós</h2>
        <p>Venha treinar na melhor academia da cidade! Equipamentos modernos, treinadores experientes e um ambiente motivador.</p>
    </section>

    <section id="planos">
        <h2>Nossos Planos</h2>
        <div class="plano">
            <h3>Básico</h3>
            <p>Treino livre + acesso à área de musculação.</p>
            <p>R$ 99/mês</p>
        </div>
        <div class="plano">
            <h3>Premium</h3>
            <p>Acesso total + aulas exclusivas.</p>
            <p>R$ 199/mês</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2025 Total Fit Academia - Todos os direitos reservados.</p>
    </footer>
</body>
</html>
    """
    return HttpResponse(html)