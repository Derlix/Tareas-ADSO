<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Factura extends Model
{
    use HasFactory;

    protected $fillable = [
        'cliente',
        'total',
        'fecha',
    ];

    public function detalleFacturas()
    {
        return $this->hasMany(DetalleFactura::class);
    }
}