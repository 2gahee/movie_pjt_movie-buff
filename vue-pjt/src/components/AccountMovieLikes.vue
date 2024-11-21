<template>
    <div>
        <h2>My Movies</h2>
        <div class="MovieCardContainer">
        <p v-for="movieId in likedList" :key="movieId" @click="watchDetail(movieId)" :movieId="movieId"> {{movieId}}</p>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
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
    flex-wrap: wrap;
}
</style>