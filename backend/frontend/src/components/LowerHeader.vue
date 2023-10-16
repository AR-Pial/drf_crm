<template>
    <div class="w-100 m-0 p-0">
        <hr class="m-0 p-0">
          <div class="m-0 p-2 row">
            <div class="col-6">
                <slot name="page-title"></slot>
            </div>
            <nav aria-label="breadcrumb" class="col-6">
              <ol class="breadcrumb m-0 p-0 d-flex justify-content-end">
                <li class="breadcrumb-item text-end"><a href="#">Dashboard</a></li>
                <!-- <li class="breadcrumb-item"><a href="#">Library</a></li>
                <li class="breadcrumb-item active" aria-current="page">Data</li> -->
                <slot name="breadcrumb"></slot>
              </ol>
            </nav>
          </div>
    </div>
  </template>
  
  <script>
  export default {

  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

  </style>
  