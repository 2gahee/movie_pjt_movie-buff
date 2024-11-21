<template>
    <div>
        <div class="card movieCard" style="width: 18rem;">
        <img class="card-img-top" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="img" width=300px>
        <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
  </div>
</div>
    </div>
</template>

<script setup>
defineProps({
    movie: Object
})
</script>

<style scoped>
.movieCard {
    margin : 10px;
}
</style>