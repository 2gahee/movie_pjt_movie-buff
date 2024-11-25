<template>
  <div>
    <div v-if="movie">
      <div class="mb-4 text-bg-dark rounded-3 jumbo">
        <h1>{{ movie.title }}</h1>
        <p>{{ movie.original_title }}</p>
        <p>{{ genreString }}</p>
        <p>{{ movie.release_date }} · {{ Math.floor(movie.runtime / 60) }}시간 {{ movie.runtime % 60 }}분 · {{ Math.round(movie.vote_average * 10) / 10 }}점 ({{ movie.vote_count }}명)</p>
        <button 
          v-if="store.token && isLiked != null" 
          @click="likeToggle(movie.id)" 
          :class="isLiked ? 'btn btn-secondary btn-lg' : 'btn btn-primary btn-lg'">
          {{ isLiked ? '좋아요 취소' : '좋아요' }}
        </button>
        <button v-else class="btn btn-secondary btn-lg" disabled>로그인 후 좋아요 가능</button>
      </div>
      <div class="whole-container">
        <div class="img-container">
          <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="img">
        </div>
        <div class="movie-info-container">
          <p>"{{ movie.tagline }}"</p>
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
import { onMounted, ref, computed, watch } from 'vue'

const store = useMovieStore()
const route = useRoute()
const movie = ref(null)
const genreString = ref('')
const isLiked= ref(null)
const movieId = Number(route.params.id)

onMounted(async () => {
  console.log("movieId:", movieId)
  if (!movieId || isNaN(movieId)) {
    console.error("유효하지 않은 movieId입니다.")
    return
  }

  try {
    movie.value = await store.getMovieDetails(movieId);
    await store.getLikedMovies();
    console.log(movie.value);
    genreString.value = movie.value.genres.map(genre => genre.name).join(" / ");

    const likedMovie = store.likedMovies.find((movie) => movie.id === movieId);
    isLiked.value = !!likedMovie;
    // 배경 이미지 설정
    const jumboElement = document.querySelector('.jumbo');
    jumboElement.style.backgroundImage = `url('https://image.tmdb.org/t/p/original/${movie.value.backdrop_path}')`;
  } catch (error) {
    console.error("영화 정보를 가져오는 중 오류 발생:", error);
  }
})

const likeToggle = async function(movieId) {
  try {
    await store.movieLike(movieId)
    isLiked.value = !isLiked.value
  } catch (error) {
    console.error("좋아요 토글 중 오류 발생:", error);
  }
}

</script>

<style scoped>
.jumbo {
    background-size: cover; 
    background-position: center; 
    background-repeat: no-repeat;
    width: 80%;
    margin: 20px;
    height: 300px;
    display: flex;
    flex-direction: column;
    padding: 40px;
    gap : -10px;
    align-items: flex-start;
}
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
