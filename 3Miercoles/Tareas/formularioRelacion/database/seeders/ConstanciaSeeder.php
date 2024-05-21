<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Constancia;

class ConstanciaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        Constancia::create([
            'folio' => 'GVA-CC-SPPTR-21-3-395',
            'rfc' => 'JIGF790118',
            'curp' => 'JIGF790118HTCMNR17',
            'nombre' => 'JOSE FREDDY',
            'apellidos' => 'JIMENEZ GONZALEZ',
            'expedicion' => '2021-09-18',
            'vencimiento' => '2025-09-18',
            'duracion' => 24,
            'curso_id' => 1 // Asegúrate de que este ID coincida con un curso en CategoriaCursoSeeder
        ]);

        Constancia::create([
            'folio' => 'GVA-CC-SPPTR-21-3-396',
            'rfc' => 'XYZF790118',
            'curp' => 'XYZF790118HTCMNR17',
            'nombre' => 'MARIA FERNANDA',
            'apellidos' => 'LOPEZ MARTINEZ',
            'expedicion' => '2022-01-10',
            'vencimiento' => '2026-01-10',
            'duracion' => 30,
            'curso_id' => 2 // Asegúrate de que este ID coincida con un curso en CategoriaCursoSeeder
        ]);
    }
}
