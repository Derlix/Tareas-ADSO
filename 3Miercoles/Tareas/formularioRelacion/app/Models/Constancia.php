<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Constancia extends Model
{
    protected $fillable = [
        'folio', 'rfc', 'curp', 'nombre', 'apellidos', 'expedicion', 'vencimiento', 'duracion', 'curso_id'
    ];

    public function categoriaCurso()
    {
        return $this->belongsTo(CategoriaCurso::class, 'curso_id');
    }
}
