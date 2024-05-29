<?php

namespace App\Http\Controllers;

use App\Models\Factura;
use App\Models\DetalleFactura;
use Illuminate\Http\Request;
use App\Models\Producto;

class FacturaController extends Controller
{
    public function vistaPersonal()
    {
        $facturas = Factura::all();
        $productos = Producto::all();
        $detalles = DetalleFactura::all();

        return view('vista-personal', compact('facturas', 'productos', 'detalles'));
    }
}
