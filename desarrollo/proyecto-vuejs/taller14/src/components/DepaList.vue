<template>
    <div class="pt-5">
        <div v-if="departamentos && departamentos.length">
            <div class="card mb-3" v-for="tdepartamento of departamentos" v-bind:key="departamento.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <span class="card-title"><b>Costo:</b> {{ departamento.costo_depa }}</span>
                            <br>
                            <span class="card-text"><b>Numero de Cuatos:</b> {{ departamento.num_cuartos }}</span>
                            <br>
                            <router-link :to="{name: 'edit_departamento', params: { id: departamento.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteDepartamento(telefono)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="card-text">Banios: {{ departamento.num_banios }}</p>
                            <p class="card-text">Valor: {{ departamento.valor}}</p>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <span class="card-text"><b>Propietario:</b> {{ departamento.propietario_str }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="departamentos.length == 0"> Sin Departamentos</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamentos: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteDepartamento: function(e) {
            if (confirm('Eliminar ' + e.departamento)) {
                axios.delete(e.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/departamento/')
                .then( response => {
                    this.departamentos = response.data
                });
        }
    },
}
</script>
