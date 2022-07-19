
<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Administración de Estudiante</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">+ Estudiante</router-link>
        <br>
        <router-link to="/departamentos" class="btn btn-sm btn-primary">ver departamentos</router-link>
        <br>
        <router-link to="/create_departamento" class="btn btn-sm btn-primary">+ departamento</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>