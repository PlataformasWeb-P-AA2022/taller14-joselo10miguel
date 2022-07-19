<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo_depa">COSTO</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo_depa"
                    v-model="departamento.costo_depa"
                    v-validate="'required'"
                    name="costo_depa"
                    placeholder="Ingres "
                    :class="{'is-invalid': errors.has('departamento.costo_depa') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid costo.
                </div>
            </div>

            <div class="form-group">
                <label for="tipo">Tipo</label>
                <input
                   type="text"
                    class="form-control"
                    id=" valor"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name=" valor"
                    placeholder="Ingrese "
                    :class="{'is-invalid': errors.has('departamento. valor') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="propietario">PROPIETARIO</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in PropietarioList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>

            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
              departamento: {
                costo_depa: '',
                num_cuartos: '',
                num_banios: '',
                valor: '',
                propietario: '',
            },
            PropietarioList: [],
            submitted: false
        }
    },
    mounted() {
        this.getEstudiantesList(),
        axios.get('http://127.0.0.1:8000/api/departamento/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.departamento = response.data
        });
    },
    methods: {
      getEstudiantesList() {
            axios
            .get('http://127.0.0.1:8000/api/propietario/')
            .then(response => {
                this.PropietarioList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/departamento/${this.departamento.id}/`,
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamento');
                    })
            });
        }
    },
}
</script>
