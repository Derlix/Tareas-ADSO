<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\ConstanciaController;

Route::get('/', function () {
    return view('index'); 
});



Route::get('/', [ConstanciaController::class, 'index']);
Route::get('/constancia/{id}', [ConstanciaController::class, 'show']);
