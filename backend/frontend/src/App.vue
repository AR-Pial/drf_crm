<template>
  <div class="">
    <div class="row min-vh-100 m-0">
      <div id="sidebar" class="col-12 col-md-2 d-none d-lg-block">
        <sidebar></sidebar>
      </div>
        
      <div class="col m-0 p-0">
        <div id="header" class="bg-light row m-0 p-0 bf-info">
          <div class="py-3">
            <app-header></app-header>
          </div>
          <lower-header></lower-header>
          

        </div>
        <router-view/>
      </div>
    </div>
    
  </div>
  
</template>

<script>
import SideBar from './components/SideBar.vue'
import HeaderApp from './components/HeaderApp.vue'
import LowerHeader from './components/LowerHeader.vue'

export default {
  components:{
    "sidebar": SideBar,
    "app-header": HeaderApp,
    "lower-header": LowerHeader
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
