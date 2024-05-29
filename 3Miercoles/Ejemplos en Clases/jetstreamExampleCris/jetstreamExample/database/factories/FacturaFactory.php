<?php

namespace Database\Factories;

use App\Models\Factura;
use Illuminate\Database\Eloquent\Factories\Factory;

class FacturaFactory extends Factory
{
    protected $model = Factura::class;

    public function definition(): array
    {
        return [
            'cliente' => $this->faker->name,
            'total' => $this->faker->randomFloat(2, 100, 1000),
            'fecha' => $this->faker->date(),
        ];
    }
}