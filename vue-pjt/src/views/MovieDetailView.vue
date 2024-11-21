<template>
    <div>
    <div v-if="movie">
        <div class="whole-container">
            <div class="img-container">
        <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="img">
        <button v-if="true" @click="likeToggle(movie.id, $event)" type="button" class="btn btn-primary">좋아요</button>
        <button v-else type="button" class="btn btn-secondary">좋아요 취소</button>
        
            </div>
        
         <div class="movie-info-container">
            <!-- <p>{{ movie.title }}</p> -->
            <p>{{ movie.original_title }}</p>
            <p>"{{ movie.tagline }}"</p>
            <p>{{ movie.release_date }}</p>
            <p>{{ genreString }}</p>
            <p>{{ Math.floor(movie.runtime / 60) }}시간 {{ movie.runtime % 60 }}분</p>
            <p>{{ Math.round(movie.vote_average * 10) / 10 }}점 ({{ movie.vote_count }}명)</p>
            <p>{{ movie.overview }}</p>
            
         </div>
        </div> 
    </div>
    <div v-else>
        <p>Loading...</p>
    </div>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/counter'
import { onMounted, ref } from 'vue'
const store = useMovieStore()
const route = useRoute()
const movie = ref(null)
const genreString = ref('')
onMounted(async () => {
    const movieId = Number(route.params.id)
    console.log("movieId:", movieId)
    if (!movieId || isNaN(movieId)) {
        console.error("유효하지 않은 movieId입니다.")
        return;
    }

    try {
        movie.value = await store.getMovieDetails(movieId);
        console.log(movie.value);
        genreString.value = movie.value.genres.map(genre => genre.name).join(" / ")
    } catch (error) {
        console.error("영화 정보를 가져오는 중 오류 발생:", error);
    }
})
const likeToggle = function(movieId, event) {
    store.movieLike(movieId, event)
}
</script>

<style scoped>
.whole-container{
    display: flex;
    gap : 20px;
    margin : 20px;
}

.img-container{
    display: flex;
    flex-direction: column;
    width: 20%;
    gap : 10px;
}
.movie-info-container{
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    width: 50%;
}
</style>