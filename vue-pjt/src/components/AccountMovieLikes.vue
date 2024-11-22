<template>
    <div>
        <h2>My Movies</h2>
        <p>내가 선호하는 장르 : </p>
        <div class="MovieCardContainer">
        <MovieCard v-for="movie in likedList" :key="movie.id" @click="watchDetail(movie.id)" :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import MovieCard from '@/components/MovieCard.vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useMovieStore()
onMounted(async function() {
    await store.getLikedMovies()
})
const likedList = computed(() => store.likedMovies)
const watchDetail = function(id) {
    router.push({name:'detail', params: {id}})
}


</script>

<style scoped>
.MovieCardContainer{
    display: flex;
    overflow: auto;
}
</style>