<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\CategoriaCurso;

class CategoriaCursoSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run()
    {
        CategoriaCurso::create(['curso' => 'Curso de Programación']);
        CategoriaCurso::create(['curso' => 'Curso de Diseño']);
    }
}
