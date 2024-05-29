<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facturas</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h1 class="text-center mb-4">Facturas</h1>
        @foreach ($facturas as $factura)
            <div class="card mb-3">
                <div class="card-header">
                    <h2 class="h5 mb-0">Cliente: {{ $factura->nombre_cliente }}</h2>
                </div>
                <div class="card-body">
                    <ul class="list-group">
                        @foreach ($factura->productos as $producto)
                            <li class="list-group-item d-flex justify-content-between align-items-center">
                                {{ $producto->nombre }} - Precio: ${{ $producto->precio }}
                                <span class="badge badge-primary badge-pill">Cantidad: {{ $producto->pivot->cantidad }}</span>
                            </li>
                        @endforeach
                    </ul>
                </div>
            </div>
        @endforeach
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
