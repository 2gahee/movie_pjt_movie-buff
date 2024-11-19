<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-dark border-bottom border-body" >
    <div class="container-fluid">
      <RouterLink to="/" class="navbar-brand">로고</RouterLink>
      <button
        class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarNav" 
        aria-controls="navbarNav" 
        aria-expanded="false" 
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">

        <ul class="navbar-nav">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/movies" class="nav-link">Movies</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/now-on" class="nav-link">Now On</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/articles" class="nav-link">Community</RouterLink>
         </li>
        </ul>

        <ul class="navbar-nav ms-auto">
          <li class="nav-item2">
            <RouterLink to="/mypage" class="nav-link">MyPage</RouterLink>
          </li>
          <li class="nav-item2">
            <RouterLink to="/login" class="nav-link">LogIn</RouterLink>
          </li>
          <li class="nav-item2">
            <RouterLink to="/signup" class="nav-link">SignUp</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>


<style  scoped>

</style>
