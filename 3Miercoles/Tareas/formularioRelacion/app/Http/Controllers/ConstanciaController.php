<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Constancia;

class ConstanciaController extends Controller
{
    public function index()
    {
        $constancias = Constancia::with('categoriaCurso')->get();
        return view('index', compact('constancias'));
    }

    public function show($id)
    {
        $constancia = Constancia::with('categoriaCurso')->find($id);

        if (!$constancia) {
            abort(404);
        }

        return view('show', compact('constancia'));
    }
}
