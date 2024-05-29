<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Producto extends Model
{
    use HasFactory;

    public function facturas()
    {
        return $this->belongsToMany(Factura::class, 'detalle_facturas')
                    ->withPivot('cantidad')
                    ->withTimestamps();
    }
}
