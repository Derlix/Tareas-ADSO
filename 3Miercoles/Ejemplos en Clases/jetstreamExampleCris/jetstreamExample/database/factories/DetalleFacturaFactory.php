<?php

namespace Database\Factories;

use App\Models\DetalleFactura;
use App\Models\Factura;
use App\Models\Producto;
use Illuminate\Database\Eloquent\Factories\Factory;

class DetalleFacturaFactory extends Factory
{
    protected $model = DetalleFactura::class;

    public function definition(): array
    {
        $facturas = Factura::all();
        $productos = Producto::all();

        $factura = $this->faker->randomElement($facturas);
        $producto = $this->faker->randomElement($productos);

        return [
            'id_factura' => $factura->id_factura,
            'id_producto' => $producto->id_producto,
            'precio_unitario' => $producto->precio,
        ];
    }
}
