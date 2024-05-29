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
            Schema::create('detalle_facturas', function (Blueprint $table) {
                $table->id('id_detalle');
                $table->unsignedBigInteger('id_factura');
                $table->unsignedBigInteger('id_producto');
                $table->decimal('precio_unitario', 10, 2);
                $table->timestamps();
            });
        }

        /**
         * Reverse the migrations.
         */
        public function down(): void
        {
            Schema::dropIfExists('detalle_facturas');
        }
    };
