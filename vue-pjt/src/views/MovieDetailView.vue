<!-- <template>
  <div class="all">
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
        <MovieEvent v-if="title!=null" :title="title"/>
      </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template> -->
<template>
  <div class="all">
    <div v-if="movie">
      <div class="mb-4 text-bg-dark rounded-3 jumbo">
        <!-- 텍스트 콘텐츠 -->
        <div class="jumbo-text">
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

        <!-- 이미지 컨테이너 -->
        <div class="img-container">
          <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="img">
        </div>
      </div>

      <div class="whole-container">
        <div class="movie-info-container">
          <p>"{{ movie.tagline }}"</p>
          <p>{{ movie.overview }}</p>
        </div>
        <MovieEvent v-if="title != null" :title="title" />
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
import MovieEvent from '@/components/MovieEvent.vue';

const store = useMovieStore()
const route = useRoute()
const movie = ref(null)
const genreString = ref('')
const isLiked= ref(null)
const movieId = Number(route.params.id)
const title = ref(null)
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
    title.value = movie.value.title
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
/* .all {
  display: flex;
  justify-content: center;
} */

/* .jumbo {
    background-size: cover; 
    background-position: center; 
    background-repeat: no-repeat;
    width: 70%;
    margin: 20px;
    height: 400px;
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
    width: 40%;
} */


.jumbo {
  background-size: cover;
  background-repeat: no-repeat;
  width: 80%;
  margin: 20px;
  height: 400px;
  display: flex;
  flex-direction: row; /* 행 방향으로 배치 */
  justify-content: space-between; /* 양 끝으로 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  padding: 40px;
  gap: 20px;
  background-color: rgba(15, 15, 15, .5);
}

.jumbo-text {
  flex: 2; /* 텍스트 영역 비율 */
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.img-container {
  flex: 1; /* 이미지 영역 비율 */
  max-width: 200px; /* 이미지 크기 제한 */
  height: auto;
}

.img-container img {
  width: 100%;
  height: auto;
  border-radius: 8px; /* 둥근 테두리 추가 (선택 사항) */
}

button {
  width: 15rem;
}


/* 밑에 두 개는 메가박스에서 퍼옴  */
/* .movie-detail-page {
    position: relative;
    z-index: 1;
    height: 520px;
    margin: 0 0 40px 0;
    color: #ccc;
    background-color: #151515;
}

.movie-detail-page .bg-img:after {
    content: '';
    display: block;
    position: absolute;
    left: 0;
    top: 0;
    z-index: 2;
    width: 100%;
    height: 100%;
    background-color: rgba(15, 15, 15, .5);
} */
</style>
