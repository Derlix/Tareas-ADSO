<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Producto;

class ProductoSeeder extends Seeder
{

    public function run(): void
    {
        Producto::create(['nombre' => 'Producto A', 'precio' => 100.00]);
        Producto::create(['nombre' => 'Producto B', 'precio' => 200.00]);
    }
}
