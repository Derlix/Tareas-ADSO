<!DOCTYPE html>
<html>

<head>
    <title>Facturas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>


    <div style="display: flex; align-items: center;">
        <div style="width: 100px; margin-right: 20px;">
            <a href="{{ route('dashboard') }}" class="d-block h-9 w-auto m-4">
                <x-application-mark />
            </a>
        </div>
        <a href="{{ route('dashboard') }}" 
           class="btn btn-primary m-2 {{ request()->routeIs('dashboard') ? 'active' : '' }}">
            {{ __('Dashboard') }}
        </a>
        <a href="{{ route('vistaPersonal') }}"
           class="btn btn-primary m-2{{ request()->routeIs('vistaPersonal') ? 'active' : '' }}">
            {{ __('vistaPersonal') }}
        </a>
    </div>



    <div class="container my-5">

        <h2 class="mb-3">Facturas</h2>
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Cliente</th>
                    <th>Total</th>
                    <th>Fecha</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($facturas as $factura)
                    <tr>
                        <td>{{ $factura->id_factura }}</td>
                        <td>{{ $factura->cliente }}</td>
                        <td>{{ $factura->total }}</td>
                        <td>{{ $factura->fecha }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>

        <h2 class="mb-3">Detalles de Factura</h2>
        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th>ID Factura</th>
                    <th>ID Producto</th>
                    <th>Precio Unitario</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($detalles as $detalle)
                    <tr>
                        <td>{{ $detalle->id_factura }}</td>
                        <td>{{ $detalle->id_producto }}</td>
                        <td>{{ $detalle->precio_unitario }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>

        <h2 class="mb-4">Productos</h2>
        <table class="table">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Stock</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($productos as $producto)
                    <tr>
                        <td>{{ $producto->nombre }}</td>
                        <td>{{ $producto->precio }}</td>
                        <td>{{ $producto->stock }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>

    </div>
</body>

</html>
