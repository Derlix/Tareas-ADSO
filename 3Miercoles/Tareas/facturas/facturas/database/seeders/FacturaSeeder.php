<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Factura;

class FacturaSeeder extends Seeder
{

    public function run(): void
    {
        Factura::create(['nombre_cliente' => 'Juan Pérez']);
        Factura::create(['nombre_cliente' => 'María López']);
    }
}
