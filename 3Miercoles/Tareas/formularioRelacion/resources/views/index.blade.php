<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Principal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        .card-container {
            margin-top: 20px;
        }
        .card {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center my-4">Página Principal</h1>
        <div class="row card-container">
            @foreach($constancias as $constancia)
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-header bg-primary text-white">
                            Constancia ID: {{ $constancia->id }}
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">{{ $constancia->nombre }} {{ $constancia->apellidos }}</h5>
                            <p class="card-text"><strong>Folio:</strong> {{ $constancia->folio }}</p>
                            <p class="card-text"><strong>RFC:</strong> {{ $constancia->rfc }}</p>
                            <p class="card-text"><strong>CURP:</strong> {{ $constancia->curp }}</p>
                            <p class="card-text"><strong>Curso:</strong> {{ $constancia->categoriaCurso->curso }}</p>
                            <a href="{{ url('/constancia/' . $constancia->id) }}" class="btn btn-primary">Ver Detalles</a>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+Fmgm1a02VbEvoEh3sl0sibVcOQVnN" crossorigin="anonymous"></script>
</body>
</html>
