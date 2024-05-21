<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class CategoriaCurso extends Model
{
    protected $fillable = ['curso'];

    public function constancias()
    {
        return $this->hasMany(Constancia::class, 'curso_id');
    }
}
