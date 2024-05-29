<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Factura;
use App\Models\Producto;
use App\Models\DetalleFactura;

class DetalleFacturaSeeder extends Seeder

{
    public function run(): void
    {
        DetalleFactura::factory()->times(10)->create();
    }
}
