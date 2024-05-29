<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\DetalleFactura;
use App\Models\Factura;
use App\Models\Producto;

class DetalleFacturaSeeder extends Seeder
{

    public function run(): void
    {
        $factura1 = Factura::first();
        $factura2 = Factura::find(2);
        $producto1 = Producto::first();
        $producto2 = Producto::find(2);

        $factura1->productos()->attach($producto1->id, ['cantidad' => 2]);
        $factura1->productos()->attach($producto2->id, ['cantidad' => 1]);
        $factura2->productos()->attach($producto1->id, ['cantidad' => 5]);
    }
}
