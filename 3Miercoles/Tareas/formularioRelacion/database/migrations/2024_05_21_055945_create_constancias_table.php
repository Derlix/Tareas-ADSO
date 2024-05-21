<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('constancias', function (Blueprint $table) {
            $table->id();
            $table->string('folio');
            $table->string('rfc');
            $table->string('curp');
            $table->string('nombre');
            $table->string('apellidos');
            $table->date('expedicion');
            $table->date('vencimiento');
            $table->integer('duracion');
            $table->unsignedBigInteger('curso_id');
            $table->timestamps();
            
            $table->foreign('curso_id')->references('id')->on('categoria_cursos')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('constancias');
    }
};
