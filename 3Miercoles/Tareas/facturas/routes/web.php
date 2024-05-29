<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\FacturaController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/facturas', [FacturaController::class, 'index']);
