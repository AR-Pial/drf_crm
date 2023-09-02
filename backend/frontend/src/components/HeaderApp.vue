<template>
	<div class="row">
		<div id="open_sidebar" class="col-2  d-lg-none">
			<svg xmlns="http://www.w3.org/2000/svg" height="1.5em" viewBox="0 0 448 512">
				<path d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"/>
			</svg>
		</div>
		<div class="col">
			<ul class="d-flex m-0 p-0 align-items-center">
				<li><router-link :to="{name: 'dashboard'}">Dashboard</router-link></li>

				<li class="nav-item dropdown ms-lg-auto">
                        <a class="nav-link" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            <svg xmlns="http://www.w3.org/2000/svg" height="1.3em" viewBox="0 0 448 512">
                                <path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/>
                            </svg>
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end overflow-hidden" aria-labelledby="navbarDropdownMenuLink">
                            <li class=""><a class="dropdown-item m-0" href="#">Profile</a></li>
                            <li class=""><a class="dropdown-item m-0" href="/logout">Log out</a></li>
                        </ul>
                    </li>
			</ul>
			
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
  