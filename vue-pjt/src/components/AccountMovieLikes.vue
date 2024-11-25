<template>
    <div>
        <h2 class="movies-title">{{ store.userInfo.username }}님의 Movies</h2>
        <!-- <h4 class="movies-genre">{{ store.userInfo.username }}님이 선호하는 장르: </h4> -->
        <div class="MovieCardContainer">
        <MovieCard v-for="movie in likedList" :key="movie.id" @click="watchDetail(movie.id)" :movie="movie"/>
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
.movies-title {
  margin-top: 2rem;        
  margin-left: 3rem;    
}
/* .movies-genre {
  margin-top: 1rem;        
  margin-left: 3rem;    
} */

.MovieCardContainer{
    display: flex;
    overflow: auto;
    padding: 0 3rem;  
    gap: 10px;        
}
</style>