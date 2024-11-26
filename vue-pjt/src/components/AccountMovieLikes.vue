<template>
    <div>
        <h2 class="movies-title">{{ store.userInfo.username }}님의 Movies</h2>
        <!-- <h4 class="movies-genre">{{ store.userInfo.username }}님이 선호하는 장르: </h4> -->
        <div v-if="likedList.length === 0" class="no-movies">
            <p>좋아요 누른 영화가 없습니다. 좋아요를 눌러보세요!</p>
            <button @click="goMovies" type="button" class="btn btn-dark">전체 영화 보러가기</button>&ensp;
            <button @click="goCurrentMovies" type="button" class="btn btn-dark">상영 중인 영화 보러가기</button>
        </div>
        <div v-else class="MovieCardContainer">
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

const goMovies = function() {
    router.push({path:'/movies'})
}

const goCurrentMovies = function() {
    router.push({path:'/now-on'})
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

.no-movies {
  /* text-align: center; */
  margin-top: 3rem;
  margin-left: 3rem;
}

.no-movies p {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.MovieCardContainer{
    display: flex;
    overflow: auto;
    padding: 0 3rem;  
    gap: 10px;        
}
</style>